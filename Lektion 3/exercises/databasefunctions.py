"""Database functions"""

from utils import debug_msg, err_msg, sys_msg

from sqlite3 import connect
from sqlite3 import DataError
from sqlite3 import DatabaseError
from sqlite3 import IntegrityError
from sqlite3 import InterfaceError
from sqlite3 import InternalError
from sqlite3 import OperationalError

import sys

__ALL__ = [
    "SQLITE3_ERRORS",
    "initialise_tables",
    "insert_users",
    "list_users",
    "update_user_score",
    "update_user_name"
]

# Globals
DATA_BASE = "highscores.db"
SQLITE3_ERRORS = (DataError,
                  DatabaseError,
                  IntegrityError,
                  InterfaceError,
                  InternalError,
                  OperationalError)


# Table definitions
GAME_TABLE = "game"
GAME_TABLE_COLUMS = {"value": "text UNIQUE"}
GAME_TABLE_VALUES = ("sten", "sax", "påse")
HIGHSCORE_TABLE = "highscores"
HIGHSCORE_TABLE_COLUMS = {
    "id": "INT PRIMARY KEY",
    "name": "TEXT UNIQUE",
    "highscore": "INT CHECK(highscore >= 0)"
}

# Users dict, used to insert test data
USERS = {'user1':[1, 'Kalle', 11],
         'user2':[2, 'Svea', 5],
         'user3':[3, 'Rune', 0]}
USER_NAMES =  [USERS[user][1] for user in USERS]


class NO_SUCH_USER_ERROR(Exception):
    pass


def initialise_tables() -> None:
    """Create tables from scratch, 
    dropping them if it already exist."""
    try:
        with connect(DATA_BASE) as db_connection:
            sys_msg(f"Initialising table {HIGHSCORE_TABLE}...")
            # Drop the table
            db_connection.execute(f"DROP TABLE IF EXISTS {HIGHSCORE_TABLE};")
            # Create the table (again)
            create_code = f"""CREATE TABLE IF NOT EXISTS {HIGHSCORE_TABLE}(
                                id INTEGER PRIMARY KEY,
                                name TEXT NOT NULL,
                                highscore INT CHECK(highscore >= 0) ) STRICT;"""
            db_connection.execute(create_code)
            sys_msg("done")

            sys_msg(f"Initialising table {GAME_TABLE}...")
            db_connection.execute(f"DROP TABLE IF EXISTS {GAME_TABLE}")
            create_code = f"""CREATE TABLE IF NOT EXISTS {GAME_TABLE}(
                              value TEXT NOT NULL UNIQUE);"""
            db_connection.execute(create_code)
            sys_msg("done")
    except SQLITE3_ERRORS as exception:
        err_msg(f"sqlite3 error: {repr(sys.exception)}")
        raise


def populate_game_table() -> None:
    """Insert values into the game table ('sten', 'sax', 'påse')"""
    try:
        with connect(DATA_BASE) as db_connection:
            sys_msg(f"Populating game table...")
            for value in GAME_TABLE_VALUES:
                db_connection.execute(f"""INSERT INTO {GAME_TABLE}
                    (value) VALUES('{value}');""")
            sys_msg("done")
    except SQLITE3_ERRORS as exception:
        err_msg(f"sqlite3 error: {repr(sys.exception)}")
        raise


def get_random_value() -> None:
    """Retrieve a random value from the game table"""
    try:
        with connect(DATA_BASE) as db_connection:
            sys_msg(f"Retrieving random value from the game table...")
            random_value = db_connection.execute(f"""SELECT value FROM {GAME_TABLE}
                                            ORDER BY RANDOM() LIMIT 1;""").fetchall()[0][0]
            sys_msg("done")
            return random_value
    except SQLITE3_ERRORS as exception:
        err_msg(f"sqlite3 error: {repr(sys.exception)}")
        raise


def insert_users():
    """Insert users into the 'users' table"""
    try:
        # Connect to the database and insert users
        with connect(DATA_BASE) as db_connection:
            try:
                sys_msg(f"Inserting user-data into table '{HIGHSCORE_TABLE}'...")
                for item in USERS.items():
                    (_, user_data) = item
                    (user_id, user_name, high_score) = user_data
                    insert_code = \
                        f"""insert into users (id, name, highscore)
                        values ({user_id}, '{user_name}', {high_score});"""
                    db_connection.execute(insert_code)
                sys_msg("done")
            except (IndexError, ValueError) as exception:
                err_msg(exception)
                raise SystemExit(1) from exception
    except SQLITE3_ERRORS as exception:
        err_msg(f"sqlite3 error: {exception}")
        raise


def list_users():
    """ Retrieve and print user data"""
    try:
        with connect(DATA_BASE) as db_connection:
            sys_msg("Retrieving user data...")
            select_data = db_connection.execute(f"select * from {HIGHSCORE_TABLE};")
            user_data = select_data.fetchall()
            try:
                for user in user_data:
                    (user_id, user_name, high_score) = user
                    print(f"\tid: {user_id}, "
                        f"username: {user_name}, "
                        f"highscore: {high_score}")
            except (IndexError, ValueError) as exception:
                err_msg(exception)
                raise SystemExit(1) from exception
            sys_msg("done")
    except SQLITE3_ERRORS as exception:
        err_msg(f"sqlite3 error: {exception}")
        raise 


def update_user_score(name: str,
                      increment: int) -> None:
    """Update user highscore"""
    try:
        with connect(DATA_BASE) as db_connection:
            select_code = f"""select * from {HIGHSCORE_TABLE}
                              where name = '{name}';"""
            user_data = db_connection.execute(select_code).fetchall()
            # If user exists in the database, update
            if user_data:
                sys_msg(f"Updating user {name}'s score by {increment}")
                score = user_data[0][2] + increment
                update_code = f"""update {HIGHSCORE_TABLE}
                                  set highscore = {score}
                                  where name = '{name}';"""
                db_connection.execute(update_code)
                sys_msg("done")
            else:
                raise NO_SUCH_USER_ERROR(name)

    except SQLITE3_ERRORS as exception:
        err_msg(repr(sys.exception()))
        raise 


def update_user_name(name: str, new_name: str) -> None:
    """Update username"""
    try:
        with connect(DATA_BASE) as db_connection:
            select_code = f"""select * from {HIGHSCORE_TABLE}
                              where name = '{name}';"""
            user_data = db_connection.execute(select_code).fetchall()
            # If user exists in the database, update
            if user_data:
                sys_msg(f"Updating user {name}'s name to {new_name}")
                update_code = f"""update {HIGHSCORE_TABLE}
                                  set name = '{new_name}'
                                  where name = '{name}';"""
                db_connection.execute(update_code)
                sys_msg("done")
            else:
                raise NO_SUCH_USER_ERROR(user)

    except SQLITE3_ERRORS as exception:
        err_msg(repr(sys.exception()))
        raise 


