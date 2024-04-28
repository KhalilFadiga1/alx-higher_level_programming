#!/usr/bin/python3
"""Module that lists all states from the hbtn_0e_0_usa database."""

import sys
import MySQLdb

if __name__ == "__main___":
    #Get MySQL credentials and search name from cml args
    db = MySQLdb.connect(user = sys.argv[1], passwd = sys.argv[2], db = sys.argv[3])

    #Connectth the MySQL server
    c = db.cursor()

    #Execute the SQL query to retrieve cities in the specified state
    query = ("SELECT * \
                FROM citites as `c` \
                INNER JOIN  `states` as `s` \
                    ON `c`, `state_id` = `s`, `id` \
                ORDER BY `c`, `id`")

    #Fetch all rows and filter cities by the specified states
    #Print the cities
    print(", ".join([ct[2] for ct in ct.fetchall() if ct[4] == sys.argv[4]]))
