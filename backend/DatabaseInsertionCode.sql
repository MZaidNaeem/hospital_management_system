INSERT INTO Hospital (hospital_name)
VALUES ('City Hospital')




SET IDENTITY_INSERT Branches ON;

INSERT INTO Branches (branch_id, hospital_id, branch_name, contact_number)
VALUES (1, 1, 'Main Branch', '03001234567');

SET IDENTITY_INSERT Branches OFF;
GO





INSERT INTO Admin (hospital_id, first_name, last_name, cnic, email, password)
VALUES
(1, 'Ali', 'Khan', '1', 'ali.admin@example.com', '123'),
(1, 'Sara', 'Ahmad', '2', 'sara.admin@example.com', '456');
GO





SET IDENTITY_INSERT Doctors ON;

INSERT INTO Doctors (doctor_id,branch_id, first_name, last_name, email, cnic, password, specialty, contact_number)
VALUES
(1,1, 'Dr. Faisal', 'Shah', 'faisal.doctor@example.com', '3', '123', 'Cardiology', '03009998877'),
(2, 1, 'Dr. Hina', 'Khan', 'hina.doctor@example.com', '4', '456', 'Neurology', '03006667788');
GO

SET IDENTITY_INSERT Doctors OFF;




INSERT INTO Patients (first_name, last_name, email, cnic, password, gender, contact_number)
VALUES
('Ahmed', 'Raza', 'ahmed.patient@example.com', '5', '123', 'Male', '03001112233'),
('Ayesha', 'Ali', 'ayesha.patient@example.com', '6', '456', 'Female', '03004445566');
GO



