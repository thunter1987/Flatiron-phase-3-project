# Flatiron-phase-3-project
## Appointment Tracking CLI App

The Appointment Tracking CLI App is a simple command-line application designed to help you manage patient appointments and doctor information. This app allows you to keep track of appointments, patient details, and doctor information using a user-friendly interface.

### Features

- Add and manage patient appointments
- Maintain patient records including names, phone numbers, and appointment schedules
- Keep track of doctor information, specialties, and appointments
- Search and view appointments by patient, doctor, or date
- Easy-to-use command-line interface
- Built-in validation to ensure accurate data input

### Getting Started

1. **Installation**: Before using the app, make sure you have Python and the required dependencies installed. You can install the dependencies using the following command:

    ```
    pip install -r requirements.txt
    ```

2. **Database Setup**: The app uses an SQLite database to store information. The database file (`app.db`) will be automatically created when you run migrations and seed data.

3. **Running Migrations**: To set up the database schema, run the following command:

    ```
    alembic upgrade head
    ```

4. **Seeding Data**: You can populate the database with initial data by running the seeds script:

    ```
    python seeds.py
    ```

5. **Using the App**: To use the app, run the following command:

    ```
    python cli.py <database_url>
    ```

    Replace `<database_url>` with your SQLite database URL. This will launch the interactive CLI menu, where you can navigate through various options to manage appointments and patient information.

### App Workflow

1. Main Menu: Choose between doctor options, patient options, search appointments, or exit the app.
2. Doctor Options: View all doctors, search doctors by ID or name.
3. Patient Options: View all patients, add a new patient, or search patients by name.
4. Search Appointments: Search appointments by patient information.
5. Exit: Quit the application.

### Example Usage

1. To view all doctors, choose the "Doctor Options" from the main menu and then select "View All Doctors."
2. To add a new patient, choose "Patient Options" and then select "Add Patient." Follow the prompts to enter patient details.
3. To search for appointments by patient information, select "Search Appointments by Patient."

### Contributing

Contributions to this project are welcome! If you find issues or have suggestions, please open an issue or submit a pull request.

### License

This project is licensed under the [MIT License](LICENSE).
