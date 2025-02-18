""" exercise_02_01:
    Skapa en databas med en tabell som innehåller kolumnerna id, namn och highscore
    Välj passande datatyper för varje kolumn
"""

from databasefunctions import *
from utils import debug_msg, err_msg, sys_msg


def main():
    """main"""
    try:
        initialise_users_table()
        insert_users()
        list_users()
        update_user_score(name='Kalle', increment=20)
        # update_user_score(name='mier', increment=20)
        list_users()
        update_user_name(name="Kalle", new_name="Karl")
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
    except TypeError as exception:
        err_msg(f"TypeError: {exception}")

if __name__ == '__main__':
    main()
