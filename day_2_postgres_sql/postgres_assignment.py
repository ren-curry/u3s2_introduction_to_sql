"""
This module contains Part 1 of the assignment
Assignment - Part 1, Transfering Data from SQLite3 to PostgreSQL
"""
import configparser
import sqlite3
import psycopg2

from queries import (
    r_t_exists_check,
    r_v_select_all,
    c_t_charactercreator_character,
    c_t_armory_item,
    c_t_armory_weapon,
    c_t_charactercreator_character_inventory,
    c_t_charactercreator_mage,
    c_t_charactercreator_necromancer,
    c_t_charactercreator_thief,
    c_t_charactercreator_cleric,
    c_t_charactercreator_fighter,
    c_v_charactercreator_character,
    c_v_armory_item,
    c_v_armory_weapon,
    c_v_charactercreator_character_inventory,
    c_v_charactercreator_mage,
    c_v_charactercreator_necromancer,
    c_v_charactercreator_thief,
    c_v_charactercreator_cleric,
    c_v_charactercreator_fighter,
    )


config = configparser.ConfigParser()
config.read('config.ini')
pg_config = config['PostgreSQL']

DBNAME = pg_config['DBNAME']
USER = pg_config['USER']
PASSWORD = pg_config['PASSWORD']
HOST = pg_config['HOST']


def connect_pg_db(DBNAME=DBNAME, USER=USER, PASSWORD=PASSWORD, HOST=HOST):
    pg_conn = psycopg2.connect(dbname=DBNAME, user=USER,
                               password=PASSWORD, host=HOST)
    pg_curs = pg_conn.cursor()
    return pg_conn, pg_curs


def connect_sl_db(dbname="rpg_db.sqlite3"):
    sl_conn = sqlite3.connect(dbname)
    sl_curs = sl_conn.cursor()
    return sl_conn, sl_curs


def execute_read_query(cursor, query):
    cursor.execute(query)
    return cursor.fetchall()


def create_tables(connection, cursor):
    table_list = [
        ('charactercreator_character',
         c_t_charactercreator_character),
        ('armory_item',
         c_t_armory_item),
        ('armory_weapon',
         c_t_armory_weapon),
        ('charactercreator_character_inventory',
         c_t_charactercreator_character_inventory),
        ('charactercreator_mage',
         c_t_charactercreator_mage),
        ('charactercreator_necromancer',
         c_t_charactercreator_necromancer),
        ('charactercreator_thief',
         c_t_charactercreator_thief),
        ('charactercreator_cleric',
         c_t_charactercreator_cleric),
        ('charactercreator_fighter',
         c_t_charactercreator_fighter),
        ]
    for table in table_list:
        exists_query = r_t_exists_check.format(table[0])
        exists = execute_read_query(cursor, exists_query)[0][0]
        if(exists is not True):
            cursor.execute(table[1])
    connection.commit()


def transfer_data(sl_cursor, pg_conn, pg_cursor):
    table_list = [
        ('charactercreator_character',
         c_v_charactercreator_character),
        ('armory_item',
         c_v_armory_item),
        ('armory_weapon',
         c_v_armory_weapon),
        ('charactercreator_character_inventory',
         c_v_charactercreator_character_inventory),
        ('charactercreator_mage',
         c_v_charactercreator_mage),
        ('charactercreator_necromancer',
         c_v_charactercreator_necromancer),
        ('charactercreator_thief',
         c_v_charactercreator_thief),
        ('charactercreator_cleric',
         c_v_charactercreator_cleric),
        ('charactercreator_fighter',
         c_v_charactercreator_fighter),
        ]

    for table in table_list:
        read_query = r_v_select_all.format(table[0])
        records = execute_read_query(sl_cursor, read_query)
        for record in records:
            insert_query = table[1].format(*record)
            print(insert_query)
            pg_cursor.execute(insert_query)

    pg_conn.commit()


def execution_function():
    sl_conn, sl_curs = connect_sl_db()
    pg_conn, pg_curs = connect_pg_db()

    create_tables(pg_conn, pg_curs)
    transfer_data(sl_curs, pg_conn, pg_curs)

    sl_curs.close()
    pg_curs.close()


if __name__ == '__main__':
    execution_function()
