from openai import OpenAI
from astrapy import DataAPIClient
import os
from dotenv import load_dotenv
from langchain.text_splitter import RecursiveCharacterTextSplitter


# Load environment variables
load_dotenv()

# Debug: Check if API keys are loaded
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
DATASTAX_KEY = os.getenv('DATASTAX_KEY')

if not DATASTAX_KEY:
    raise ValueError("ERROR: DATASTAX_KEY is not set! Check your .env file.")

# Create clients
clientOpenAI = OpenAI(api_key=OPENAI_API_KEY)
clientDataAPI = DataAPIClient(DATASTAX_KEY)

# Connect to Astra database
database_url = "https://c092bc40-37e0-425d-a7e6-ffc06427de9e-us-east-2.apps.astra.datastax.com"
database = clientDataAPI.get_database(database_url, keyspace="default_keyspace")

# Ensure collection exists
collection_name = "hr_document"

try:
    collection = database.get_collection(collection_name)
except Exception:
    collection = database.create_collection(collection_name)  # No extra args

# Function to create and store embeddings
def createEmbedding(phrase, title):
    response = clientOpenAI.embeddings.create(
        input=phrase,
        model="text-embedding-3-small",
        dimensions = 1024
    )
    embedding = response.data[0].embedding  # Extract embedding vector

    # Insert into database
    collection.insert_one({
        "title": title.strip(),
        "$vector": embedding,  # Store only vector, not full response
    })
    
# Read and process file
def addFile(fileName):
    #constant to hold the length of each chunck
    CHUNK_LEN = 200

    #create text splitter to divide up the file
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = CHUNK_LEN,
        chunk_overlap = round(CHUNK_LEN * .2),
        length_function = len,
        is_separator_regex= False
    )

    #open file and set to read
    with open('Backend/Databases/Documents/' + fileName, 'r', encoding="utf-8") as file:
      text = file.read() # reads file and save as string
    #split string into a list of strings 
    chunks = text_splitter.create_documents([text])
    for c in chunks: # loop through the list
        createEmbedding(c.page_content, fileName)  # Store section in database
               

def searchEmbedding(query):
  # Get an existing collection
  client = DataAPIClient(DATASTAX_KEY)
  database = client.get_database("https://c092bc40-37e0-425d-a7e6-ffc06427de9e-us-east-2.apps.astra.datastax.com")
  collection = database.get_collection("hr_document")

  # Find a document
  result = collection.find_one(
      {},
      sort={"$vectorize": query}
  )

  print(result)


    
searchEmbedding("PTO")