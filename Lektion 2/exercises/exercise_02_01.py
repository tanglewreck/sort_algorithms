""" exercise_02_01:
    Skapa en databas med en tabell som innehåller kolumnerna id, namn och highscore
    Välj passande datatyper för varje kolumn
"""

from utils import debug_msg, err_msg, sys_msg

from sqlite3 import connect
from sqlite3 import DataError
from sqlite3 import DatabaseError
from sqlite3 import IntegrityError
from sqlite3 import InterfaceError
from sqlite3 import InternalError
from sqlite3 import OperationalError

import sys

# Globals
DATA_BASE = "highscores.db"
SQLITE3_ERRORS = (DataError,
                  DatabaseError,
                  IntegrityError,
                  InterfaceError,
                  InternalError,
                  OperationalError)


class NO_SUCH_USER_ERROR(Exception):
    pass


USERS = {'user1':[1, 'Kalle', 11],
         'user2':[2, 'Svea', 5],
         'user3':[3, 'Rune', 0]}
USER_NAMES =  [USERS[user][1] for user in USERS]
USERS_TABLE = "users"


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
                                user text not null,
                                highscore int check(highscore >= 0) );"""
                                # highscore int );"""
            db_connection.execute(create_code)
            sys_msg("done")
    except SQLITE3_ERRORS as exception:
        err_msg(f"sqlite3 error: {repr(sys.exception)}")
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
                        f"""insert into users (id, user, highscore)
                        values ({user_id}, '{user_name}', {high_score});"""
                    db_connection.execute(insert_code)
                sys_msg("done")
            except (IndexError, ValueError) as exception:
                err_msg(exception)
                raise SystemExit(1) from exception
    except SQLITE3_ERRORS as exception:
        # err_msg(f"sqlite3 error: {exception}")
        raise
        # raise SystemExit(1) from exception


def list_users():
    """ Retrieve and print user data"""
    try:
        with connect(DATA_BASE) as db_connection:
            sys_msg("Retrieving user data...")
            select_data = db_connection.execute(f"select * from footable;")
            # select_data = db_connection.execute(f"select * from {USERS_TABLE};")
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
        raise exception from exception
        # raise SystemExit(1) from exception



def update_user_score(user: str,
                      increment: int) -> None:
    """Update user highscore"""
    try:
        with connect(DATA_BASE) as db_connection:
            select_code = f"""select * from {USERS_TABLE}
                              where user = '{user}';"""
            user_data = db_connection.execute(select_code).fetchall()
            # If user exists in the database, update
            if user_data:
                sys_msg(f"Updating user {user}'s score with {increment}")
                score = user_data[0][2] + increment
                update_code = f"""update {USERS_TABLE}
                                  set highscore = {score}
                                  where user = '{user}';"""
                db_connection.execute(update_code)
                sys_msg("done")
            else:
                raise NO_SUCH_USER_ERROR(user)

    #except NO_SUCH_USER_ERROR:
    #    # print(f"Error: No such user {user}")
    #    raise NO_SUCH_USER_ERROR
    # except Exception:
    except SQLITE3_ERRORS as exception:
        err_msg(repr(sys.exception()))
        raise 
    #    err_msg(f"sqlite3 error: {exception}")
    #    raise SystemExit(1) from exception


def update_user_name(user: str, new_name: str) -> None:
    """Update username"""
    try:
        with connect(DATA_BASE) as db_connection:
            pass
    except SQLITE_ERRORS as exception:
        err_msg(repr(sys.exception()))
        raise


def main():
    """main"""
    try:
        initialise_users_table()
        insert_users()
        list_users()
        update_user_score(user='Kalle', increment=20)
        update_user_score(user='mier', increment=20)
        list_users()
    except NO_SUCH_USER_ERROR as exception:
        sys_msg(f"User does not exist: {exception}")
    except DatabaseError as exception:
        err_msg(f"DatabaseError: {exception}")
    except IntegrityError as exception:
        err_msg(f"IntegrityError: {exception}")
    except InterfaceError as exception:
        err_msg(f"InterfaceError: {exception}")
    except InternalError as exception:
        err_msg(f"InternalError: {exception}")
    except OperationalError as exception:
        err_msg(f"OperationalError: {exception}")
    #except SQLITE3_ERRORS as exception:
    #    err_msg(f"sqlite3 error: {exception}")
    #    raise SystemExit(1) from exception
    except TypeError as exception:
        err_msg(f"TypeError: {exception}")

if __name__ == '__main__':
    main()
