import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def select_star(conn, sql_select_star):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param sql_select_star: a SELECT statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(sql_select_star)
        for row in c.fetchall():
            print(row)
    except Error as e:
        print(e)


def main():
    database = "db/penguins.db"

    sql_select_star = """ select * from little_penguins; """

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create projects table
        select_star(conn, sql_select_star)

    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()
