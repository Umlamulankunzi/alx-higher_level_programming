#!/usr/bin/python3
"""prints the State object with the name passed as argument from the database
hbtn_0e_6_usa.
take 4 arguments: mysql username, mysql password, database name and state name
to search (SQL injection free)
"""
import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    obj = session.query(State).filter(State.name == (sys.argv[4],))
    try:
        print(obj[0].id)
    except IndexError:
        print("Not found")
