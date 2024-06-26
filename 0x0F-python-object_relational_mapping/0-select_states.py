#!/usr/bin/python3
"""Module that lists all the states from MySQL database"""
import sys
import MySQLdb

def list_states(username, password, database):
    """Connecting to MySQL server"""
    db = MySQLdb.connect(host = 'localhost', port = 3306, user = username, passwd = password, db = database)
    cursor = db.cursor()

    #Executing the SQL query to fetch all states
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    #Fetch all rows from query result
    rows = cursor.fetchall()

    #Print the results
    for row in rows:
        print(row)

    #Close the connection to the database
    db.close()

#Example usage
if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_states(username, password, database)
