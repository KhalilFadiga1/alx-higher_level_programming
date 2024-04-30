#!/usr/bin/python3
"""Module that retrieves and prints state with letter a from a MySQL database using SQLAlchemy"""
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

    #Retrieve state with letter 'a' from the database, then print its ID and name
    for state in session.query(State).order_by(State.id):
        if "a" in state.name:
            print("{}: {}".format(state.id, state.name))
