import os

from astrapy import DataAPIClient
from dotenv import load_dotenv
from langchain.text_splitter import RecursiveCharacterTextSplitter
from openai import OpenAI

load_dotenv()

# declare local constants
COLLECTION_NAME = "hr_document"

# Function to create and store embeddings
def createEmbedding(phrase, title):
  # Create clients
  DATABASE_URL = os.getenv("VECTOR_DATABASE_URL")
  COLLECTION_NAME = "hr_document"
  OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
  clientOpenAI = OpenAI(api_key=OPENAI_API_KEY)
  response = clientOpenAI.embeddings.create(
    input=phrase,
    model="text-embedding-3-small",
    dimensions = 1024
  )
  embedding = response.data[0].embedding  # Extract embedding vector
  # Insert into database
  DATASTAX_KEY = os.getenv("DATASTAX_KEY")
  clientDataAPI = DataAPIClient(DATASTAX_KEY)
  database = clientDataAPI.get_database(DATABASE_URL, keyspace="default_keyspace")
  collection = database.get_collection(COLLECTION_NAME)
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
  with open("databases/" + fileName) as file:
    text = file.read() # reads file and save as string
  #split string into a list of strings
  chunks = text_splitter.create_documents([text])
  for c in range(len(chunks)): # loop through the list
    createEmbedding(chunks[c].page_content, fileName + "_" + str(c))  # Store section in database

#search for a like query
def searchEmbedding(query):
  DATABASE_URL = os.getenv("VECTOR_DATABASE_URL")
  COLLECTION_NAME = "hr_document"
  DATASTAX_KEY = os.getenv("DATASTAX_KEY")
  client = DataAPIClient(DATASTAX_KEY)
  database = client.get_database(DATABASE_URL)
  collection = database.get_collection(COLLECTION_NAME)
  # Find a document
  result = collection.find_one(
  {},  # Adjust your query to match the data you're looking for
  sort={"$vectorize": query}
  )
  # Check if result is found
  if result is None:
    return("No document found for the query.")
    return
  # Constant to hold the length of each chunk
  CHUNK_LEN = 200
  title = result["title"]

  if not title:
    return("No '_title' found in the result.")
    return
  # Split id into filename and chunk index
  try:
    chunk_index = int(title.split("_")[-1])  # Assuming chunk_index is an integer
    filename = title[:-len(str(chunk_index))-1]  # Remove the chunk index part to get the filename
  except ValueError as e:
    return(f"Error extracting chunk index from title: {e}")
    return
  # Create text splitter to divide up the file
  text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=CHUNK_LEN,
    chunk_overlap=round(CHUNK_LEN * .2),
    length_function=len,
    is_separator_regex=False
  )
  file_path = f"databases/{filename}"
  # Check if the file exists before reading
  if not os.path.exists(file_path):
    return(f"File {filename} does not exist.")
    return

  with open(file_path) as file:
    text = file.read()  # Read the file and save as string
    # Split string into a list of strings (chunks)
    chunks = text_splitter.create_documents([text])
  # Ensure chunk_index is valid before accessing the chunks
  if chunk_index < 0 or chunk_index >= len(chunks):
    return(f"Invalid chunk index: {chunk_index}")
    return
  if len(chunks) < 5:
    return chunks
  return chunks[:5]

def deleteTableEntry(documentId):
  DATABASE_URL = os.getenv("VECTOR_DATABASE_URL")
  COLLECTION_NAME = "hr_document"
  # Replace with your Astra DB credentials
  DATASTAX_KEY = os.getenv("DATASTAX_KEY")
  # Initialize DataAPIClient
  client = DataAPIClient(DATASTAX_KEY)
  db = client.get_database_by_api_endpoint(DATABASE_URL)
  collection = db.get_collection(COLLECTION_NAME)  # Get the collection (table)
  # Delete the document by ID
  collection.delete_one({"_id": documentId})

  print(f"Document with ID {documentId} deleted successfully.")

def clearAllEntries():
  DATABASE_URL = os.getenv("VECTOR_DATABASE_URL")
  COLLECTION_NAME = "hr_document"
  DATASTAX_KEY = os.getenv("DATASTAX_KEY")
  # Initialize DataAPIClient
  client = DataAPIClient(DATASTAX_KEY)
  db = client.get_database_by_api_endpoint(DATABASE_URL)
  collection = db.get_collection(COLLECTION_NAME)  # Get the collection (table)
  # Delete all documents in the collection
  collection.delete_many({})

  print("All documents deleted successfully.")

