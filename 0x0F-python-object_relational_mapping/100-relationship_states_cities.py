#!/usr/bin/python3
"""
    To create the State 'California'
    With the City iSan Franciscoi
    From the database hbtn_0e_100_usa.
"""

from sys import argv
from relationship_state import State
from relationship_city import Base, City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # To Create the 'MySQL' conected database.
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    # To Create tables of 'models01'
    Base.metadata.create_all(engine)

    # To Create  session of database.
    Session = sessionmaker(bind=engine)
    session = Session()

    # To Create a City object and Associate
    session.add(City(name="San Francisco", state=State(name="California")))

    session.commit()
