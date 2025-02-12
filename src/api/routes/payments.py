from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from src.schemas import Payment, PaymentCreate, PaymentUpdate
from src.services import PaymentService
from src.db.base import get_db

router = APIRouter()

@router.get("/", response_model=List[Payment])
def get_payments(page_no: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return PaymentService.get_payments(db, page_no, limit)

@router.post("/", response_model=Payment)
def create_payment(payment: PaymentCreate, db: Session = Depends(get_db)):
    return PaymentService.create_payment(db, payment)

@router.get("/{payment_id}", response_model=Payment)
def get_payment(payment_id: int, db: Session = Depends(get_db)):
    return PaymentService.get_payment(db, payment_id)

@router.put("/{payment_id}", response_model=Payment)
def update_payment(payment_id: int, payment: PaymentUpdate, db: Session = Depends(get_db)):
    return PaymentService.update_payment(db, payment_id, payment)

@router.delete("/{payment_id}", response_model=Payment)
def delete_payment(payment_id: int, db: Session = Depends(get_db)):
    return PaymentService.delete_payment(db, payment_id)