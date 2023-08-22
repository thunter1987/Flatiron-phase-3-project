from DateTime import DateTime
from sqlalchemy import Column, Integer, String, func
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Patient(Base):
    __tablename__ = "patient"
    
    id = Column(Integer, primary_key=True, nullable=False)
    patient_first_name = Column(String, nullable=False)
    patient_last_name = Column(String, nullable=False)
    patient_phone = Column(String, nullable=False)
    patient_next_appointment = Column(DateTime)
    patient_created_date = Column(DateTime, server_default=func.current_timestamp())
    patient_last_updated = Column(DateTime, onupdate=func.now())