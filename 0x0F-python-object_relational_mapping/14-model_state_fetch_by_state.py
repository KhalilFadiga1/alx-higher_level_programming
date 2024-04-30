#!/usr/bin/python3
"""Module that retrieves and prints lists of cities with their respective states from a MySQL database using SQLAlchemy"""
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

    #Retrieve cities and their associated states from the database
    # by joining the City and state tables based on the state_id
    #Ordering the results by city ID
    for state in session.query(City, State) \
                        .filter(City.state_id == State.id) \
                        .order_by(City.id):
        # Print the City and State information
        print("{}: ({}) {}".format(state.name, city.id, city.name))
