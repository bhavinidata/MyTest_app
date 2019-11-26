import os
import psycopg2
from flask import Flask

my_awesome_app = Flask(__name__)


@my_awesome_app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    my_awesome_app.run()
    
print("Opening Database connection")

DATABASE_URL = os.environ['DATABASE_URL']

conn = psycopg2.connect(DATABASE_URL, sslmode='require')

cur = conn.cursor()

cur.execute("SELECT * FROM my_test_table;")

print(cur.fetchone())

cur.close()

conn.close()
