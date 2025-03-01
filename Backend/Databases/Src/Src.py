# imports for the program
from openai import OpenAI
from astrapy import DataAPIClient
import os
from dotenv import load_dotenv
load_dotenv()

# key varibles
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
DATASTAX_KEY = os.getenv('DATASTAX_KEY')


# create the client for database acess
client = OpenAI(api_key=OPENAI_API_KEY) 


# Initialize the client
client = DataAPIClient(DATASTAX_KEY)
db = client.get_database_by_api_endpoint(
  "https://c092bc40-37e0-425d-a7e6-ffc06427de9e-us-east-2.apps.astra.datastax.com"
)



# loop to go through all of the regulations
with open('Nexora_HR_Regulations.txt', 'r') as file:
    phrase = ""

    for line in file:

      if (line[0] != "#"):
         phrase = phrase + line

      else:
         #createEmbedding(phrase)
         phrase = ""
         phrase = phrase + line



# function to create embedding
def createEmbedding(phrase):
    response = client.embeddings.create(
    input=phrase,
    model="text-embedding-3-small"
    )

    
   
    



