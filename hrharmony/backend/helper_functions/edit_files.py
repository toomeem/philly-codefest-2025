import os
import uuid

import boto3
from dotenv import load_dotenv

load_dotenv()

S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME")
AWS_REGION = os.getenv("AWS_REGION")
IAM_PUBLIC_KEY = os.getenv("IAM_PUBLIC_KEY")
IAM_PRIVATE_KEY = os.getenv("IAM_PRIVATE_KEY")

def upload_file(file_name, organization_id):
  s3_client = boto3.client(
    service_name="s3",
    region_name=AWS_REGION,
    aws_access_key_id=IAM_PUBLIC_KEY,
    aws_secret_access_key=IAM_PRIVATE_KEY
  )
  id = str(uuid.uuid4())

  save_name = f"{organization_id}/{id}"
  response = s3_client.upload_file(file_name, S3_BUCKET_NAME, save_name)
  if response:
    return {"success": False}
  return {"success": True, "id": id}

upload_file("../README.md")
