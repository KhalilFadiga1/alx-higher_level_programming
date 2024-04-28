#!/usr/bin/python3
"""Module that feinfes the states representing a state in a MySQL database"""

from sqlalchemy import Culumn, Integer, String
from sqlalchemy.ext.declarative import declarative_base

base = declarative_base()

class State(Base):
    """Represents a state for a MySQL databse.

    __tablename__ (str): The name of the MySQL table to store states.
    id (sqlalchemy. Integer): The state's id.
    name (sqlalchemy. String): The state's name.
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key = True)
    name = Column(String(120), nullable = False)
