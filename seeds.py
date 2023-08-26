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

def generate_formatted_datetime():

    # Generate a random datetime within the specified range
    random_datetime = fake.date_time_between_dates(datetime(2023, 8, 24, 8, 15), datetime(2024, 8, 23, 17, 0))

    # Format the datetime as yyyy-mm-dd hh:mm
    formatted_datetime = random_datetime.strftime("%Y-%m-%d %H:%M")
    return formatted_datetime




    
for _ in range(20):


    patient = Patient(
        patient_first_name=fake.first_name(),
        patient_last_name=fake.last_name(),
        patient_phone=generate_and_format_phone_number(),
        patient_next_appointment=generate_formatted_datetime()
    )

    session.add(patient)
    print(patient)
session.commit()

print("Finished Seeding!")
