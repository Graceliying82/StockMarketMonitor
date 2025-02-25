from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Stock
import fetch_data

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/stocks/")
def get_stocks(db: Session = Depends(get_db)):
    return db.query(Stock).all()

@router.get("/fetch/")
def fetch_new_data():
    fetch_data.fetch_stock_data("AAPL")
    return {"message": "Data fetched"}
