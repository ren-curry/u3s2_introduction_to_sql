"""
Unit 3, Sprint 2, Sprint Challenge
Part 1 - Making and populating a Database
Part 1 Question 1: How many rows exist?
    3
Part 1 Question 2: How many records where `x` and `y` are >= 5?
    2
Part 1 Question 3: How many unique values of `y` exist?
    2
"""
import sqlite3


def connect_sl_db(db_name):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    return connection, cursor


def execute_readsingle_query(cursor, query):
    cursor.execute(query)
    return cursor.fetchall()[0][0]


def print_results(results):
    if(isinstance(results, list)):
        for result in results:
            print(result)
    else:
        print(results)


def main():
    dbname = 'demo_data.sqlite3'
    conn, curs = connect_sl_db(dbname)

    exists_query = r_t_exists_check.format('demo')
    exists = int(execute_readsingle_query(curs, exists_query))
    if(exists == 0):
        curs.execute(c_t_demo)
        curs.execute(c_v_demo)
        conn.commit()

    q1 = execute_readsingle_query(curs, row_count)
    q2 = execute_readsingle_query(curs, xy_at_least_5)
    q3 = execute_readsingle_query(curs, unique_y)

    print("Part 1 Question 1: How many rows exist?")
    print_results(q1)
    print("Part 1 Question 2: How many records where `x` and `y` are >= 5?")
    print_results(q2)
    print("Part 1 Question 3: How many unique values of `y` exist?")
    print_results(q3)


# Query Definitions
c_t_demo = (
    "CREATE TABLE IF NOT EXISTS demo ("
    "s CHAR(1), "
    "x INT, "
    "y INT);"
)

c_v_demo = (
    "INSERT INTO demo (s, x, y) "
    "VALUES ('g', 3, 9), ('v', 5, 7), ('f', 8, 7);"
)

row_count = (
    "SELECT COUNT(*) "
    "FROM demo"
)

xy_at_least_5 = (
    "SELECT COUNT(*) "
    "FROM demo "
    "WHERE x >= 5 "
    "AND y >= 5 "
)

unique_y = (
    "SELECT COUNT(DISTINCT y) "
    "FROM demo "
)

r_t_exists_check = (
    "SELECT EXISTS("
    "SELECT * "
    "FROM sqlite_master "
    "WHERE type = 'table' "
    "AND name = '{}');"
    )

if __name__ == '__main__':
    main()
