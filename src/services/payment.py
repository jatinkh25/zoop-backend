from sqlalchemy.orm import Session
from fastapi import HTTPException
from src.models.payment import Payment
from src.schemas.payment import PaymentCreate, PaymentUpdate

class PaymentService:
    @staticmethod
    def get_payments(db: Session, skip: int = 0, limit: int = 100):
        return db.query(Payment).offset(skip).limit(limit).all()

    @staticmethod
    def get_payment(db: Session, payment_id: int):
        payment = db.query(Payment).filter(Payment.id == payment_id).first()
        if not payment:
            raise HTTPException(status_code=404, detail="Payment not found")
        return payment

    @staticmethod
    def create_payment(db: Session, payment: PaymentCreate):
        db_payment = Payment(**payment.model_dump())
        db.add(db_payment)
        db.commit()
        db.refresh(db_payment)
        return db_payment

    @staticmethod
    def update_payment(db: Session, payment_id: int, payment: PaymentUpdate):
        db_payment = PaymentService.get_payment(db, payment_id)
        update_data = payment.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_payment, field, value)
        db.commit()
        db.refresh(db_payment)
        return db_payment

    @staticmethod
    def delete_payment(db: Session, payment_id: int):
        db_payment = PaymentService.get_payment(db, payment_id)
        db.delete(db_payment)
        db.commit()
        return db_payment