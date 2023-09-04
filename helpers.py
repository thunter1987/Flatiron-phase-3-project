import re
from tabulate import tabulate    
from datetime import datetime
from banners import *
from models import *

def sanitize_input(input_str):
    return input_str.strip()

def validate_datetime(date_str):
    stripped_date_str = date_str.strip()  # Strip whitespace
    try:
        datetime.strptime(stripped_date_str, "%m-%d-%Y %I:%M %p")
        return True
    except ValueError:
        return False

def validate_phone_number(phone_number):
    stripped_phone_number = phone_number.strip()  # Strip whitespace
    return bool(re.match(r'^\(\d{3}\) \d{3}-\d{4}$', stripped_phone_number))

def validate_date(date_str):
    stripped_date_str = date_str.strip()  # Strip whitespace
    try:
        datetime.strptime(stripped_date_str, "%m-%d-%Y")
        return True
    except ValueError:
        return False
    
def view_all_doctors(session):
    doctor = session.query(Doctor).all()
    if doctor:
        doctor_data = [
            (
                doctor.id,
                doctor.first_name,
                doctor.last_name,
                doctor.specialty,
            )
            for doctor in doctor
        ]
        headers = [
            "ID",
            "First Name",
            "Last Name",
            "Specialty"
        ]
        print(tabulate(doctor_data, headers=headers, tablefmt="grid"))
    else:
        print("No doctor found.")


def search_doctor_by_name(session, first_name, last_name):
    doctors = session.query(Doctor).filter(Doctor.first_name.ilike(f"%{first_name}%"), Doctor.last_name.ilike(f"%{last_name}%")).all()
    return doctors

def search_doctor_by_id(session, doctor_id: int):
    try:
        # Use SQLAlchemy to query the Doctor model by the given ID
        doctor = session.query(Doctor).filter(Doctor.id == doctor_id).all()
        
        if doctor:
            return doctor  # Return the found doctor
        else:
            return None  # Return None if no doctor with the given ID is found
    except Exception as e:
        raise Exception(f"Error searching for doctor by ID: {str(e)}")

# def search_doctor_by_id(session, doctor_id):
#     doctor = session.query(Doctor).filter_by(id=doctor_id).first()
#     return doctor if doctor else []

def search_patient_by_name(session, first_name, last_name):
    patients = session.query(Patient).filter(Patient.first_name.ilike(f"%{first_name}%"), Patient.last_name.ilike(f"%{last_name}%")).all()
    return patients

def search_appointments_by_doctor(session, doctor_id):
    appointments = session.query(Appointment).filter_by(doctor_id=doctor_id).all()
    return appointments

def search_all_appointments_by_patient(session):
    patient_first_name = sanitize_input(input("Enter Patient's First Name: "))
    patient_last_name = sanitize_input(input("Enter Patient's Last Name: "))
    patients = search_patient_by_name(session, patient_first_name, patient_last_name)

    if patients:
        patient = patients[0]
        appointments = session.query(Appointment).filter_by(patient_id=patient.id).all()
        if appointments:
            appointment_data = [
                (
                    appointment.id,
                    appointment.doctor.first_name,
                    appointment.doctor.last_name,
                    appointment.date_time,
                )
                for appointment in appointments
            ]
            headers = ["Appointment ID", "Doctor First Name", "Doctor Last Name"]
            print(appointment_submenu_banner())
            print(tabulate(appointment_data, headers=headers, tablefmt="grid"))
            
def search_specific_appointment_by_patient(session, appointment_id, patient_id):
    appointment = session.query(Appointment).filter_by(id=appointment_id, patient_id=patient_id).first()
    return [appointment] if appointment else []
