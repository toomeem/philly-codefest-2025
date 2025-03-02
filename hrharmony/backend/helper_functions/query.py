import vector_database
from openai import OpenAI
import json
import os

def get_bot_response(query, chat_messages=None):
    chat_log_path = "backend/Databases/chat_log.json"
    
    # Check if the chat log file exists and is not empty
    if os.path.exists(chat_log_path) and os.path.getsize(chat_log_path) > 0:
        with open(chat_log_path, "r") as f:
            try:
                chat_messages = json.load(f)
            except json.JSONDecodeError:
                print(f"Error reading JSON from {chat_log_path}. The file may be corrupt.")
                chat_messages = []
    else:
        print(f"File {chat_log_path} is empty or doesn't exist. Initializing chat_messages.")
        chat_messages = []

    SYSTEM_PROMPT = '''
    You are an HR chatbot designed to assist employees with HR-related inquiries by utilizing the Retrieval-Augmented Generation (RAG) approach. Your task is to provide accurate, helpful, and timely responses to employee questions by retrieving relevant information from the HR knowledge base (policies, handbooks, benefits information, etc.) and generating answers.

    Here’s how you should work:
    1. **Retrieve**: When a user asks a question, retrieve relevant documents, excerpts, or knowledge pieces from the HR knowledge base that may contain answers to the question. The retrieval should focus on HR policies, employee handbooks, and other authoritative resources.

    2. **Generate**: Using the retrieved information, craft a human-readable, clear, and concise response. Make sure the response is tailored to the specific query and context of the employee's situation.

    3. **Contextual Understanding**: Always ensure that the answer is accurate, respectful, and aligned with company policies. If the question is related to something personal (e.g., payroll, personal leave, or benefits), remind employees that they may need to contact HR directly for sensitive or personalized inquiries.

    4. **Handle Ambiguity**: If the question is unclear or you cannot find a relevant answer in the knowledge base, ask follow-up questions to clarify. If no answer is found, inform the user that you were unable to find the information and suggest they contact HR directly.

    5. **Provide References**: Whenever possible, provide citations to the HR knowledge base or documentation from where the information was retrieved so that users can verify the response.

    6. **Tone and Professionalism**: Maintain a professional, friendly, and empathetic tone. Always make employees feel supported and valued.

    ---

    Example questions you should be able to answer:
    - "How do I request vacation time?"
    - "What are the company's benefits policies?"
    - "Can you explain the process for filing a grievance?"
    - "What is the company's policy on remote work?"
    - "How do I update my personal information?"

    Remember, your role is to help employees by providing clear and trustworthy information and making their HR-related processes as smooth as possible.
    '''
    
    # Retrieve relevant chunks from vector database
    chunks = vector_database.searchEmbedding(query)
    
    # Read the user query template
    with open('backend/helper_functions/user_query_template.txt') as file:
        user_prompt = file.read()

    # Replace placeholders in the prompt template with the user query and relevant chunks
    user_prompt = user_prompt.replace("{USER_QUERY}", query)
    for i in range(min(5, len(chunks))):  # Ensure there are enough chunks
        user_prompt = user_prompt.replace("{CHUNK_" + str(i+1) + "}", chunks[i].page_content)
    
    print(user_prompt)  # For debugging
    
    # Create the OpenAI client
    client = OpenAI()

    # Initialize chat history if it's not provided
    if not chat_messages:
        chat_messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    
    # Add the user query to the chat history
    chat_messages.append({"role": "user", "content": user_prompt})

    # Request completion from GPT-4
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=chat_messages
    )
    
    # Extract the response
    response = completion.choices[0].message.content
    chat_messages.append({"role": "assistant", "content": response})

    # Save the updated chat log back to the JSON file
    with open(chat_log_path, "w") as f:
        json.dump(chat_messages, f, indent=4)

    return response



get_bot_response("what is my hourly pay")




    
