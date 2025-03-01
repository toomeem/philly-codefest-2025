import os

from astrapy import DataAPIClient
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
DATASTAX_KEY = os.getenv('DATASTAX_KEY')

client = OpenAI(api_key=OPENAI_API_KEY)

# function to create embedding
def createEmbedding(phrase):

    response = client.embeddings.create(
    input="Your text string goes here",
    model="text-embedding-3-small"
    )

    return response



# Initialize the client
client = DataAPIClient(DATASTAX_KEY)
db = client.get_database_by_api_endpoint(
  "https://c092bc40-37e0-425d-a7e6-ffc06427de9e-us-east-2.apps.astra.datastax.com"
)

print(f"Connected to Astra DB: {db.list_collection_names()}")
