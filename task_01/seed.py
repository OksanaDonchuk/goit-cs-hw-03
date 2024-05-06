import logging
from faker import Faker
from psycopg2 import DatabaseError
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="my_db@2024",
)

cur = conn.cursor()


for _ in range(10):
    fullname = Faker().name() + Faker().last_name()
    email = Faker().email()
    cur.execute("INSERT INTO users (fullname, email) VALUES (%s, %s)", (fullname, email))


for status in [('new',), ('in progress',), ('completed',)]:
    cur.execute("INSERT INTO status (name) VALUES (%s)", (status,))


for _ in range(30):
    title = Faker().sentence()
    description = Faker().paragraph()
    user_id = Faker().random_int(min=1, max=10)
    status_id = Faker().random_int(min=1, max=3)
    cur.execute("INSERT INTO tasks (title, description, user_id, status_id) VALUES (%s, %s, %s, %s)", (title, description, user_id, status_id))


try:
    conn.commit()
except DatabaseError as e:
    logging.error(e)
finally:
    conn.close()