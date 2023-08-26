from sqlalchemy import Column, DateTime, Integer, String, func
from datetime import datetime
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Patient(Base):
    __tablename__ = "patient"

    id = Column(Integer, primary_key=True)
    patient_first_name = Column(String, nullable=False)
    patient_last_name = Column(String, nullable=False)
    patient_phone = Column(String, nullable=False)
    patient_next_appointment = Column(String(datetime) )
    patient_created_date = Column(DateTime, server_default=func.current_date())
    patient_last_updated = Column(DateTime, onupdate=func.current_date())

    def __repr__(self):
        return (
            f"\n<Patient "
            + f"id:{self.id}, "
            + f"first name:{self.patient_first_name}, "
            + f"last name:{self.patient_last_name}, "
            + f"phone:{self.patient_phone}, "
            + f"next appointment:{self.patient_next_appointment}, "
            + f"created on:{self.patient_created_date}, "
            + f"last updated on:{self.patient_last_updated}, "
            + " >"
        )
