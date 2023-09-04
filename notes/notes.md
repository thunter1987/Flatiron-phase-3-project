# flatiron-phase-3-project

## Notes

### _Minimum Requirements_

* [ ] A CLI application  
  * [ ] that solves a real-world problem
  * [ ] adheres to best practices.

* [ ] A database created with SQLAlchemy
  * [ ] modified with SQLAlchemy ORM
  * [ ] 2+ related tables

* [ ] A well-maintained virtual environment using Pipenv.

* [ ] Proper package structure in your application.

* [ ] Use of lists
* [ ] Use of dicts

### _Stretch Goals_

* [ ] A database created with SQLAlchemy
  * [] modified with SQLAlchemy ORM
  * [ ] 3+ related tables.

* [ ] Uses many-to-many relationships

* [ ] Use of additional data structures
  * [ ] uses ranges
  * [ ] uses tuples.

## Project Idea 1

### Main idea

* A patient doctor database to manage appointment information for doctors and patients.

### User story

* Users can create new patients with attributes.
* Users can create new doctors with attributes.
* Users can set up appointments between patients and doctors.

### How I will use the concepts I recently learned to meet the project requirements

* Object Oriented Python
  * Class for Doctors with attributes
  * Class for Patients with attributes

* Database Tables

  * Table: Doctors
    * id  
    * first_name
    * last_name
    * specialty

  * Table: Patients
    * id
    * first_name
    * last_name
    * telephone

  * Table: Appointments
    * ID
    * time
    * doctor_ID
    * patient_ID  

* Object Relationships
  
  *Patients can have many appointments
  * Doctors can have many patients
  * Appointments = many to many
    * with join table doctor_patient_appointments

* Aggregate and Association Methods
  * CRUD
    * Create
      * Create a list of appointments
    * Read
      * Read One
        * Display one patient with id
      * Read All
        * Display all appointments
    * Update
      * Update patient appointments
    * Delete
      * Delete appointments

* Use of Data Structures
  * LIST: List of patient appointments
  * DICTIONARY: Doctors and Patients have attributes and values

### What area I think will be most challenging

* creating join tables for the many to many relationship between doctor and patient

## Project Idea 2

### Main idea

* A patient doctor database to manage appointment information for doctors and patients.

### User story

* Users can create new vehicles with attributes.
* Users can create new parking designations with attributes.
* Users can set up relationships between vehicles and parking designations.

### How I will use the concepts I recently learned to meet the project requirements

* Object Oriented Python
  * Class for Vehicle with attributes
  * Class for Parking with attributes

* Database Tables

  * Table: Vehicle
    * id  
    * owner_first_name
    * owner_last_name
    * approved parking location(s)

  * Table: Parking
    * id
    * availability

  * Table: Allowed_Vehicles
    * ID
    * Parking_ID
    * Vehicle_ID(s)

* Object Relationships
  
  *Parking can have many vehicles associated
  * Vehicles can have many Parking locations associated
  * Vehicles_Allowed = many to many
    * with join table vehicle_to_parking

* Aggregate and Association Methods
  * CRUD
    * Create
      * Create a list of vehicles
    * Read
      * Read One
        * Display one Parking location with id
      * Read All
        * Display all Parking locations
    * Update
      * Update vehicle associated with parking location
    * Delete
      * Delete vehicles

* Use of Data Structures
  * LIST: List of parking spots
  * DICTIONARY:  Vehicles have attributes and values

### What area I think will be most challenging

* creating join tables for the many to many relationship between vehicles and parking spots
