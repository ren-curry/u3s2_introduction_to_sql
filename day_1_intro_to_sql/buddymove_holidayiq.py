"""
This module contains Part 1 of the assignment
Assigment - Part 2, Making and populating a Database
"""
import sqlite3
import pandas as pd


# Query Strings
QRY_TOTAL_RECORDS = '''
                    SELECT COUNT(*)
                    FROM review
                    '''
QRY_NATURE_SHOPPING_USERS = '''
                            SELECT COUNT(*)
                            FROM review r
                            WHERE r.Nature >= 100
                            AND r.Shopping >= 100
                            '''
QRY_AVG_REVIEWS = '''
                  SELECT AVG(Sports), AVG(Religious), AVG(Nature),
                    AVG(Theatre), AVG(Shopping), AVG(Picnic)
                  FROM review r
                  '''


def connect_to_database(db_name):
    conn = sqlite3.connect(db_name)
    return conn


def retrieve_csv(url):
    csv_results = pd.read_csv(url)
    return csv_results


def execute_read(cursor, query):
    cursor.execute(query)
    return cursor.fetchall()


def main_script():
    db_name = 'buddymove_holidayiq.sqlite3'
    conn = connect_to_database(db_name)
    cursor = conn.cursor()

    url = 'buddymove_holidayiq.csv'
    df = retrieve_csv(url)

    df.to_sql('review', con=conn, if_exists='replace')

    total_records = execute_read(cursor, QRY_TOTAL_RECORDS)
    nature_shopping_users = execute_read(cursor, QRY_NATURE_SHOPPING_USERS)
    average_reviews = execute_read(cursor, QRY_AVG_REVIEWS)

    total_records = total_records[0][0]
    nature_shopping_users = nature_shopping_users[0][0]

    string2 = (f"There are {nature_shopping_users} users"
               " with 100 or more reviews in"
               " Nature and Shopping."
               )

    print(f"There are {total_records} in the table 'review'.")
    print(string2)
    print(f"The average reviews for 'Sports' is: {average_reviews[0][0]}")
    print(f"The average reviews for 'Religious' is: {average_reviews[0][1]}")
    print(f"The average reviews for 'Nature' is: {average_reviews[0][2]}")
    print(f"The average reviews for 'Theatre' is: {average_reviews[0][3]}")
    print(f"The average reviews for 'Shopping' is: {average_reviews[0][4]}")
    print(f"The average reviews for 'Picnic' is: {average_reviews[0][5]}")


if __name__ == '__main__':
    main_script()
