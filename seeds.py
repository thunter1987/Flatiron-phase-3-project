from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Patient

print("Starting Seed")

engine = create_engine("sqlite:///patient_doctor.db")
Session = sessionmaker(bind=engine)
session = Session()

import ipdb
import re
from faker import Faker

fake = Faker()

session.query(Patient).delete()

def generate_and_format_phone_number():
  while True:
            
    # Generate a random phone number as a string
    phone_number = fake.phone_number()

    # Format the phone number as (XXX) XXX-XXXX using regular expressions
    formatted_phone_number = re.sub(r"(\d{3})(\d{3})(\d{4})", r"(\1) \2-\3", phone_number)

    # Check if the formatted phone number matches the expected format
    if re.match(r"\(\d{3}\) \d{3}-\d{4}", formatted_phone_number):
      return formatted_phone_number

    # Generate and format a phone number until it's properly formatted
properly_formatted_phone_number = generate_and_format_phone_number()
    
for _ in range(20):


    patient = Patient(
        patient_first_name=fake.first_name(),
        patient_last_name=fake.last_name(),
        patient_phone=generate_and_format_phone_number()
    )

    # patients = [Patient(patient_first_name="John", patient_last_name="Smith", patient_phone="936-247-0238", patient_next_appointment=datetime(year=2023, month=9, day=2, hour=8, minute=30)),
    #             Patient(patient_first_name="Jane", patient_last_name="Doe",
    #                     patient_phone="832-287-9443", patient_next_appointment=datetime(year=2024, month=8, day=15, hour=13, minute=30))
    #             ]
    session.add(patient)
    print(patient)
session.commit()

print("Finished Seeding!")
