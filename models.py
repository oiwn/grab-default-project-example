# -*- coding: utf-8 -*-
"""
Models for default project
"""
import datetime

from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (Column, Integer, Text, String, ForeignKey,
                        DateTime, PickleType, Table)

Base = declarative_base()

    
class Item(Base):
    __tablename__ = 'item'

    sqlite_autoincrement = True
    id = Column(Integer, primary_key=True)

    title = Column(String(160))
    author = Column(String(160))
    description = Column(String(255))
    url = Column(String(160))

    last_update = Column(DateTime, default=datetime.datetime.now)

