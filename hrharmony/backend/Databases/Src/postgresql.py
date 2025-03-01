import os

import psycopg2
from dotenv import load_dotenv

load_dotenv()


def create_user(email, department, first_name, last_name, password):
  conn = psycopg2.connect(
    host=os.getenv("RDS_ENDPOINT"),
    database="postgres",
    user=os.getenv("RDS_USERNAME"),
    password=os.getenv("RDS_PASSWORD"),
    port="5432"
  )
  cur = conn.cursor()

  cur.execute(f'''INSERT INTO users (email, department, first_name, last_name, password) VALUES
    ('{email}', '{department}', '{first_name}', '{last_name}', '{password}')
  ''')

  conn.commit()

  cur.close()
  conn.close()
