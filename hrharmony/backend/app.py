import random
import string
from pprint import pprint

from flask import Flask, request

from backend.helper_functions.edit_users import (fetch_user,update_user_in_db, create_user_in_db, delete_user_in_db)
from backend.helper_functions.edit_files import upload_file_to_s3
app = Flask(__name__)


def generate_password():
  characters = string.ascii_letters + string.digits + string.punctuation
  password = "".join(random.choice(characters) for _ in range(12))
  return password

@app.route("/", methods=["GET"])
def home():
  return "HR Harmony"

@app.route("/file", methods=["POST"])
def upload_file():
  file = request.files["file"]
  file_name = file.filename
  organization_id = request.form["organization_id"]
  file.save(f"tmp/{file_name}")
  return upload_file_to_s3(organization_id, file_name)


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

@app.route("/user", methods=["PUT"])
def update_user():
  request_data = request.get_json()
  id = request_data["id"]
  success = update_user_in_db(id, **request_data)
  return {"success": success}

@app.route("/user", methods=["DELETE"])
def delete_user():
  request_data = request.get_json()
  id = request_data["id"]
  success = delete_user_in_db(id)
  return {"success": success}

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8080)
