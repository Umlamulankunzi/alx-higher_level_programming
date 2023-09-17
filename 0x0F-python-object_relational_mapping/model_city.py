#!/usr/bin/python3

"""Defines a model class City"""
from sqlalchemy import Column, ForeignKey, Integer, String

from model_state import Base, State


class City(Base):
    """City class which inherits from Base

    Args:
        Base (any): parent class
    Attributes:
        id (int): column of an auto-generated, unique integer
        name (string): column of a string of 128 characters
        state_id (int): column of an integer, can't be null
                        and is a foreign key to states.id
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
