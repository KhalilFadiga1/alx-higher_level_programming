#!/usr/bin/python3
"""Module that lists all states from the hbtn_0e_0_usa database."""
import sys
import MySQLdb

if __name__ == "__main__":
    import MySQLdb
    import sys

    #Get the cml args
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    #Connecting to the MySQL server
    db = MySQLdb.connect(host = 'localhost', port = 3306, user = mysql_username, db = databse_name)
    
    #Create a cursor obj to execute queries
    cursor = db.cursor()

    #Prepare the SQL query with placeholders
    sql_query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"

    #Execute the query with the state name as a parameter
    cursor.execute(sql_query, (state_name,))

    #Fetch all the rows returned by the query
     rows = cursor.fetchall()

     #Display the outcome
     for row in rows:
         print(row)
