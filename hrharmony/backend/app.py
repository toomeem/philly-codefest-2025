import random
import string
import uuid
from pprint import pprint

from flask import Flask, request
from helper_functions.edit_files import upload_file_to_s3
from helper_functions.edit_users import (create_user_in_db, delete_user_in_db,
                                         fetch_user_in_db, update_user_in_db)

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
  if 'file' not in request.files:
    return "No file part", 400

  file = request.files["file"]
  if file.filename == '':
    return "No selected file", 400

  file_id = str(uuid.uuid4())
  file.save(f"tmp/{file_id}")

  file_name = file.filename
  organization_id = request.form.get("organization_id", "")
  departments = request.form.get("departments", "")

  response = upload_file_to_s3(organization_id, file_id)

  return response


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
  user = fetch_user_in_db(email, password)
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
