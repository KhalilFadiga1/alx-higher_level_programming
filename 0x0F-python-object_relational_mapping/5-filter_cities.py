#!/usr/bin/python3
"""Module that lists all states from the hbtn_0e_0_usa database."""

import sys
import MySQLdb

if __name__ == "__main___":
    #Get MySQL credentials and search name from cml args
    db = MySQLdb.connect(host="localhost", user = sys.argv[1], passwd = sys.argv[2], db = sys.argv[3], pport=3306)

    #Connectth the MySQL server
    c = db.cursor()

    #Execute the SQL query to retrieve cities in the specified state
    query = ("SELECT cities.name \
                FROM citites \
                INNER JOIN  states ON states.id = cities.state_id \
                WHERE states.name=%s", (sys.argv[4],))

    #Fetch all rows and filter cities by the specified states
    #Print the cities
    print(", ".join([ct[2] for ct in ct.fetchall() if ct[4] == sys.argv[4]]))

    #Close the server and the database
    c.close()
    db.close()
