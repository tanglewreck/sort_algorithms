"""Database functions"""

__ALL__ = [
    "SQLITE3_ERRORS",
    "initialise_users_table",
    "insert_users",
    "list_users",
    "update_user_score",
    "update_user_name"
]

import sys
from sqlite3 import connect
from sqlite3 import DataError
from sqlite3 import DatabaseError
from sqlite3 import IntegrityError
from sqlite3 import InterfaceError
from sqlite3 import InternalError
from sqlite3 import OperationalError
from utils import err_msg, sys_msg

# Globals
DATA_BASE = "highscores.db"
SQLITE3_ERRORS = (DataError,
                  DatabaseError,
                  IntegrityError,
                  InterfaceError,
                  InternalError,
                  OperationalError)


class NoSuchUserError(Exception):
    """No such user-error, used when a user
    cannot be found in the database"""


USERS = {'user1': [1, 'Kalle', 11],
         'user2': [2, 'Svea', 5],
         'user3': [3, 'Rune', 0]}
USERS_TABLE = "users"
# USER_NAMES = [USERS[user][1] for user in USERS]


def initialise_users_table():
    """Create the 'users' table from scratch,
    dropping the table if it already exists."""
    try:
        with connect(DATA_BASE) as db_connection:
            sys_msg(f"Initialising table {USERS_TABLE}...")
            # Drop the table
            db_connection.execute("drop table if exists users;")
            # Create the table (again)
            create_code = f"""create table if not exists {USERS_TABLE}(
                              id integer primary key,
                              name text not null,
                              highscore int check(highscore >= 0) ) strict;"""
            db_connection.execute(create_code)
            sys_msg("done")
    except SQLITE3_ERRORS:
        err_msg(repr(sys.exception))
        raise


def insert_users():
    """Insert users into the 'users' table"""
    try:
        # Connect to the database and insert users
        with connect(DATA_BASE) as db_connection:
            try:
                sys_msg(f"Inserting user-data into table '{USERS_TABLE}'...")
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
    except SQLITE3_ERRORS:
        err_msg(repr(sys.exception))
        raise


def list_users():
    """ Retrieve and print user data"""
    try:
        with connect(DATA_BASE) as db_connection:
            sys_msg("Retrieving user data...")
            select_data = db_connection.execute(
                f"select * from {USERS_TABLE};"
            )
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
    except SQLITE3_ERRORS:
        err_msg(repr(sys.exception))
        raise


def update_user_score(name: str,
                      increment: int) -> None:
    """Update user highscore"""
    try:
        with connect(DATA_BASE) as db_connection:
            select_code = f"""select * from {USERS_TABLE}
                              where name = '{name}';"""
            user_data = db_connection.execute(select_code).fetchall()
            # If user exists in the database, update
            if user_data:
                sys_msg(f"Updating user {name}'s score by {increment}")
                score = user_data[0][2] + increment
                update_code = f"""update {USERS_TABLE}
                                  set highscore = {score}
                                  where name = '{name}';"""
                db_connection.execute(update_code)
                sys_msg("done")
            else:
                raise NoSuchUserError(name)

    except SQLITE3_ERRORS:
        err_msg(repr(sys.exception()))
        raise


def update_user_name(name: str, new_name: str) -> None:
    """Update username"""
    try:
        with connect(DATA_BASE) as db_connection:
            select_code = f"""select * from {USERS_TABLE}
                              where name = '{name}';"""
            user_data = db_connection.execute(select_code).fetchall()
            # If user exists in the database, update
            if user_data:
                sys_msg(f"Updating user {name}'s name to {new_name}")
                update_code = f"""update {USERS_TABLE}
                                  set name = '{new_name}'
                                  where name = '{name}';"""
                db_connection.execute(update_code)
                sys_msg("done")
            else:
                raise NoSuchUserError(name)

    except SQLITE3_ERRORS:
        err_msg(repr(sys.exception()))
        raise
