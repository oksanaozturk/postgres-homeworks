"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv
import os
import psycopg2

postgres_key = os.getenv('POSTGRES_SQL_KEY')

conn = psycopg2.connect(
        host="Localhost",
        database="north",
        user="postgres",
        password=postgres_key
    )

try:
    with conn:
        with conn.cursor() as cur:
            with open('north_data/customers_data.csv', 'r', encoding='UTF-8') as file:
                data = csv.reader(file)
                next(data)
                for row in data:
                    element = ', '.join(['%s'] * len(row))
                    query = f"INSERT INTO customers_data VALUES ({element})"
                    cur.execute(query, row)

            with open('north_data/employees_data.csv', 'r', encoding='UTF-8') as file:
                data = csv.reader(file)
                next(data)
                for row in data:
                    element = ', '.join(['%s'] * len(row))
                    query = f"INSERT INTO employees_data VALUES ({element})"
                    cur.execute(query, row)

            with open('north_data/orders_data.csv', 'r', encoding='UTF-8') as file:
                data = csv.reader(file)
                next(data)
                for row in data:
                    element = ', '.join(['%s'] * len(row))
                    query = f"INSERT INTO orders_data VALUES ({element})"
                    cur.execute(query, row)

finally:
    conn.close()



