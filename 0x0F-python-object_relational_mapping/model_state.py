#!/usr/bin/python3
"""
Defines State class and
Base class which is an instance of declarative_base()
"""
from sqlalchemy import Column, Integer, MetaData, String
from sqlalchemy.ext.declarative import declarative_base

mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)


class State(Base):
    """State class which inherits from Base

    Args:
        Base (any): parent class

    Attributes:
        id (int): column of an auto-generated, unique integer
        name (string): column of a string of 128 characters
    """
    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
