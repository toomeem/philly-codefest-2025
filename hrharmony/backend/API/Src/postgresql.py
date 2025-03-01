import psycopg2

conn = psycopg2.connect(
  host="localhost",
  database="users",
  user="postgres",
  password="np139553",
  port="5432"
)
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS users (id serial PRIMARY KEY, email VARCHAR(255), department VARCHAR(255), first_name VARCHAR(255), last_name VARCHAR(255), password VARCHAR(255))")

conn.commit()

cur.close()
conn.close()
