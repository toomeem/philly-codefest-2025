import random
import string

import boto3
from flask import Flask, request

app = Flask(__name__)


def generate_password():
  characters = string.ascii_letters + string.digits + string.punctuation
  password = "".join(random.choice(characters) for _ in range(12))
  return password

@app.route("/", methods=["GET"])
def home():
  return "HR Harmony"

@app.route("/upload_file", methods=["POST"])
def upload_file():
  file = request.files["file"]

  file.save(f"uploads/{file.filename}")
  return "200"


@app.route("/user", methods=["POST"])
def create_user():
  request_data = request.get_json()
  email = request_data["email"]
  department = request_data["department"]
  first_name = request_data["first_name"]
  last_name = request_data["last_name"]
  password = generate_password()
  return "200"



if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0", port=8080)
