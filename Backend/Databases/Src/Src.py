from openai import OpenAI
from astrapy import DataAPIClient
import os
from dotenv import load_dotenv
load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
DATASTAX_KEY = os.getenv('DATASTAX_KEY')

client = OpenAI(api_key="Add key here") 
client = OpenAI(api_key=OPENAI_API_KEY) 


# Initialize the client
client = DataAPIClient(DATASTAX_KEY)
db = client.get_database_by_api_endpoint(
  "https://c092bc40-37e0-425d-a7e6-ffc06427de9e-us-east-2.apps.astra.datastax.com"
)




with open('Nexora_HR_Regulations.txt', 'r') as file:
    phrase = ""

    for line in file:

      if (line[0] != "#"):
         phrase = phrase + line

      else:
         #createEmbedding(phrase)
         phrase = ""



# function to create embedding
def createEmbedding(phrase):
    response = client.embeddings.create(
    input=phrase,
    model="text-embedding-3-small"
    )

    
   
    



