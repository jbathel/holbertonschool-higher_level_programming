#!/usr/bin/python3
# Script that lists all states from the database hbtn_0e_0_usa
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """Defines Class States"""
    __tablename__ = 'states'
    id = Column(
        Integer, primary_key=True, unique=True, autoincrement=True)
    name = Column(String(128), nullable=False)
