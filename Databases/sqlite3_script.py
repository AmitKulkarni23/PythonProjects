# Interacting with databases consist of 5 steps
# 1) Connect to the database
# 2) Create a cursor object ( pointer to access row and columns)
# 3) Write an SQL Query
# 4) Commit changes to db
# 5) Close the connection

import sqlite3

# SQL Query to create a table
create_table = "CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)"


# Creating a connection
# If no db file is present, a db will be created and
# the connection will be established
# Else, the connection will be established to an existing database


def create_table():
    conn = sqlite3.connect("lite.db")

    # Point to the cursor object
    cursor = conn.cursor()

    # Actual SQL code
    # Use execute method of the cursor

    cursor.execute(create_table)

    # Committing the changes
    conn.commit()

    # Closing the connection
    conn.close()


def insert(item, quantity, price):
    """
    Function to insert into the database
    :return:
    """

    conn = sqlite3.connect("lite.db")

    # Point to the cursor object
    cursor = conn.cursor()

    # Inserting a quantity
    cursor.execute("INSERT INTO store VALUES (?, ?, ?)", (item, quantity, price))

    # Commit
    conn.commit()

    # Close connection
    conn.close()


def show():
    """
    Function which displays all the data from the db
    :return: Returns all the data in the db
    """
    conn = sqlite3.connect("lite.db")
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
    conn = sqlite3.connect("lite.db")
    cursor = conn.cursor()

    # Query to delete particular data from db
    cursor.execute("DELETE FROM store WHERE item=?", (item, ))

    # Commit
    conn.commit()

    # Closing the connection
    conn.close()


def update(quantity, price, item):
    """
    Function to update a data field
    :return:
    """

    conn = sqlite3.connect("lite.db")
    cursor = conn.cursor()

    # Query to delete particular data from db
    cursor.execute("UPDATE STORE SET quantity=?, price=? WHERE item=?", (quantity, price, item))

    # Commit
    conn.commit()

    # Closing the connection
    conn.close()

# insert("Coffee", 10, 2)
# delete("Coffee")
update(200, 200, "Wine Glass")
print(show())
