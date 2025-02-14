""" exercise_02_01:
    Skapa en databas med en tabell som innehåller kolumnerna id, namn och highscore
    Välj passande datatyper för varje kolumn
"""

from sqlite3 import connect
from sqlite3 import IntegrityError
from sqlite3 import InterfaceError
from sqlite3 import InternalError
from sqlite3 import OperationalError

import inspect
import sys

# Globals
DATA_BASE = "scores.db"
SQLITE3_ERRORS = (IntegrityError,
                  InterfaceError,
                  InternalError,
                  OperationalError)
USERS = {'user1':[1, 'mier', 0],
         'user2':[2, 'meri04', 0],
         'user3':[3, 'mikeri', 0]}
USERS_TABLE = "users"


# Some useful utility functions
def debug_msg(*args, end="\n"):
    """Utility function. Prints debugging info on stderr"""
    args_str = [str(x) for x in args]
    msg = ' '.join(args_str)
    caller = inspect.stack()[1].function
    if caller == "<module>":
        caller = "main"
    sys.stderr.write(f"({caller}) {msg}{end}")


def err_msg(*args, end="\n"):
    """Utility function. Prints a message on stderr"""
    args_str = [str(x) for x in args]
    msg = ' '.join(args_str)
    caller = inspect.stack()[1].function
    if caller == "<module>":
        caller = "main"
    sys.stderr.write(f"({caller}) {msg}{end}")


def sys_msg(*args, end="\n"):
    """Utility function. Prints a message on stdout"""
    args_str = [str(x) for x in args]
    msg = ' '.join(args_str)
    caller = inspect.stack()[1].function
    if caller == "<module>":
        caller = "main"
    sys.stdout.write(f"({caller}) {msg}{end}")


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
                                highscore integer);"""
            db_connection.execute(create_code)
            sys_msg("done")
    except SQLITE3_ERRORS as exception:
        err_msg(f"sqlite3 error: {exception}")
        raise SystemExit(1) from exception


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
        err_msg(f"sqlite3 error: {exception}")
        raise SystemExit(1) from exception

def list_users():
    """ Retrieve and print user data"""
    try:
        with connect(DATA_BASE) as db_connection:
            sys_msg("Retrieving user data...")
            select_data = db_connection.execute("select * from users;")
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
        raise SystemExit(1) from exception


def update_user_score(user: str, score: int) -> None:
    """Update the 'users' table"""
    try:
        with connect(DATA_BASE) as db_connection:
            sys_msg(f"Updating user {user}'s score to {score}")
            update_code = f"""update {USERS_TABLE}
                set highscore = {score}
                where user = '{user}';"""
            db_connection.execute(update_code)
            sys_msg("done")
    except SQLITE3_ERRORS as exception:
        err_msg(f"sqlite3 error: {exception}")
        raise SystemExit(1) from exception



def main():
    """main"""
    initialise_users_table()
    insert_users()
    update_user_score(user='mier', score=10)
    list_users()


if __name__ == '__main__':
    main()
