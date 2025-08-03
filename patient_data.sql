USE health_monitor;
CREATE TABLE patient_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    bp INT,
    sugar INT,
    cholesterol INT,
    heart INT,
    spo2 INT,
    respiration INT,
    weight FLOAT,
    height FLOAT,
    temperature FLOAT,
    bmi FLOAT,
    submitted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
