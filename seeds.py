from datetime import datetime
from models import Patient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
print("Starting Seed")

engine = create_engine('sqlite:///patient_doctor.db')

Session = sessionmaker(bind=engine)
session = Session()

session.query(Patient).delete()

patients = [
    Patient(patient_first_name = "John", patient_last_name = "Smith"),
    Patient(patient_first_name = "Jane", patient_last_name = "Doe", patient_phone = "832-287-9443", patient_next_appointment = datetime.now(), patient_balance = 125.97)
]

session.bulk_save_objects(patients)
session.commit()

print("Finished Seeding!")