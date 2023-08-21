from sqlalchemy import Column, Integer,Float, String, Date
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Patient(Base):
    __tablename__ = "patient"
    
    id = Column(Integer, primary_key=True)
    patient_first_name = Column(String)
    patient_last_name = Column(String)
    patient_phone = Column(String)
    patient_next_appointment = Column(Date)
    patient_balance = Column(Float)