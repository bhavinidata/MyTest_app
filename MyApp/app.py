import os
import psycopg2

print("Opening Database connection")

DATABASE_URL = os.environ['DATABASE_URL']

conn = psycopg2.connect(DATABASE_URL, sslmode='require')

cur = conn.cursor()

cur.execute("SELECT * FROM my_test_table;")

print(cur.fetchone())

cur.close()

conn.close()
