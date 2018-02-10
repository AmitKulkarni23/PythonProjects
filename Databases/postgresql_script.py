# Interacting with databases consist of 5 steps
# 1) Connect to the database
# 2) Create a cursor object ( pointer to access row and columns)
# 3) Write an SQL Query
# 4) Commit changes to db
# 5) Close the connection

import psycopg2

# SQL Query to create a table
create_table_string = "CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)"


# Creating a connection
# If no db file is present, a db will be created and
# the connection will be established
# Else, the connection will be established to an existing database


def create_table():
    # Need to pass the PostgreSQL dbname, password and port number
    conn = psycopg2.connect("dbname='database1' user='postgres' password='postgres23#' host='localhost' port='5432'")

    # Point to the cursor object
    cursor = conn.cursor()

    # Actual SQL code
    # Use execute method of the cursor

    cursor.execute(create_table_string)

    # Committing the changes
    conn.commit()

    # Closing the connection
    conn.close()


def insert(item, quantity, price):
    """
    Function to insert into the database
    :return:
    """

    # Need to pass the PostgreSQL dbname, password and port number
    conn = psycopg2.connect("dbname='database1' user='postgres' password='postgres23#' host='localhost' port='5432'")

    # Point to the cursor object
    cursor = conn.cursor()

    # Inserting a quantity
    cursor.execute("INSERT INTO store VALUES (%s, %s, %s)", (item, quantity, price))

    # Commit
    conn.commit()

    # Close connection
    conn.close()


def show():
    """
    Function which displays all the data from the db
    :return: Returns all the data in the db
    """
    # Need to pass the PostgreSQL dbname, password and port number
    conn = psycopg2.connect("dbname='database1' user='postgres' password='postgres23#' host='localhost' port='5432'")

    cursor = conn.cursor()

    # Query to display all records from the db
    cursor.execute("SELECT * from store")

    # Fetch this data
    rows = cursor.fetchall()

    conn.close()

    return rows


def delete(item):
    """
    Function to delete data from the db
    :return:
    """
    # Need to pass the PostgreSQL dbname, password and port number
    conn = psycopg2.connect("dbname='database1' user='postgres' password='postgres23#' host='localhost' port='5432'")

    cursor = conn.cursor()

    # Query to delete particular data from db
    cursor.execute("DELETE FROM store WHERE item=%s", (item, ))

    # Commit
    conn.commit()

    # Closing the connection
    conn.close()


def update(quantity, price, item):
    """
    Function to update a data field
    :return:
    """

    # Need to pass the PostgreSQL dbname, password and port number
    conn = psycopg2.connect("dbname='database1' user='postgres' password='postgres23#' host='localhost' port='5432'")

    cursor = conn.cursor()

    # Query to delete particular data from db
    cursor.execute("UPDATE STORE SET quantity=%s, price=%s WHERE item=%s", (quantity, price, item))

    # Commit
    conn.commit()

    # Closing the connection
    conn.close()

# insert("Coffee", 10, 2)
# delete("Coffee")
# update(200, 200, "Wine Glass")
# print(show())
# create_table()
insert("Orange", 100, 100)
update(0, 0, "Orange")

# delete("Orange")
print(show())