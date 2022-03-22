import psycopg2
import pandas as pd


def create_sql_table():

    create_query = """CREATE TABLE employee(
        FIRST_NAME VARCHAR(30),
        LAST_NAME VARCHAR(30),
        EMPLOYEE_ID VARCHAR(30),
        AGE NUMERIC,
        GENDER VARCHAR(1))"""

    try:
        connection = psycopg2.connect(host="postgres", database="airflow", user="airflow", password="airflow",
                                      port='5432')

        print("Database successfully connected.")
        cur = connection.cursor()
        print("Cursor defined")
        cur.execute(create_query)
        print("Successfully created table.")

    except:
        print("Could not create table. Unknown error occurred")

    finally:
        if connection is not None:
            connection.commit()
            connection.close()
