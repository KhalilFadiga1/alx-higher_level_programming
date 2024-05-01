#!/usr/bin/python3
"""
Module that retrieves and prints all cities along with their states from MySQL database
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City

if __name__ == "__main__":

    #Get the CML arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    mysql_name = sys.argv[3]

    #Create the engine to connect to the server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                        .format(mysql_username, mysql_password, database_name))

    #Create a configured session class
    session = sessionmaker(bind = engine)

    #Create a session
    session = session()

    #Query all city objects and their respective state objects
    cities = session.query(City).join(State).order_by(city.id)

    #Print the outcome
    for city in cities:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))

    #close the session
    session.close()
