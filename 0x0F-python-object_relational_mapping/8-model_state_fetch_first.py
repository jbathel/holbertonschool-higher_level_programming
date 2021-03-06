#!/usr/bin/python3
# Script that lists all states from the database hbtn_0e_0_usa
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import sys
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(engine)
    session = Session()
    state = session.query(State).first()
    if state:
        print("{}: {}".format(state.id, state.name))
    else:
        print('Nothing')
    session.close()
