#!/usr/bin/env python

import sys
from simple_term_menu import TerminalMenu
import click
import time
from tabulate import tabulate    
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Appointment, Base, Doctor, Patient
from banners import *
from helpers import *


def main_menu():
    menu_title = "Patient Appointment Tracking CLI"
    menu_items = ["Doctor Options", "Patient Options", "Search Appointments by Patient", "Exit"]

    main_menu = TerminalMenu(menu_entries=menu_items, title=menu_title)
    menu_selection = main_menu.show()

    return menu_selection

@click.command()
def main():
    try:
        database_url = "sqlite:///patient_doctor.db"  # Change this to your database URL
        engine = create_engine(database_url)
        Base.metadata.create_all(bind=engine)
        Session = sessionmaker(bind=engine)
        session = Session()    
        
        welcome_banner()
        choice = main_menu()

        if choice == 0:  # Doctor Options
            doctor_submenu(session)
                
        elif choice == 1:  # Patient Options
            patient_submenu(session)
                
        elif choice == 2:  # Search Appointments by Patient
            search_by_patient_info_menu(session)

        elif choice == 3:  # Exit
            click.echo("Exiting the application. Goodbye!")
            exit(1)
            
    except Exception as e:
        click.echo(f"An error occurred: {str(e)}")
        sys.exit(1)

def doctor_submenu(session):
    while True:
        
        doctor_submenu_banner()
        doctor_submenu_items = [
        "View All Doctors",
        "Search Doctor by ID",
        "Search Doctor by Name",
        "Back",
    ]
        doctor_submenu = TerminalMenu(doctor_submenu_items, title="Doctor Options")
        selected_index = doctor_submenu.show()

        if selected_index == 0:
            view_all_doctors(session)
            time.sleep(5)
            main()
        elif selected_index == 1:
            doctor_id = int(input("Enter Doctor ID: "))
            search_doctor_by_id(session, doctor_id)
            doctor_submenu()
        elif selected_index == 2:
            search_by_doctor_menu(session)
        elif selected_index == 3:
            return main()
    
        doctor_submenu.show()

def patient_submenu(session):
    patient_submenu_banner()
    patient_submenu_items = [
        "View All Patients",
        "Add Patient",
        "Search Patient by Name",
        "Back",
    ]
    patient_submenu = TerminalMenu(patient_submenu_items, title="Patient Options")
    selected_index = patient_submenu.show()

    if selected_index == 0:
        view_all_patients(session)
    elif selected_index == 1:
        first_name = sanitize_input(input("Enter First Name: "))
        last_name = sanitize_input(input("Enter Last Name: "))
        phone_number = sanitize_input(input("Enter Phone Number: "))
        next_appointment = sanitize_input(
            input("Enter Next Appointment (MM-DD-YYYY HH:MM am/pm format): ")
        )
        Patient(session, first_name, last_name, phone_number, next_appointment)
        
        session.add(Patient)
        
    elif selected_index == 2:
        search_by_patient_menu(session)
    elif selected_index == 3:
        main()


def search_by_patient_info_menu(session):
    search_type_menu_items = [
        "Search All Appointments by Patient",
        "Search Specific Appointment by Patient",
        "Back",
    ]
    search_type_menu = TerminalMenu(
        search_type_menu_items, title="Search Appointments by Patient"
    )
    selected_index = search_type_menu.show()

    if selected_index == 0:
        search_all_appointments_by_patient(session)
    elif selected_index == 1:
        search_specific_appointment_by_patient(session)
    elif selected_index == 2:
        return

def search_by_doctor_menu(session):
    doctor_first_name = sanitize_input(input("Enter Doctor's First Name: "))
    doctor_last_name = sanitize_input(input("Enter Doctor's Last Name: "))
    doctors = search_doctor_by_name(session, doctor_first_name, doctor_last_name)

    if doctors:
        doctor_data = [
            (doctor.id, doctor.first_name, doctor.last_name) for doctor in doctors
        ]
        headers = ["Doctor ID", "First Name", "Last Name"]
        print(tabulate(doctor_data, headers=headers, tablefmt="grid"))
        doctor_id = int(input("Enter Doctor ID for details (or 0 to cancel): "))
        if doctor_id == 0:
            return
        appointments = search_appointments_by_doctor(session, doctor_id)
        if appointments:
            appointment_data = [
                (
                    appointment.id,
                    appointment.patient.first_name,
                    appointment.patient.last_name,
                    appointment.date_time,
                )
                for appointment in appointments
            ]
            headers = [
                "Appointment ID",
                "Patient First Name",
                "Patient Last Name",
                "Date and Time",
            ]
            print(appointment_submenu_banner())
            print(tabulate(appointment_data, headers=headers, tablefmt="grid"))
        else:
            print("No appointments found for this doctor.")
    else:
        print("Doctor not found.")


def search_patient_by_name(session, first_name, last_name):
    patients = (
        session.query(Patient)
        .filter(
            Patient.first_name.ilike(f"%{first_name}%"),
            Patient.last_name.ilike(f"%{last_name}%"),
        )
        .all()
    )
    return patients


def view_all_patients(session):
    patients = session.query(Patient).all()
    if patients:
        patient_data = [
            (
                patient.id,
                patient.first_name,
                patient.last_name,
                patient.phone_number,
                patient.next_appointment,
                patient.created_date,
                patient.last_updated,
            )
            for patient in patients
        ]
        headers = [
            "ID",
            "First Name",
            "Last Name",
            "Phone Number",
            "Next Appointment",
            "Created Date",
            "Last Updated",
        ]
        print(tabulate(patient_data, headers=headers, tablefmt="grid"))
    else:
        print("No patients found.")


def search_by_patient_menu(session):
    patient_first_name = sanitize_input(input("Enter Patient's First Name: "))
    patient_last_name = sanitize_input(input("Enter Patient's Last Name: "))
    patients = search_patient_by_name(session, patient_first_name, patient_last_name)

    if patients:
        patient_data = [
            (
                patient.id,
                patient.first_name,
                patient.last_name,
                patient.phone_number,
                patient.next_appointment,
                patient.created_date,
                patient.last_updated,
            )
            for patient in patients
        ]
        headers = [
            "ID",
            "First Name",
            "Last Name",
            "Phone Number",
            "Next Appointment",
            "Created Date",
            "Last Updated",
        ]
        print(tabulate(patient_data, headers=headers, tablefmt="grid"))
    else:
        print("No patients found.")


if __name__ == "__main__":
    main()