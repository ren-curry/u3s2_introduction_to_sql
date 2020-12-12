"""
Unit 3, Sprint 2, Sprint Challenge
Part 2 - The Northwind Database
Part 2 Question 1: What are the most expensive items?
    ('Côte de Blaye',)
    ('Thüringer Rostbratwurst',)
    ('Mishi Kobe Niku',)
    ("Sir Rodney's Marmalade",)
    ('Carnarvon Tigers',)
    ('Raclette Courdavault',)
    ('Manjimup Dried Apples',)
    ('Tarte au sucre',)
    ('Ipoh Coffee',)
    ('Rössle Sauerkraut',)
Part 2 Question 2: What is the average age at hire?
    37.28344360787892
Part 2 Question 3: What are the average ages at hire by city?
    ('Kirkland', 28.588637919233403)
    ('London', 32.82819986310746)
    ('Redmond', 55.619438740588635)
    ('Seattle', 39.77275838466804)
    ('Tacoma', 40.48459958932238)

Part 3 - Sailing the Northwind Seas
Part 3 Question 1: What are the most expensive items w/supplier?
    ('Aux joyeux ecclésiastiques', 'Côte de Blaye')
    ('Plutzer Lebensmittelgroßmärkte AG', 'Thüringer Rostbratwurst')
    ('Tokyo Traders', 'Mishi Kobe Niku')
    ('Specialty Biscuits, Ltd.', "Sir Rodney's Marmalade")
    ('Pavlova, Ltd.', 'Carnarvon Tigers')
    ('Gai pâturage', 'Raclette Courdavault')
    ("G'day, Mate", 'Manjimup Dried Apples')
    ("Forêts d'érables", 'Tarte au sucre')
    ('Leka Trading', 'Ipoh Coffee')
    ('Plutzer Lebensmittelgroßmärkte AG', 'Rössle Sauerkraut')
Part 3 Question 2: What are the largest category of products?
    Confections
Part 3 Question 3: Which employee has the most territories?
    ('King', 'Robert')
"""
import sqlite3


def connect_sl_db(db_name):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    return connection, cursor


def execute_readall_query(cursor, query):
    cursor.execute(query)
    return cursor.fetchall()


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
    conn, curs = connect_sl_db('northwind_small.sqlite3')

    # Retrieve Query results
    q2_1 = execute_readall_query(curs, expensive_items)
    q2_2 = execute_readsingle_query(curs, avg_hire_age)
    q2_3 = execute_readall_query(curs, r_v_avg_age_athire_bycity)
    q3_1 = execute_readall_query(curs, r_v_most_expensive_bysupplier)
    q3_2 = execute_readsingle_query(curs, r_v_largest_category)
    q3_3 = execute_readall_query(curs, r_v_most_territories)

    print("Part 2 Question 1: What are the most expensive items?")
    print_results(q2_1)
    print("Part 2 Question 2: What is the average age at hire?")
    print_results(q2_2)
    print("Part 2 Question 3: What are the average ages at hire by city?")
    print_results(q2_3)
    print("Part 3 Question 1: What are the most expensive items w/supplier?")
    print_results(q3_1)
    print("Part 3 Question 2: What are the largest category of products?")
    print_results(q3_2)
    print("Part 3 Question 3: Which employee has the most territories?")
    print_results(q3_3)


# Query Definitions
# Part 2 Queries
expensive_items = (
    "SELECT ProductName "
    "FROM Product "
    "ORDER BY UnitPrice DESC "
    "LIMIT 10;"
)

avg_hire_age = (
    "SELECT AVG((julianday(HireDate) - julianday(BirthDate))/365.25) "
    "AS 'Average Age at Hire' "
    "FROM Employee;"
)

r_v_avg_age_athire_bycity = (
    "SELECT City, "
    "AVG((julianday( HireDate) - julianday(BirthDate))/365.25) "
    "AS 'Average Age at Hire' "
    "FROM Employee "
    "GROUP BY City;"
)

# Part 3 Queries
r_v_most_expensive_bysupplier = (
    "SELECT CompanyName, ProductName "
    "FROM Product p "
    "INNER JOIN Supplier s "
    "ON s.id = p.supplierId "
    "ORDER BY UnitPrice DESC "
    "LIMIT 10;"
)

r_v_largest_category = (
    "SELECT CategoryName "
    "FROM Category c "
    "INNER JOIN Product p "
    "ON c.Id = p.CategoryId "
    "GROUP BY CategoryName "
    "ORDER BY COUNT(p.Id) DESC "
    "LIMIT 1;"
)

r_v_most_territories = (
    "SELECT emp.LastName, emp.FirstName "
    "FROM Employee AS emp "
    "INNER JOIN EmployeeTerritory et "
    "ON et.EmployeeId = emp.Id "
    "GROUP BY LastName, FirstName "
    "ORDER BY COUNT(et.TerritoryId) DESC "
    "LIMIT 1;"
)


if __name__ == '__main__':
    main()
