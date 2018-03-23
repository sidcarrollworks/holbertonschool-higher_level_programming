#!/usr/bin/python3
"""mode for city"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import State Base


class City(Base):
    """ city class """
    __tablename__ = 'cities'
    id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id), nullable=False)
