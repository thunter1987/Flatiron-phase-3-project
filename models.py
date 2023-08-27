from sqlalchemy import Column, DateTime, Integer, String, func, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

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
    
    doctor_id = Column(Integer, ForeignKey("doctor.id"))

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
    
    patients = relationship("Patient", backref="doctor")
    
    def __init__(self, first_name, last_name, specialty):
        self.first_name = first_name
        self.last_name = last_name
        self.specialty = specialty
    
    def __repr__(self):
        return (
            f"\n<Doctor "
            + f"id:{self.id}, "
            + f"first name:{self.first_name}, "
            + f"last name:{self.last_name}, "
            + f"specialty:{self.specialty}, "
            + " >"
        )
    