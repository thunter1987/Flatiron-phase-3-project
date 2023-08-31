# app/cli.py

import argparse
from datetime import datetime
from sqlalchemy.orm import sessionmaker
from .models import Patient, Doctor, Appointment
from .helpers import validate_datetime, validate_phone_number, validate_mm_dd_yyyy, sanitize_input
from simple_terminal_menu import TerminalMenu
from tabulate import tabulate  # Import the tabulate library for formatting tables
import re

def main_menu(session):
    while True:
        main_menu_items = [
            "Doctor Options",
            "Patient Options",
            "Search Appointments by Patient",
            "Exit"
        ]
        
        main_menu = TerminalMenu(main_menu_items, title="Main Menu")
        selected_index = main_menu.show()

        if selected_index == 0:
            doctor_submenu(session)
        elif selected_index == 1:
            patient_submenu(session)
        elif selected_index == 2:
            search_by_patient_info_menu(session)
        elif selected_index == 3:
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please choose a valid option.")

def doctor_submenu(session):
    doctor_submenu_items = [
        "View All Doctors",
        "Search Doctor by ID",
        "Search Doctor by Name",
        "Back"
    ]
    doctor_submenu = TerminalMenu(doctor_submenu_items, title="Doctor Options")
    selected_index = doctor_submenu.show()

    if selected_index == 0:
        view_all_doctors(session)
    elif selected_index == 1:
        doctor_id = int(input("Enter Doctor ID: "))
        search_doctor_by_id(session, doctor_id)
    elif selected_index == 2:
        search_by_doctor_menu(session)
    elif selected_index == 3:
        return

def patient_submenu(session):
    patient_submenu_items = [
        "View All Patients",
        "Add Patient",
        "Search Patient by Name",
        "Back"
    ]
    patient_submenu = TerminalMenu(patient_submenu_items, title="Patient Options")
    selected_index = patient_submenu.show()

    if selected_index == 0:
        view_all_patients(session)
    elif selected_index == 1:
        first_name = sanitize_input(input("Enter First Name: "))
        last_name = sanitize_input(input("Enter Last Name: "))
        phone_number = sanitize_input(input("Enter Phone Number: "))
        next_appointment = sanitize_input(input("Enter Next Appointment (MM-DD-YYYY HH:MM am/pm format): "))
        add_patient(session, first_name, last_name, phone_number, next_appointment)
    elif selected_index == 2:
        search_by_patient_menu(session)
    elif selected_index == 3:
        return

def search_by_patient_info_menu(session):
    search_type_menu_items = [
        "Search All Appointments by Patient",
        "Search Specific Appointment by Patient",
        "Back"
    ]
    search_type_menu = TerminalMenu(search_type_menu_items, title="Search Appointments by Patient")
    selected_index = search_type_menu.show()

    if selected_index == 0:
        search_all_appointments_by_patient(session)
    elif selected_index == 1:
        search_specific_appointment_by_patient(session)
    elif selected_index == 2:
        return

def search_doctor_by_name(session, first_name, last_name):
    doctors = session.query(Doctor).filter(Doctor.first_name.ilike(f"%{first_name}%"), Doctor.last_name.ilike(f"%{last_name}%")).all()
    return doctors

def search_doctor_by_id(session, doctor_id):
    doctor = session.query(Doctor).filter_by(id=doctor_id).first()
    return [doctor] if doctor else []

def search_appointments_by_doctor(session, doctor_id):
    appointments = session.query(Appointment).filter_by(doctor_id=doctor_id).all()
    return appointments

def search_by_doctor_menu(session):
    doctor_first_name = sanitize_input(input("Enter Doctor's First Name: "))
    doctor_last_name = sanitize_input(input("Enter Doctor's Last Name: "))
    doctors = search_doctor_by_name(session, doctor_first_name, doctor_last_name)

    if doctors:
        doctor_data = [(doctor.id, doctor.first_name, doctor.last_name) for doctor in doctors]
        headers = ["Doctor ID", "First Name", "Last Name"]
        print(tabulate(doctor_data, headers=headers, tablefmt="grid"))
        doctor_id = int(input("Enter Doctor ID for details (or 0 to cancel): "))
        if doctor_id == 0:
            return
        appointments = search_appointments_by_doctor(session, doctor_id)
        if appointments:
            appointment_data = [(appointment.id, appointment.patient.first_name, appointment.patient.last_name, appointment.date_time) for appointment in appointments]
            headers = ["Appointment ID", "Patient First Name", "Patient Last Name", "Date and Time"]
            print(tabulate(appointment_data, headers=headers, tablefmt="grid"))
        else:
            print("No appointments found for this doctor.")
    else:
        print("Doctor not found.")

def search_patient_by_name(session, first_name, last_name):
    patients = session.query(Patient).filter(Patient.first_name.ilike(f"%{first_name}%"), Patient.last_name.ilike(f"%{last_name}%")).all()
    return patients

def view_all_patients(session):
    patients = session.query(Patient).all()
    if patients:
        patient_data = [(patient.id, patient.first_name, patient.last_name, patient.phone_number, patient.next_appointment, patient.created_date, patient.last_updated) for patient in patients]
        headers = ["ID", "First Name", "Last Name", "Phone Number", "Next Appointment", "Created Date", "Last Updated"]
        print(tabulate(patient_data, headers=headers, tablefmt="grid"))
    else:
        print("No patients found.")

def search_by_patient_menu(session):
    patient_first_name = sanitize_input(input("Enter Patient's First Name: "))
    patient_last_name = sanitize_input(input("Enter Patient's Last Name: "))
    patients = search_patient_by_name(session, patient_first_name, patient_last_name)
    
    if patients:
        patient_data = [(patient.id, patient.first_name, patient.last_name, patient.phone_number, patient.next_appointment, patient.created_date, patient.last_updated) for patient in patients]
        headers = ["ID", "First Name", "Last Name", "Phone Number", "Next Appointment", "Created Date", "Last Updated"]
        print(tabulate(patient_data, headers=headers, tablefmt="grid"))
    else:
        print("No patients found.")

def search_all_appointments_by_patient(session):
    patient_first_name = sanitize_input(input("Enter Patient's First Name: "))
    patient_last_name = sanitize_input(input("Enter Patient's Last Name: "))
    patients = search_patient_by_name(session, patient_first_name, patient_last_name)
    
    if patients:
        patient = patients[0]
        appointments = session.query(Appointment).filter_by(patient_id=patient.id).all()
        if appointments:
            appointment_data = [(appointment.id, appointment.doctor.first_name, appointment.doctor.last_name, appointment.date_time) for appointment in appointments]
            headers = ["Appointment ID", "Doctor First Name", "Doctor Last Name"]

def main():
    parser = argparse.ArgumentParser(description="CLI App for Patient Appointments")
    parser.add_argument("database_url", type=str, help="Database URL")
    args = parser.parse_args()
    
    engine = create_engine(args.database_url)
    Session = sessionmaker(bind=engine)
    session = Session()
    
    main_menu(session)
    
    session.commit()
    session.close()

if __name__ == "__main__":
    main()
