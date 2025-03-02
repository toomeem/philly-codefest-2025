import os
import uuid

import boto3
import psycopg2
from dotenv import load_dotenv

load_dotenv()


def upload_file_to_s3(organization_id, file_name):
  S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME")
  AWS_REGION = os.getenv("AWS_REGION")
  IAM_PUBLIC_KEY = os.getenv("IAM_PUBLIC_KEY")
  IAM_PRIVATE_KEY = os.getenv("IAM_PRIVATE_KEY")
  s3_client = boto3.client(
    service_name="s3",
    region_name=AWS_REGION,
    aws_access_key_id=IAM_PUBLIC_KEY,
    aws_secret_access_key=IAM_PRIVATE_KEY
  )
  file_path = f"../tmp/{file_name}"
  id = str(uuid.uuid4())
  save_name = f"{organization_id}/{id}"
  response = s3_client.upload_file(file_path, S3_BUCKET_NAME, save_name)
  if response:
    return {"success": False}
  return {"success": True, "id": id}

def delete_file_from_s3(organization_id, file_id):
  S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME")
  AWS_REGION = os.getenv("AWS_REGION")
  IAM_PUBLIC_KEY = os.getenv("IAM_PUBLIC_KEY")
  IAM_PRIVATE_KEY = os.getenv("IAM_PRIVATE_KEY")
  s3_client = boto3.client(
    service_name="s3",
    region_name=AWS_REGION,
    aws_access_key_id=IAM_PUBLIC_KEY,
    aws_secret_access_key=IAM_PRIVATE_KEY
  )

  save_name = f"{organization_id}/{file_id}"
  response = s3_client.delete_object(Bucket=S3_BUCKET_NAME, Key=save_name)
  return {"success": bool(response)}

def create_file_in_db(id, name, org_id, departments):
  conn = psycopg2.connect(
    host=os.getenv("RDS_ENDPOINT"),
    database="postgres",
    user=os.getenv("RDS_USERNAME"),
    password=os.getenv("RDS_PASSWORD"),
    port="5432"
  )
  cur = conn.cursor()
  cur.execute(f'''INSERT INTO files (id, name, org_id, departments) VALUES
  ('{id}', '{name}', '{org_id}', '{departments}')''')
  conn.commit()
  cur.close()
  conn.close()
  return True

def fetch_department_files_in_db(org_id, department):
  conn = psycopg2.connect(
    host=os.getenv("RDS_ENDPOINT"),
    database="postgres",
    user=os.getenv("RDS_USERNAME"),
    password=os.getenv("RDS_PASSWORD"),
    port="5432"
  )
  cur = conn.cursor()
  cur.execute(f"SELECT * FROM files WHERE org_id='{org_id}'")
  files = cur.fetchall()
  cur.close()
  conn.close()
  department_files = []
  for file in files:
    if department in list(file[3]):
      department_files.append(file)
  return department_files

def fetch_file_in_db(id):
  conn = psycopg2.connect(
    host=os.getenv("RDS_ENDPOINT"),
    database="postgres",
    user=os.getenv("RDS_USERNAME"),
    password=os.getenv("RDS_PASSWORD"),
    port="5432"
  )
  cur = conn.cursor()
  cur.execute(f"SELECT * FROM files WHERE id='{id}'")
  file = cur.fetchone()
  cur.close()
  conn.close()
  return file

def update_file_in_db(id, name=None, org_id=None, departments=None):
  file = fetch_file_in_db(id=id)
  if not file:
    return
  conn = psycopg2.connect(
    host=os.getenv("RDS_ENDPOINT"),
    database="postgres",
    user=os.getenv("RDS_USERNAME"),
    password=os.getenv("RDS_PASSWORD"),
    port="5432"
  )
  cur = conn.cursor()
  if name:
    cur.execute(f"UPDATE files SET name='{name}' WHERE id='{id}'")
  if org_id:
    cur.execute(f"UPDATE files SET org_id='{org_id}' WHERE id='{id}'")
  if departments:
    cur.execute(f"UPDATE files SET departments='{departments}' WHERE id='{id}'")
  conn.commit()
  cur.close()
  return True

