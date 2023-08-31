from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Patient, Doctor
import random

print("Starting Seed")

engine = create_engine("sqlite:///patient_doctor.db")
Session = sessionmaker(bind=engine)
session = Session()

import ipdb
import re
from faker import Faker

fake = Faker()

session.query(Patient).delete()
session.query(Doctor).delete()


def generate_and_format_phone_number():
    while True:
        # Generate a random phone number as a string
        phone_number = fake.phone_number()

        # Format the phone number as (XXX) XXX-XXXX using regular expressions
        formatted_phone_number = re.sub(
            r"(\d{3})(\d{3})(\d{4})", r"(\1) \2-\3", phone_number
        )

        # Check if the formatted phone number matches the expected format
        if re.match(r"\(\d{3}\) \d{3}-\d{4}", formatted_phone_number):
            return formatted_phone_number

        # Generate and format a phone number until it's properly formatted


properly_formatted_phone_number = generate_and_format_phone_number()


def generate_formatted_datetime():
    # Generate a random datetime within the specified range
    random_datetime = fake.date_time_between_dates(
        datetime(2023, 8, 24, 8, 15), datetime(2024, 8, 23, 17, 0)
    )

    # Format the datetime as yyyy-mm-dd hh:mm
    formatted_datetime = random_datetime.strftime("%Y-%m-%d %H:%M")
    return formatted_datetime


for _ in range(20):
    patient = Patient(
        first_name=fake.first_name(),
        last_name=fake.last_name(),
        phone=generate_and_format_phone_number(),
        next_appointment=generate_formatted_datetime(),
        doctor_id = random.randint(1, 5)
    )

    session.add(patient)
    print(patient)

doctors = []
specialties = ["Primary Care", "Cardiology", "Neurology", "Ophthalmology", "Pediatrics"]

doctor1 = Doctor("Andrea", "Jones", "Ophthalmology")
doctor2 = Doctor("Laura", "Richmond", "Cardiology")
doctor3 = Doctor("Christopher", "Baker", "Neurology")
doctor4 = Doctor("Thomas", "Walker", "Primary Care")
doctor5 = Doctor("Joseph", "Smith", "Pediatrics")
doctors = [doctor1, doctor2, doctor3, doctor4, doctor5]
session.add_all(doctors)
print(doctors)
session.commit()
session.close()

print("Finished Seeding!")

        ###########NEW CODE#########
'''
    MOVE TO:   # app/seeds.py

import random
from sqlalchemy.orm import Session
from .models import Doctor, Patient, Appointment
from datetime import datetime, timedelta

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
    "Endocrinology"
]

def seed_data(session: Session):
    # Add doctors with random medical specialties
    doctors = []
    for _ in range(5):
        first_name = f"Doctor{random.randint(1, 100)}"
        last_name = "Smith"
        specialty = random.choice(medical_specialties)
        doctor = Doctor(first_name=first_name, last_name=last_name, specialty=specialty)
        doctors.append(doctor)
    
    session.add_all(doctors)
    session.commit()

   # Add patients
    patients = []
    for _ in range(20):
        first_name = f"Patient{random.randint(1, 100)}"
        last_name = "Doe"
        phone_number = f"({random.randint(100, 999)}) {random.randint(100, 999)}-{random.randint(1000, 9999)}"
        next_appointment = (datetime.now() + timedelta(days=random.randint(1, 30))).strftime("%m-%d-%Y %I:%M %p")
        patient = Patient(first_name=first_name, last_name=last_name, phone_number=phone_number, next_appointment=next_appointment)
        patients.append(patient)
    
    session.add_all(patients)
    session.commit()

    # Add appointments for patients
    for patient in patients:
        for _ in range(4):  # Adding 4 appointments for each patient
            doctor = random.choice(doctors)
            date_time = datetime.now() + timedelta(days=random.randint(1, 30), hours=random.randint(8, 17))
            appointment = Appointment(doctor_id=doctor.id, patient_id=patient.id, date_time=date_time)
            session.add(appointment)
    
    session.commit()

if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from app.models import Base

    database_url = "sqlite:///app.db"  # Change this to your database URL
    engine = create_engine(database_url)
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    seed_data(session)

'''
