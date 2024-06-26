#!/usr/bin/python3
"""Module that adds a city and its state to a MySQL database using SQLAlchemy"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import Base, City

if __name__ == "__main__":
    #Create the SqlAlchemy engine using the available MySQL credentials
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                            .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                            pool_pre_ping = True)

    #Create the database tables based on the defined models
    Base.metadata.create_all(engine)

    #Create a session factory
    session = sessionmaker(bind = engine)

    #Create a session object
    session = session()

    #Create a new City and its state and adds to the session
    session.add(City(name="San Francisco", state = State(name = "California")))

    #Commit the session to persist the changes in the database
    session.commit()
