-- Create Database
CREATE DATABASE HospitalManagementSystem;
GO

USE HospitalManagementSystem;
GO

--------------------------------------------------------
-- Table: Hospital
--------------------------------------------------------
CREATE TABLE Hospital (
    hospital_id INT PRIMARY KEY IDENTITY(1,1),
    hospital_name VARCHAR(255),
    created_at DATETIME DEFAULT GETDATE()
);
GO

--------------------------------------------------------
-- Table: Branches
--------------------------------------------------------
CREATE TABLE Branches (
    branch_id INT PRIMARY KEY IDENTITY(1,1),
    hospital_id INT NOT NULL DEFAULT 1,
    branch_name VARCHAR(255) UNIQUE,
    contact_number VARCHAR(50),
    created_at DATETIME DEFAULT GETDATE(),
    deleted BIT NOT NULL DEFAULT 0;
    FOREIGN KEY (hospital_id) REFERENCES Hospital(hospital_id)
);
GO

--------------------------------------------------------
-- Table: Admin
--------------------------------------------------------
CREATE TABLE Admin (
    admin_id INT PRIMARY KEY IDENTITY(1,1),
    hospital_id INT NOT NULL DEFAULT 1,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    cnic VARCHAR(13) UNIQUE,
    email VARCHAR(255) UNIQUE,
    password VARCHAR(255),
    created_at DATETIME DEFAULT GETDATE(),
    deleted BIT NOT NULL DEFAULT 0;
    FOREIGN KEY (hospital_id) REFERENCES Hospital(hospital_id)
);
GO

--------------------------------------------------------
-- Table: Patients
--------------------------------------------------------
CREATE TABLE Patients (
    patient_id INT PRIMARY KEY IDENTITY(1,1),
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    email VARCHAR(255) UNIQUE,
    cnic VARCHAR(13) UNIQUE,
    password VARCHAR(255),
    gender VARCHAR(20),
    contact_number VARCHAR(50),
    deleted BIT NOT NULL DEFAULT 0;
    created_at DATETIME DEFAULT GETDATE()
);
GO

--------------------------------------------------------
-- Table: Doctors
--------------------------------------------------------
CREATE TABLE Doctors (
    doctor_id INT PRIMARY KEY IDENTITY(1,1),
    branch_id INT NOT NULL,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    email VARCHAR(255),
    cnic VARCHAR(13),
    password VARCHAR(255),
    specialty VARCHAR(100),
    contact_number VARCHAR(50),
    created_at DATETIME DEFAULT GETDATE(),
    deleted BIT NOT NULL DEFAULT 0,
    CONSTRAINT FK_Doctors_Branch FOREIGN KEY (branch_id) REFERENCES Branches(branch_id),
    CONSTRAINT UQ_Doctor_Branch_CNIC UNIQUE (branch_id, cnic)
    CONSTRAINT UQ_Doctor_CNIC_Password UNIQUE (cnic, password);
);
GO


--------------------------------------------------------
-- Table: Appointments
--------------------------------------------------------
CREATE TABLE Appointments (
    appointment_id INT PRIMARY KEY IDENTITY(1,1),
    patient_id INT NOT NULL,
    doctor_id INT NOT NULL,
    appointment_time DATETIME,
    status VARCHAR(20) DEFAULT 'Scheduled',
    created_at DATETIME DEFAULT GETDATE(),
    FOREIGN KEY (patient_id) REFERENCES Patients(patient_id),
    FOREIGN KEY (doctor_id) REFERENCES Doctors(doctor_id),
    CHECK (status IN ('Scheduled', 'Completed', 'Cancelled'))
);
GO

--------------------------------------------------------
-- Table: Rooms
--------------------------------------------------------
CREATE TABLE Rooms (
    room_id INT PRIMARY KEY IDENTITY(1,1),
    branch_id INT NOT NULL,
    status VARCHAR(20) DEFAULT 'Available',
    last_serviced DATETIME,
    deleted BIT NOT NULL DEFAULT 0;
    FOREIGN KEY (branch_id) REFERENCES Branches(branch_id),
    CHECK (status IN ('Available', 'Occupied', 'Under Maintenance'))
);
GO

--------------------------------------------------------
-- Table: Room Assignments
--------------------------------------------------------
CREATE TABLE Room_Assignments (
    assignment_id INT PRIMARY KEY IDENTITY(1,1),
    appointment_id INT NOT NULL,
    room_id INT NOT NULL,
    assignment_start DATETIME,
    assignment_end DATETIME,
    FOREIGN KEY (appointment_id) REFERENCES Appointments(appointment_id),
    FOREIGN KEY (room_id) REFERENCES Rooms(room_id)
);
GO



