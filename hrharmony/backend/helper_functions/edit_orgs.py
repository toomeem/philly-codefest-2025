import os
import uuid
import psycopg2
from dotenv import load_dotenv


def create_org_in_db(orgid, name, admin=None ):
  id = str(uuid.uuid4())
  conn = psycopg2.connect(
    host=os.getenv("RDS_ENDPOINT"),
    database="postgres",
    user=os.getenv("RDS_USERNAME"),
    password=os.getenv("RDS_PASSWORD"),
    port="5432"
  )
  cur = conn.cursor()
  cur.execute(f'''INSERT INTO orgs (id, admin, name) VALUES
  ('{orgid}', '{admin}', '{name}')''')
  conn.commit()
  cur.close()
  conn.close()
  return True
  

def fetch_org_in_db(id=None, email=None, password=None):
  conn = psycopg2.connect(
    host=os.getenv("RDS_ENDPOINT"),
    database="postgres",
    user=os.getenv("RDS_USERNAME"),
    password=os.getenv("RDS_PASSWORD"),
    port="5432"
  )
  cur = conn.cursor()
  if id:
    cur.execute(f"SELECT * FROM orgs WHERE id='{id}'")
  else:
    cur.close()
    conn.close()
    return
  user = cur.fetchone()
  cur.close()
  conn.close()
  return user


def update_org_in_db(id, name= None, admin=None):
 user = fetch_org_in_db(id=id)
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
 if name:
    cur.execute(f"UPDATE orgs SET name='{name}' WHERE id='{id}'")
 if admin:
    cur.execute(f"UPDATE orgs SET admin='{admin}' WHERE id='{id}'")

 conn.commit()
 cur.close()
 return True


def delete_org_in_db():
  user = fetch_org_in_db(id=id)
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
  cur.execute(f"DELETE FROM orgs WHERE id='{id}'")
  conn.commit()
  cur.close()
  conn.close()
  return True


def drop_org_db():
  conn = psycopg2.connect(
    host=os.getenv("RDS_ENDPOINT"),
    database="postgres",
    user=os.getenv("RDS_USERNAME"),
    password=os.getenv("RDS_PASSWORD"),
    port="5432"
  )
  cur = conn.cursor()
  cur.execute("DROP TABLE orgs")
  conn.commit()
  cur.close()
  conn.close()

def create_org_db():
  conn = psycopg2.connect(
    host=os.getenv("RDS_ENDPOINT"),
    database="postgres",
    user=os.getenv("RDS_USERNAME"),
    password=os.getenv("RDS_PASSWORD"),
    port="5432"
  )
  cur = conn.cursor()
  cur.execute('''CREATE TABLE IF NOT EXISTS orgs (
    orgid VARCHAR(255) PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    admin VARCHAR(255) NOT NULL,
  )''')
  conn.commit()
  cur.close()
  conn.close()


def __fetch_all_orgs():
  conn = psycopg2.connect(
    host=os.getenv("RDS_ENDPOINT"),
    database="postgres",
    user=os.getenv("RDS_USERNAME"),
    password=os.getenv("RDS_PASSWORD"),
    port="5432"
  )
  cur = conn.cursor()
  cur.execute("SELECT * FROM orgs")
  users = cur.fetchall()
  cur.close()
  conn.close()
  return users
