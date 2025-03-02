import json
import os

import helper_functions.vector_database
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

def get_bot_response(user_id, query, chat_messages=None):
  chat_log_path = "databases/chat_log.json"
  try:
    with open("databases/system_prompt.txt") as file:
      SYSTEM_PROMPT = file.read()
  except FileNotFoundError:
    return("files in this dir:" + str(os.listdir())+ ":" + str(os.getcwd()))
  # Check if the chat log file exists and is not empty
  try:
    with open(chat_log_path, "r") as f:
      all_messages = json.load(f)
  except:
    all_messages = {}
  if user_id in all_messages.keys():
    chat_messages = all_messages[user_id]
  else:
    chat_messages = [{"role": "system", "content": SYSTEM_PROMPT}]
  # Retrieve relevant chunks from vector database
  chunks = helper_functions.vector_database.searchEmbedding(query)
  if isinstance(chunks, str):
    return chunks
  context_message = {"role": "system", "content": "Here are some relevant chunks from the database:\n"}
  for i in range(min(5, len(chunks))):
    context_message["content"] += "\n" + "\'\'\'"+chunks[i].page_content + "\'\'\'"
  chat_messages.append(context_message)
  chat_messages.append({"role": "user", "content": query})
  # Create the OpenAI client
  client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
  )
  # Request completion from GPT-4
  completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=chat_messages
  )
  # Extract the response
  response = completion.choices[0].message.content
  # update last message to remove chunk content
  chat_messages.append({"role": "assistant", "content": response})
  all_messages[user_id] = list(chat_messages)
  # Save the updated chat log back to the JSON file
  with open(chat_log_path, "w") as f:
    json.dump(all_messages, f, indent=2)

  return response
