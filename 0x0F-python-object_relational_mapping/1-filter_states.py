#!/usr/bin/python3
"""Module that list all states from the hbtn_0e_0_usa database."""
import sys
import MySQLdb

if __name__ == "__main__":
    #Get MySQL credentials from command-line arguments
    #Connecting MySQL server
    db = MySqLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    curs = db.cursor()

    #Executing the SQL query to retrieve all states sorted by id
    curs.execute("SELECT * FROM `states` ORDER BY `id`")
    [print(state) for state in curs.fetchall() if state[1][0] == "N"]
