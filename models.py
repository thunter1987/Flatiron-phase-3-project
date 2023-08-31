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
        
        
        #########NEW CODE##########
    

'''

from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from .helpers import validate_date, validate_phone_number, validate_mm_dd_yyyy

Base = declarative_base()

class Patient(Base):
    __tablename__ = 'patients'
    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    phone_number = Column(String, validate=validate_phone_number)
    next_appointment = Column(String, validate=validate_date)
    created_date = Column(String, validate=validate_mm_dd_yyyy)
    last_updated = Column(String, validate=validate_date)
    appointments = relationship('Appointment', back_populates='patient')

class Doctor(Base):
    __tablename__ = 'doctors'
    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    appointments = relationship('Appointment', back_populates='doctor')

class Appointment(Base):
    __tablename__ = 'appointments'
    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey('patients.id'))
    doctor_id = Column(Integer, ForeignKey('doctors.id'))
    date_time = Column(String, nullable=False, validate=validate_date)
    actual_doctor = Column(Boolean, default=False)
    patient = relationship('Patient', back_populates='appointments')
    doctor = relationship('Doctor', back_populates='appointments')
    
    '''
    