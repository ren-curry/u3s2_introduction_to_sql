"""
This module contains Part 1 of the assignment
Assignment - Part 1, Transfering Data from SQLite3 to MongoDB

Question: How was working with MongoDB different from working with PostgreSQL?
    What was easier, and what was harder?

Answer:
MongoDB works on the concept of documents and loses the relationships
common to SQL DBs. This means that I am not entering records into
tables but instead I am creating and editing documents.
I find SQL much easier, something in the way I personally think of Data
fits into RDBMSs better than Document based DBMSs like MongoDB. It could
be that I have long worked with SQL and not NoSQL solutions, but I also
find learning how to work with MongoDB to be more challenging to learn.
"""
import configparser
import sqlite3
import pymongo


config = configparser.ConfigParser()
config.read('config.ini')
mdb_config = config['MongoDB']

DBNAME = mdb_config['DBNAME']
PASSWORD = mdb_config['PASSWORD']


def connect_mongo_db(password=PASSWORD, dbname=DBNAME):
    connection_string = (
        "mongodb+srv://lambdaschool_user:{}@cluster0.ycwfc.mongodb.net/"
        "{}?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE"
        )
    mongo_conn_str = connection_string.format(password, dbname)
    client = pymongo.MongoClient(mongo_conn_str)
    return client


def connect_sl_db(dbname="rpg_db.sqlite3"):
    sl_conn = sqlite3.connect(dbname)
    sl_curs = sl_conn.cursor()
    return sl_conn, sl_curs


def execute_read_query(cursor, query):
    cursor.execute(query)
    return cursor.fetchall()


def get_character_inventory(cursor, query, character_id):
    final_result = []

    query = query.format(character_id)
    response = execute_read_query(cursor, query)
    if(len(response) > 0):
        for record in response:
            final_result.append(record[0])

    return final_result


def mongo_show_all(db):
    all_docs = list(db.find())
    return all_docs


def create_mongo_character(sl_cursor, mongo_db):
    character_columns = ['name', 'level', 'exp', 'hp', 'strength',
                         'intelligence', 'dexterity', 'wisdom']
    sl_query = r_v_select_all.format('charactercreator_character')

    characters = execute_read_query(sl_cursor, sl_query)

    for character in characters:
        character_toadd = tuple(zip(character_columns, character[1:]))
        mongo_doc = {key: value for key, value in character_toadd}
        mongo_doc['items'] = get_character_inventory(sl_cursor,
                                                     r_v_character_items,
                                                     character[0])
        mongo_doc['weapons'] = get_character_inventory(sl_cursor,
                                                       r_v_character_weapons,
                                                       character[0])
        mongo_db.insert_one(mongo_doc)


def execution_function():
    sl_conn, sl_curs = connect_sl_db()

    mongo_client = connect_mongo_db()
    mongo_db = mongo_client['LambdaSchoolDS21']['sprint2_module3']

    create_mongo_character(sl_curs, mongo_db)
    print(mongo_show_all(mongo_db))


# SQLite Queries:
r_v_select_all = "SELECT * FROM {};"

r_v_character_items = (
    "SELECT ai.name "
    "FROM armory_item ai "
    "LEFT JOIN armory_weapon aw "
    "ON ai.item_id = aw.item_ptr_id "
    "INNER JOIN charactercreator_character_inventory ccci "
    "ON ccci.item_id = ai.item_id "
    "WHERE ccci.character_id = {} "
    "AND aw.item_ptr_id IS NULL"
)

r_v_character_weapons = (
    "SELECT ai.name "
    "FROM armory_item ai "
    "LEFT JOIN armory_weapon aw "
    "ON ai.item_id = aw.item_ptr_id "
    "INNER JOIN charactercreator_character_inventory ccci "
    "ON ccci.item_id = ai.item_id "
    "WHERE ccci.character_id = {} "
    "AND aw.item_ptr_id IS NOT NULL"
)

if __name__ == '__main__':
    execution_function()
