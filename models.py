from sqlalchemy import Column, DateTime, Integer, String, func
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Patient(Base):
    __tablename__ = "patient"

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    next_appointment = Column(String)
    created_date = Column(DateTime, server_default=func.current_date())
    last_updated = Column(DateTime, onupdate=func.current_date())

    def __repr__(self):
        return (
            f"\n<Patient "
            + f"id:{self.id}, "
            + f"first name:{self.first_name}, "
            + f"last name:{self.last_name}, "
            + f"phone:{self.phone}, "
            + f"next appointment:{self.next_appointment}, "
            + f"created on:{self.created_date}, "
            + f"last updated on:{self.last_updated}, "
            + " >"
        )

class Doctor(Base):
    __tablename__ = "doctor"
    
    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    specialty = Column(String)
    
    def __repr__(self):
        return (
            f"\n<Doctor "
            + f"id:{self.id}, "
            + f"first name:{self.first_name}, "
            + f"last name:{self.last_name}, "
            + f"specialty:{self.specialty}, "
            + " >"
        )
    