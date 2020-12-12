"""
List of Query strings
"""

# Read queries
r_t_exists_check = (
    "SELECT EXISTS("
    "SELECT * "
    "FROM information_schema.tables "
    "WHERE table_name='{}');"
    )

r_v_select_all = "SELECT * FROM {};"

# Table Creation Queries
c_t_charactercreator_character = (
    "CREATE TABLE charactercreator_character("
    "character_id INTEGER NOT NULL, "
    "name VARCHAR(30) NOT NULL, "
    "level INTEGER NOT NULL, "
    "exp INTEGER NOT NULL, "
    "hp INTEGER NOT NULL, "
    "strength INTEGER NOT NULL, "
    "intelligence INTEGER NOT NULL, "
    "dexterity INTEGER NOT NULL, "
    "wisdom INTEGER NOT NULL"
    ");"
    )

c_t_charactercreator_character_inventory = (
    "CREATE TABLE charactercreator_character_inventory("
    "id INTEGER NOT NULL, "
    "character_id INTEGER NOT NULL, "
    "item_id INTEGER NOT NULL"
    ");"
)

c_t_armory_item = (
    "CREATE TABLE armory_item("
    "item_id INTEGER NOT NULL, "
    "name VARCHAR(30) NOT NULL, "
    "value INTEGER NOT NULL, "
    "weight INTEGER NOT NULL"
    ");"
    )

c_t_armory_weapon = (
    "CREATE TABLE armory_weapon("
    "item_ptr_id INTEGER NOT NULL, "
    "power INTEGER NOT NULL"
    ");"
    )

c_t_charactercreator_mage = (
    "CREATE TABLE charactercreator_mage("
    "character_ptr_id INTEGER NOT NULL, "
    "has_pet BOOL NOT NULL, "
    "mana INTEGER NOT NULL"
    ");"
)

c_t_charactercreator_necromancer = (
    "CREATE TABLE charactercreator_necromancer("
    "mage_ptr_id INTEGER NOT NULL, "
    "talisman_charged BOOL NOT NULL"
    ");"
)

c_t_charactercreator_thief = (
    "CREATE TABLE charactercreator_thief("
    "character_ptr_id INTEGER NOT NULL, "
    "is_sneaking BOOL NOT NULL, "
    "energy INTEGER NOT NULL"
    ");"
)

c_t_charactercreator_cleric = (
    "CREATE TABLE charactercreator_cleric("
    "character_ptr_id INTEGER NOT NULL, "
    "using_shield BOOL NOT NULL, "
    "mana INTEGER NOT NULL"
    ");"
)

c_t_charactercreator_fighter = (
    "CREATE TABLE charactercreator_fighter("
    "character_ptr_id INTEGER NOT NULL, "
    "using_shield BOOL NOT NULL, "
    "rage INTEGER NOT NULL"
    ");"
)

# Insert queries
c_v_charactercreator_character = (
    "INSERT INTO charactercreator_character "
    "(character_id, name, level, exp, hp, strength, "
    "intelligence, dexterity, wisdom) "
    "VALUES ({}, '{}', {}, {}, {}, {}, {}, {}, {});"
)

c_v_charactercreator_character_inventory = (
    "INSERT INTO charactercreator_character_inventory "
    "VALUES ({}, {}, {});"
)

c_v_armory_item = (
    "INSERT INTO armory_item "
    "VALUES ({}, '{}', {}, {});"
)

c_v_armory_weapon = (
    "INSERT INTO armory_weapon "
    "VALUES ({}, {});"
)

c_v_charactercreator_mage = (
    "INSERT INTO charactercreator_mage "
    "VALUES ({}, CAST({} AS BOOL), {});"
)

c_v_charactercreator_necromancer = (
    "INSERT INTO charactercreator_necromancer "
    "VALUES ({}, CAST({} AS BOOL));"
)

c_v_charactercreator_thief = (
    "INSERT INTO charactercreator_thief "
    "VALUES ({}, CAST({} AS BOOL), {});"
)

c_v_charactercreator_cleric = (
    "INSERT INTO charactercreator_cleric "
    "VALUES ({}, CAST({} AS BOOL), {});"
)

c_v_charactercreator_fighter = (
    "INSERT INTO charactercreator_fighter "
    "VALUES ({}, CAST({} AS BOOL), {});"
)

# Titanic Problem queries
c_ty_gender = "CREATE TYPE Gender AS ENUM ('male', 'female', 'other');"

c_ty_pclass = "CREATE TYPE Pclass AS ENUM (1, 2, 3);"

c_t_titanic = (
    "CREATE TABLE titanic ("
    "id SERIAL, "
    "survived BOOL, "
    "passenger_class Pclass, "
    "name VARCHAR(100), "
    "passenger_gender Gender, "
    "age INTEGER, "
    "siblings_spouses_aboard INTEGER, "
    "parents_children_aboard INTEGER, "
    "fare NUMERIC"
    ");"
)

c_v_titanic_data = (
    "INSERT INTO {} (survived, passenger_class, name, passenger_gender, "
    "age, siblings_spouses_aboard, parents_children_aboard, fare) "
    "VALUES (CAST({} AS BOOL), '{}', '{}', '{}', {}, {}, {}, {});"
)
