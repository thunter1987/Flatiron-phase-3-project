from faker import Faker
import random
from datetime import datetime, timedelta

from sqlalchemy.orm import Session
from helpers import *
from models import Appointment, Doctor, Patient

def seed_data(session: Session):

    session.query(Doctor).delete()
    session.query(Patient).delete()
    session.query(Appointment).delete()
    fake = Faker()

    # List of possible medical specialty fields
    medical_specialties = [
        "Cardiology",
        "Dermatology",
        "Gastroenterology",
        "Neurology",
        "Orthopedics",
        "Pediatrics",
        "Psychiatry",
        "Radiology",
        "Urology",
        "Ophthalmology",
        "Oncology",
        "Endocrinology",
    ]

    # Add doctors with random medical specialties
    doctors = []
    for _ in range(5):
        first_name = fake.first_name()
        last_name = fake.last_name()
        specialty = random.choice(medical_specialties)
        doctor = Doctor(first_name=first_name, last_name=last_name, specialty=specialty)
        doctors.append(doctor)
    
    session.add_all(doctors)
    session.commit()


    # Add patients
    patients = []
    for _ in range(20):
        first_name = f"{fake.first_name()}"
        last_name = f"{fake.last_name()}"
        phone_number = f"({random.randint(100, 999)}) {random.randint(100, 999)}-{random.randint(1000, 9999)}"
        next_appointment = datetime.now() + timedelta(days=random.randint(1, 30))
        patient = Patient(first_name=first_name, last_name=last_name, phone_number=phone_number, next_appointment=next_appointment)
        patients.append(patient)
    
    print(patient in patients)

        
    session.add_all(patients)
    session.commit()


    # Add appointments for patients
    appointments = []

    # Adding between 1-2 appointments for each patient
    for patient in patients:
        for _ in range(random.randint(1, 2)):
            doctor = random.choice(doctors)
            date_time = datetime.now() + timedelta(days=random.randint(1, 30))
            appointment = Appointment(doctor_id=doctor.id, patient_id=patient.id, date_time=date_time)
            appointments.append(appointment)
             
    for appointment in appointments:
        print(f"{appointment}")            
                
    session.bulk_save_objects(appointments)
    session.commit()

if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from models import Base

    database_url = "sqlite:///patient_doctor.db"  # Change this to your database URL
    engine = create_engine(database_url)
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    seed_data(session)