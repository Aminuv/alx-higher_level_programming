#!/usr/bin/python3

"""
    The Lists all States and corresponding Cities
    in the database 'hbtn_0e_101_usa'.
"""

import sys
from relationship_state import State
from relationship_city import Cityi
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # To Create The 'SQLAlchemy'.
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # To Create a session 'factory'
    Session = sessionmaker(bind=engine)

    # To Create new session obj.
    session = Session()

    # The print them along with their 'Cities'.
    for state in session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))
