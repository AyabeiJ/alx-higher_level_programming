#!/usr/bin/python3
"""
This script changes the name of a State object from the database hbtn_0e_6_usa.
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    """
    Connect to the MySQL server and change the name of a State object.
    """
    username = argv[1]
    password = argv[2]
    database = argv[3]

    # Create the engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(username, password, database),
                           pool_pre_ping=True)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Retrieve the State object with id = 2
    state = session.query(State).filter_by(id=2).first()

    if state is not None:
        # Change the name of the State object
        state.name = "New Mexico"
        session.commit()
