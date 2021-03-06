#!/usr/bin/python3
# Script that lists all states from the database hbtn_0e_0_usa
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sys import argv
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(engine)
    session = Session()
    state = State(name='Louisiana')
    session.add(state)
    session.commit()
    print('{}'.format(state.id))
    session.close()
