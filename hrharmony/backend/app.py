import random
import string
import uuid
from pprint import pprint

import requests
from flask import Flask, request, jsonify
from flask_cors import CORS
import helper_functions.edit_files
import helper_functions.edit_users
import helper_functions.edit_orgs
import helper_functions.query
import helper_functions.vector_database
app = Flask(__name__)
CORS(app)

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

  response = helper_functions.edit_files.upload_file_to_s3(organization_id, file_id)
  if response["success"]:
    helper_functions.edit_files.create_file_in_db(file_id, file_name, organization_id, departments)
    helper_functions.vector_database.addFile(file_name)
  return response


@app.route("/user", methods=["POST"])
def create_user():
  request_data = request.get_json()
  print(request_data)
  email = request_data["email"]
  org_id = request_data["org_id"]
  department = request_data["department"]
  first_name = request_data["first_name"]
  last_name = request_data["last_name"]
  password = generate_password()
  success = helper_functions.edit_users.create_user_in_db(email, org_id, department, first_name, last_name, password)
  print(success)
  return {"password": password, "success": success}, 200

@app.route("/user", methods=["GET"])
def get_user():
  request_data = request.get_json()
  email = request_data["email"]
  password = request_data["password"]
  user = helper_functions.edit_users.fetch_user_in_db(email, password)
  return {"user": user}

@app.route("/org_users", methods=["GET"])
def get_org_users():
  request_data = request.get_json()
  org_id = request_data["org_id"]
  print(org_id)
  users_tuple = helper_functions.edit_users.fetch_org_users_in_db(org_id)
  users = []
  for user in users_tuple:
    users.append({
      "id": user[0],
      "org_id": user[1],
      "email": user[2],
      "department": user[3],
      "first_name": user[4],
      "last_name": user[5]
    })
  return jsonify(users), 200

@app.route("/user", methods=["PUT"])
def update_user():
  request_data = request.get_json()
  id = request_data["id"]
  success = helper_functions.edit_users.update_user_in_db(id, **request_data)
  return {"success": success}

@app.route("/user", methods=["DELETE"])
def delete_user():
  request_data = request.get_json()
  id = request_data["id"]
  success = helper_functions.edit_users.delete_user_in_db(id)
  return {"success": success}


@app.route("/org", methods=["POST"])
def create_org():
  request_data = request.get_json()
  print(request_data)
  orgid = request_data["orgid"]
  name = request_data["name"]
  if"admin" in request_data.keys():
    admin = request_data["admin"]
  else:
    admin = None
  success = helper_functions.edit_users.create_user_in_db(orgid,name,admin)
  print(success)

@app.route("/org", methods=["GET"])
def get_org():
  request_data = request.get_json()
  id = request_data["orgid"]
  org = helper_functions.edit_orgs.fetch_org_in_db(id)
  return {"user": org}

@app.route("/org", methods=["PUT"])
def update_org():
  request_data = request.get_json()
  id = request_data["orgid"]
  success = helper_functions.edit_orgs.update_org_in_db(id, **request_data)
  return {"success": success}

@app.route("/org", methods=["DELETE"])
def delete_org():
  request_data = request.get_json()
  id = request_data["orgid"]
  success = helper_functions.edit_orgs.delete_org_in_db(id)
  return {"success": success}

@app.route("/chat", methods=["POST"])
def send_message():
  request_data = request.get_json()
  user_id = request_data["user_id"]
  query = request_data["query"]
  user = helper_functions.edit_users.fetch_user_in_db(id=user_id)
  if user is None:
    return {"error": "User not found"}, 404
  user_id = user[0]
  response = helper_functions.query.get_bot_response(user_id, query)
  return {"response": response}

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8080)
