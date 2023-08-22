from sqlalchemy import Column, Date, DateTime, Integer, String, func
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Patient(Base):
    __tablename__ = "patient"
    
    id = Column(Integer, primary_key=True, nullable=False)
    patient_first_name = Column(String, nullable=False)
    patient_last_name = Column(String, nullable=False)
    patient_phone = Column(String, nullable=False)
    patient_next_appointment = Column(DateTime, nullable = True)
    patient_created_date = Column(Date, server_default=func.current_date())
    patient_last_updated = Column(Date, onupdate=func.current_date())
    