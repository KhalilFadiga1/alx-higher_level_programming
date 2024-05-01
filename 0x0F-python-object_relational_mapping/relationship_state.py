#!/usr/bin/python3
"""Module that defines the state model representing a state in a MySQL database"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from relationship_city import Base, City

#Create a base class for the declarative models
Base = declarative_base()


class State(Base):
    """Represents a state for a MySQL databse.

    Attributes:
        __tablename__ (str): The name of the MySQL table to store states.
        id (sqlalchemy. Integer): The state's id.
        name (sqlalchemy. String): The state's name.
        cities (sqlalchemy.orm.relationship): The state_city relationship.
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    #Defines the relationship between State and City models
    cities = relationship("city", backref = "state", cascade = "all, delete")
