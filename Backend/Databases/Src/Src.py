from openai import OpenAI

client = OpenAI(api_key="Add key here") 

response = client.embeddings.create(
    input="Your text string goes here",
    model="text-embedding-3-small"
)

print(response.data[0].embedding)