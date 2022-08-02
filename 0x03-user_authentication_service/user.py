#!/usr/bin/env python3
"""
creating a datebase model and a table
"""
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
engine = create_engine('mysql:///:Info:', echo=True)

Base = declarative_base()


class User(Base):
    """
    model named User for a database table named users
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    session_id = Column(String)
    reset_token = Column(String)
    