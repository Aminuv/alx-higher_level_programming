#!/usr/bin/python3
"""
    The class definition of a State and an instance:
        Base = Declarative_base().
"""

from sqlalchemy import Column, Integer, String, ForeignKey, null
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State

Base = declarative_base()



class City(Base):
    """
        The City class.
    """

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
