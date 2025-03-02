import os
import uuid

import psycopg2
import boto3
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

