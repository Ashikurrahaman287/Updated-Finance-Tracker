from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True)
    type = Column(String)
    amount = Column(Float)
    category = Column(String)
    date = Column(DateTime, default=func.now())

class Budget(Base):
    __tablename__ = 'budgets'

    category = Column(String, primary_key=True)
    amount = Column(Float)
