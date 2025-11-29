-- Create Database
CREATE DATABASE HospitalManagementSystem;
GO

-- Use the Database
USE HospitalManagementSystem;
GO

-- Table: Hospital
CREATE TABLE Hospital (
    hospital_id INT PRIMARY KEY IDENTITY(1,1),
    hospital_name VARCHAR(255),
    created_at DATETIME DEFAULT GETDATE()
);
GO

-- Table: Admin
CREATE TABLE Admin (
    admin_id INT PRIMARY KEY IDENTIiTY(1,1),
    hospital_id INT NOT NULL DEFAULT 1,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    cnic VARCHAR(13) UNIQUE,
    email VARCHAR(255) UNIQUE,
    password VARCHAR(255),
    created_at DATETIME DEFAULT GETDATE(),
    FOREIGN KEY (hospital_id) REFERENCES Hospital(hospital_id)
);
GO

-- Table: Branches
CREATE TABLE Branches (
    branch_id INT PRIMARY KEY IDENTITY(1,1),
    hospital_id INT NOT NULL DEFAULT 1,
    branch_name VARCHAR(255),
    address TEXT,
    contact_number VARCHAR(50),
    created_at DATETIME DEFAULT GETDATE(),
    FOREIGN KEY (hospital_id) REFERENCES Hospital(hospital_id)
);
GO

-- Table: Patients
CREATE TABLE Patients (
    patient_id INT PRIMARY KEY IDENTITY(1,1),
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    cnic VARCHAR(13) UNIQUE,
    password VARCHAR(255),
    date_of_birth DATE,
    gender VARCHAR(20),
    contact_number VARCHAR(50),
    address TEXT,
    email VARCHAR(255),
    created_at DATETIME DEFAULT GETDATE()
);
GO


-- Table: Staff
CREATE TABLE Staff (
    staff_id INT PRIMARY KEY IDENTITY(1,1),
    branch_id INT NOT NULL,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    cnic VARCHAR(13) UNIQUE,
    password VARCHAR(255),
    role VARCHAR(20) DEFAULT 'Nurse',
    contact_number VARCHAR(50),
    email VARCHAR(255),
    address TEXT,
    hire_date DATE,
    FOREIGN KEY (branch_id) REFERENCES branch_id(branch_id),
    CHECK (role IN ('Cleaner', 'Nurse'))
);
GO

-- Table: Doctors
CREATE TABLE Doctors (
    doctor_id INT PRIMARY KEY IDENTITY(1,1),
    branch_id INT NOT NULL,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    cnic VARCHAR(13) UNIQUE,
    password VARCHAR(255),
    specialty VARCHAR(100),
    contact_number VARCHAR(50),
    email VARCHAR(255),
    created_at DATETIME DEFAULT GETDATE(),
    FOREIGN KEY (branch_id) REFERENCES branch_id(branch_id)
);
GO

-- Table: Appointments
CREATE TABLE Appointments (
    appointment_id INT PRIMARY KEY IDENTITY(1,1),
    patient_id INT NOT NULL,
    doctor_id INT NOT NULL,
    appointment_date DATE,
    appointment_time TIME,
    status VARCHAR(20) DEFAULT 'Scheduled',
    created_at DATETIME DEFAULT GETDATE(),
    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id),
    FOREIGN KEY (doctor_id) REFERENCES Doctors(doctor_id),
    CHECK (status IN ('Scheduled', 'Completed', 'Cancelled'))
);
GO

-- Table: Prescription
CREATE TABLE Prescription (
    prescription_id INT PRIMARY KEY IDENTITY(1,1),
    prescription_date DATE,
    duration VARCHAR(50)
);
GO

-- Table: Billing
CREATE TABLE Billing (
    bill_id INT PRIMARY KEY IDENTITY(1,1),
    appointment_id INT NOT NULL UNIQUE,
    total_amount DECIMAL(10,2),
    payment_status VARCHAR(20) DEFAULT 'Pending',
    payment_date DATE,
    created_at DATETIME DEFAULT GETDATE(),
    FOREIGN KEY (appointment_id) REFERENCES Appointments(appointment_id),
    CHECK (payment_status IN ('Pending', 'Paid', 'Overdue'))
);
GO

-- Table: Medicine
CREATE TABLE Medicine (
    medicine_id INT PRIMARY KEY IDENTITY(1,1),
    name VARCHAR(255),
    brand VARCHAR(255),
    type VARCHAR(50)
);
GO

-- Table: Medical_Records
CREATE TABLE Medical_Records (
    record_id INT PRIMARY KEY IDENTITY(1,1),
    appointment_id INT NOT NULL,
    prescription_id INT UNIQUE NOT NULL,
    diagnosis TEXT,
    created_at DATETIME DEFAULT GETDATE(),
    FOREIGN KEY (appointment_id) REFERENCES Appointments(appointment_id),
    FOREIGN KEY (prescription_id) REFERENCES Prescription(prescription_id)
);
GO

-- Table: Prescription_Medicine
CREATE TABLE Prescription_Medicine (
    prescription_id INT NOT NULL,
    medicine_id INT NOT NULL,
    dosage VARCHAR(100),
    PRIMARY KEY (prescription_id, medicine_id),
    FOREIGN KEY (prescription_id) REFERENCES Prescription(prescription_id),
    FOREIGN KEY (medicine_id) REFERENCES Medicine(medicine_id)
);
GO

-- Table: Rooms
CREATE TABLE Rooms (
    room_id INT PRIMARY KEY IDENTITY(1,1),
    branch_id INT NOT NULL,
    status VARCHAR(20) DEFAULT 'Available',
    last_serviced DATE,
    is_cleaned VARCHAR(3) DEFAULT 'No',
    FOREIGN KEY (branch_id) REFERENCES Branches(branch_id),
    CHECK (status IN ('Available', 'Occupied', 'Under Maintenance')),
    CHECK (is_cleaned IN ('Yes', 'No'))
);
GO

-- Table: Room_Assignments
CREATE TABLE Room_Assignments (
    assignment_id INT PRIMARY KEY IDENTITY(1,1),
    appointment_id INT NOT NULL,
    staff_id INT,
    room_id INT NOT NULL,
    assignment_start DATETIME,
    assignment_end DATETIME,
    FOREIGN KEY (appointment_id) REFERENCES Appointments(appointment_id),
    FOREIGN KEY (staff_id) REFERENCES Staff(staff_id),
    FOREIGN KEY (room_id) REFERENCES Rooms(room_id)
);
GO

-- Table: Cleaning_Service
CREATE TABLE Cleaning_Service (
    service_id INT PRIMARY KEY IDENTITY(1,1),
    room_id INT NOT NULL,
    service_time DATETIME,
    staff_id INT NOT NULL,
    FOREIGN KEY (room_id) REFERENCES Rooms(room_id),
    FOREIGN KEY (staff_id) REFERENCES Staff(staff_id)
);
GO

PRINT 'Database and tables created successfully!';
GO

-- Insert sample data into Hospital table
INSERT INTO Hospital (hospital_name, created_at)
VALUES ('City General Hospital', GETDATE());
GO

-- Insert sample data into Admin table
INSERT INTO Admin (hospital_id, first_name, last_name, cnic, email, password_hash, created_at)
VALUES (
    1,
    'zaid',
    'naeem',
    '3330221667767',
    'zaidnaeemofficial@cityhospital.com',
    '@123456@',  
    GETDATE()
);
GO

