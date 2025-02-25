from sqlalchemy import Column, Integer, String, Numeric
from database import  Base

class Stock(Base):
    __tablename__ = 'stock'

    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String(10), index= True)
    price = Column(Numeric(10, 2))
    volume = Column(Integer)