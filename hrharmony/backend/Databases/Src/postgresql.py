import os
import uuid

import psycopg2
from dotenv import load_dotenv

load_dotenv()


def create_user(email, department, first_name, last_name, password):
  id = str(uuid.uuid4())
  conn = psycopg2.connect(
    host=os.getenv("RDS_ENDPOINT"),
    database="postgres",
    user=os.getenv("RDS_USERNAME"),
    password=os.getenv("RDS_PASSWORD"),
    port="5432"
  )
  cur = conn.cursor()
  cur.execute(f'''INSERT INTO users (id, email, department, first_name, last_name, password) VALUES
  ('{id}', '{email}', '{department}', '{first_name}', '{last_name}', '{password}')''')
  conn.commit()
  cur.close()
  conn.close()

def fetch_user(id=None, email=None, password=None):
  conn = psycopg2.connect(
    host=os.getenv("RDS_ENDPOINT"),
    database="postgres",
    user=os.getenv("RDS_USERNAME"),
    password=os.getenv("RDS_PASSWORD"),
    port="5432"
  )
  cur = conn.cursor()
  if id:
    cur.execute(f"SELECT * FROM users WHERE id='{id}'")
  elif email and password:
    cur.execute(f"SELECT * FROM users WHERE email='{email}' AND password='{password}'")
  else:
    return
  user = cur.fetchone()
  cur.close()
  conn.close()
  return user

def update_user(id, email=None, department=None, first_name=None, last_name=None, password=None):
  user = fetch_user(id=id)
  if not user:
    return
  conn = psycopg2.connect(
    host=os.getenv("RDS_ENDPOINT"),
    database="postgres",
    user=os.getenv("RDS_USERNAME"),
    password=os.getenv("RDS_PASSWORD"),
    port="5432"
  )
  cur = conn.cursor()
  if email:
    cur.execute(f"UPDATE users SET email='{email}' WHERE id='{id}'")
  if department:
    cur.execute(f"UPDATE users SET department='{department}' WHERE id='{id}'")
  if first_name:
    cur.execute(f"UPDATE users SET first_name='{first_name}' WHERE id='{id}'")
  if last_name:
    cur.execute(f"UPDATE users SET last_name='{last_name}' WHERE id='{id}'")
  if password:
    cur.execute(f"UPDATE users SET password='{password}' WHERE id='{id}'")
  conn.commit()
  cur.close()

def drop_db():
  conn = psycopg2.connect(
    host=os.getenv("RDS_ENDPOINT"),
    database="postgres",
    user=os.getenv("RDS_USERNAME"),
    password=os.getenv("RDS_PASSWORD"),
    port="5432"
  )
  cur = conn.cursor()
  cur.execute("DROP TABLE users")
  conn.commit()
  cur.close()
  conn.close()

def create_db():
  conn = psycopg2.connect(
    host=os.getenv("RDS_ENDPOINT"),
    database="postgres",
    user=os.getenv("RDS_USERNAME"),
    password=os.getenv("RDS_PASSWORD"),
    port="5432"
  )
  cur = conn.cursor()
  cur.execute('''CREATE TABLE IF NOT EXISTS users (
    id VARCHAR(255) PRIMARY KEY,
    email VARCHAR(255) NOT NULL,
    department VARCHAR(255) NOT NULL,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
  )''')
  conn.commit()
  cur.close()
  conn.close()
