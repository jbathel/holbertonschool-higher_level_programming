#!/usr/bin/python3
# Script that lists all states from the database hbtn_0e_0_usa
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import sys
from model_city import Base, City


if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(engine)
    session = Session()
    for cities in session.query(City).order_by(City.id).all():
        print("{}: {}".format(cities.id, cities.name))
    session.close()
