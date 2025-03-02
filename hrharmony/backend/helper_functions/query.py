import json
import os

import vector_database
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

def get_bot_response(user_id, query, chat_messages=None):
  chat_log_path = "backend/Databases/chat_log.json"
  with open("backend/Databases/system_prompt.txt") as file:
    SYSTEM_PROMPT = file.read()

  # Check if the chat log file exists and is not empty
  try:
    with open(chat_log_path, "r") as f:
      all_messages = json.load(f)
  except json.JSONDecodeError:
    print(f"Error reading JSON from {chat_log_path}. The file may be corrupt.")
    all_messages = {}
  if user_id in all_messages.keys():
    chat_messages = all_messages[user_id]
  else:
    chat_messages = [{"role": "system", "content": SYSTEM_PROMPT}]
  # Retrieve relevant chunks from vector database
  chunks = vector_database.searchEmbedding(query)
  # Read the user query template
  with open('backend/helper_functions/user_query_template.txt') as file:
    user_prompt = file.read()
  # Replace placeholders
  user_prompt = user_prompt.replace("{USER_QUERY}", query)
  for i in range(min(5, len(chunks))):  # Ensure there are enough chunks
    user_prompt = user_prompt.replace("{CHUNK_" + str(i+1) + "}", chunks[i].page_content)
  # Create the OpenAI client
  client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
  )

  # Add the user query to the chat history
  chat_messages.append({"role": "user", "content": user_prompt})

  # Request completion from GPT-4
  completion = client.chat.completions.create(
      model="gpt-4o-mini",
      messages=chat_messages
  )
  # Extract the response
  response = completion.choices[0].message.content
  # update last message so that its only the user query
  chat_messages[-1]["content"] = query
  chat_messages.append({"role": "assistant", "content": response})
  all_messages[user_id] = chat_messages
  # Save the updated chat log back to the JSON file
  with open(chat_log_path, "w") as f:
    json.dump(all_messages, f, indent=2)

  return response



get_bot_response("what is my hourly pay")
