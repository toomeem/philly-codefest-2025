import random
import string
from pprint import pprint

from Databases.Src.postgresql import create_user as create_user_in_db
from Databases.Src.postgresql import fetch_user
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
  pprint(request_data)
  email = request_data["email"]
  department = request_data["department"]
  first_name = request_data["first_name"]
  last_name = request_data["last_name"]
  password = generate_password()
  create_user_in_db(email, department, first_name, last_name, password)
  return {"password": password}

@app.route("/user", methods=["GET"])
def get_user():
  request_data = request.get_json()
  email = request_data["email"]
  password = request_data["password"]
  user = fetch_user(email, password)
  return {"user": user}

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8080)
