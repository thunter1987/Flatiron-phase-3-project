from datetime import datetime
from models import Patient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
print("Starting Seed")

engine = create_engine('sqlite:///patient_doctor.db')

Session = sessionmaker(bind=engine)
session = Session()

session.query(Patient).delete()


patients = [Patient(patient_first_name="John", patient_last_name="Smith", patient_phone="936-247-0238", patient_next_appointment=datetime(2023, 9, 2, 8, 30)),
            Patient(patient_first_name="Jane", patient_last_name="Doe",
                    patient_phone="832-287-9443", patient_next_appointment=datetime(2024, 8, 15, 13, 30))
            ]
session.add_all(patients)
session.commit()
session.close()

print("Finished Seeding!")
