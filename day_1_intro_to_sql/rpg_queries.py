"""
This module contains Part 1 of the assignment
Assignment - Part 1, Querying a Database
"""
import sqlite3
from query_list import QRY_TOTAL_CHARACTERS, QRY_TOTAL_SUBCLASSES
from query_list import QRY_ITEMS_WEAPONS_COUNT, QRY_TOTAL_ITEMS
from query_list import QRY_ITEMS_PER_CHARACTER
from query_list import QRY_WEAPONS_PER_CHARACTER


# Function Definitions
def connect_to_database(db_name):
    conn = sqlite3.connect(db_name)
    return conn


def execute_read(cursor, query):
    cursor.execute(query)
    return cursor.fetchall()


# Question 1: How many total Characters are there?
def get_total_characters(cursor):
    result = execute_read(cursor, QRY_TOTAL_CHARACTERS)
    return int(result[0][0])


def print_total_characters(cursor):
    total_characters = get_total_characters(cursor)
    print(f"1>There are {total_characters} characters currently.")
    pass


# Question 2: How many of each specific subclass?
def get_total_characters_by_subclass(cursor):
    return execute_read(cursor, QRY_TOTAL_SUBCLASSES)


def print_total_subclasses(cursor):
    total_subclasses = get_total_characters_by_subclass(cursor)

    for subclass in total_subclasses:
        label = subclass[0]
        count = int(subclass[1])
        if 'Clerics' in label:
            print(f"2>There are {count} Clerics currently.")
        elif 'Fighters' in label:
            print(f"2>There are {count} Fighters currently.")
        elif 'Mages' in label:
            print(f"2>There are {count} Mages currently.")
        elif 'Thieves' in label:
            print(f"2>There are {count} Thieves currently.")
        elif 'Necromancers' in label:
            print(f"2>Of the Mages, {count} are currently Necromancers.")
        else:
            print(f"2>It appears we have {count} of a mysterious class.")
        pass


# Question 3: How many total Items?
def get_total_items(cursor):
    result = execute_read(cursor, QRY_TOTAL_ITEMS)
    return int(result[0][0])


def print_total_items(cursor):
    total_items = get_total_items(cursor)
    print(f"3>There are {total_items} items carried by characters currently.")
    pass


# Question 4: How many of the Items are weapons? How many are not?
def get_count_items_weapons(cursor):
    result = execute_read(cursor, QRY_ITEMS_WEAPONS_COUNT)
    return int(result[0][0]), int(result[0][1])


def print_count_items_weapons(cursor):
    count_items, count_weapons = get_count_items_weapons(cursor)
    print(f"4>Of the total items carried {count_weapons} are weapons.")
    print(f"4>Of the total items carried {count_items} are other items.")
    pass


# Question 5: How many Items does each character have? (Return first 20 rows)
def get_items_per_character(cursor):
    return execute_read(cursor, QRY_ITEMS_PER_CHARACTER)


def print_items_per_character(cursor):
    items_per_character = get_items_per_character(cursor)

    for char in items_per_character:
        print(f'5>Character "{char[0]}" has {char[1]} item(s) in inventory.')
        pass


# Question 6: How many Weapons does each character have? (Return first 20 rows)
def get_weapons_per_character(cursor):
    return execute_read(cursor, QRY_WEAPONS_PER_CHARACTER)


def print_weapons_per_character(cursor):
    weapons_per_character = get_weapons_per_character(cursor)

    for char in weapons_per_character:
        print(f'6>Character "{char[0]}" has {char[1]} weapon(s) in inventory.')
        pass


# Question 7: On average, how many Items does each Character have?
# Question 8: On average, how many Weapons does each character have?
def print_average_itemsweapons_per_character(cursor):
    total_characters = get_total_characters(cursor)
    total_items, total_weapons = get_count_items_weapons(cursor)

    average_items = round(total_items/total_characters, 2)
    average_weapons = round(total_weapons/total_characters, 2)

    print(f"7>Characters have {average_items} items on average.")
    print(f"8>Characters have {average_weapons} weapons on average.")


# Print the full set of answers
def print_results():
    db_name = 'rpg_db.sqlite3'
    conn = connect_to_database(db_name)
    cursor = conn.cursor()

    # Print Function Calls:
    print_total_characters(cursor)
    print_total_subclasses(cursor)
    print_total_items(cursor)
    print_count_items_weapons(cursor)
    print_items_per_character(cursor)
    print_weapons_per_character(cursor)
    print_average_itemsweapons_per_character(cursor)


# Program Execution
if __name__ == '__main__':
    print_results()
