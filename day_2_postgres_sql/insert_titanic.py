"""
This module contains Part 2 of the assignment
Assignment - Part 2, Transfering Data from SQLite3 to PostgreSQL
"""
from csv import reader
import pandas as pd
import configparser
import psycopg2

from queries import (
    r_t_exists_check,
    r_v_select_all,
    c_ty_gender,
    c_ty_pclass,
    c_t_titanic,
    c_v_titanic_data
    )

# Config Setup for connection to PostgreSQL DB
config = configparser.ConfigParser()
config.read('config.ini')
pg_config = config['PostgreSQL']

# Retrieve Config values for PostgreSQL
DBNAME = pg_config['DBNAME']
USER = pg_config['USER']
PASSWORD = pg_config['PASSWORD']
HOST = pg_config['HOST']


# Function to connect to PostgreSQL and return connection and cursor
def connect_pg_db(DBNAME=DBNAME, USER=USER, PASSWORD=PASSWORD, HOST=HOST):
    pg_conn = psycopg2.connect(dbname=DBNAME, user=USER,
                               password=PASSWORD, host=HOST)
    pg_curs = pg_conn.cursor()
    return pg_conn, pg_curs


# Function to return all values from a passed query.
def execute_readall_query(cursor, query):
    cursor.execute(query)
    return cursor.fetchall()


def read_titanic_csv():
    titanic_file = 'titanic.csv'
    with open(titanic_file, 'r') as read_obj:
        csv_reader = reader(read_obj)
        header = next(csv_reader)
        values = []
        for row in csv_reader:
            values.append(row)

    for value in values:
        value[2] = value[2].replace("'", "''")

    return header, values


def execution_function():
    conn, curs = connect_pg_db()

    columns, records = read_titanic_csv()

    exists_query = r_t_exists_check.format('titanic')
    exists = execute_readall_query(curs, exists_query)[0][0]
    if(exists is not True):
        curs.execute(c_t_titanic)

    for record in records:
        insert_query = c_v_titanic_data.format('titanic',
                                               *record
                                               )
        # print(insert_query)
        curs.execute(insert_query)

    conn.commit()


if __name__ == '__main__':
    execution_function()
