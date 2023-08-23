from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Patient

print("Starting Seed")

engine = create_engine('sqlite:///patient_doctor.db')
Session = sessionmaker(bind=engine)
session = Session()

import ipdb
from faker import Faker
fake = Faker()

session.query(Patient).delete()
patients = []

for _ in range (20):
        patient = Patient(
          patient_first_name = fake.first_name(),
          patient_last_name = fake.last_name(),
          patient_phone = fake.phone_number()
        )


# patients = [Patient(patient_first_name="John", patient_last_name="Smith", patient_phone="936-247-0238", patient_next_appointment=datetime(year=2023, month=9, day=2, hour=8, minute=30)),
#             Patient(patient_first_name="Jane", patient_last_name="Doe",
#                     patient_phone="832-287-9443", patient_next_appointment=datetime(year=2024, month=8, day=15, hour=13, minute=30))
#             ]
        patients.append(patient)
        session.add(patient)
        print (patient.id)
session.commit()

print("Finished Seeding!")