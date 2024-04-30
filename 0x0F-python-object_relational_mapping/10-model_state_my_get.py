#!/usr/bin/python3
"""Module that searches for a states from a MySQL database using SQLAlchemy"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    #Create the SqlAlchemy engine using the available MySQL credentials
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                            .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                            pool_pre_ping = True)

    #Create a session factory
    session = sessionmaker(bind = engine)

    #Create a session object
    session = session()

    #Search for a particular state in the database
    found = False
    for state in session.query(State):
        if state.name == sys.argv[4]:
            print("{}".format(state.id))
            found = True
            break

    #Printa a message if found is still false
    if found is False:
        print("Not found")
