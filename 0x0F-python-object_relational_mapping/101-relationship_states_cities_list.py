#!/usr/bin/python3
"""
Module that interacts with a MySQL database using SQLAlchemy to print states and their cities
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City

if __name__ == "__main__":
    #Create the SqlAlchemy engine using the available MySQL credentials
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                            .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                            pool_pre_ping = True)

    #Create a session factory
    session = sessionmaker(bind = engine)

    #Create a session object
    session = session()

    #Retrieve states and their cities from the database and print them
    for state in session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))
