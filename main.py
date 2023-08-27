#!/usr/bin/env/python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Patient, Doctor

engine = create_engine("sqlite:///patient_doctor.db")
Session = sessionmaker(bind=engine)
session = Session()
print(session.query(Patient))