 Agricultural-system
Object-Oriented Programming Assignment - DPG Compliant Agriculture Scan System
 PROG211: Object-Oriented Programming 1 - Assignment
Agriculture Crop Disease Scan & Diagnosis System

 Overview
This project is an object-oriented Python application designed to manage agricultural crop health scans, automate symptom-based diagnostics, and maintain organized records.

 Features
Classes & Objects: Utilizes `PlantScan` and `Farmer` classes to model real-world agricultural entities and behaviors.
Data Structures: Implements Python dictionaries for object record storage and tuples (`SEVERITY_LEVELS`) for immutable categorization.
Methods: Includes instance methods for diagnosis and report generation, as well as a class method (`@classmethod`) for tracking system-wide metrics.

 Digital Public Goods (DPG) Alignment
Privacy-Respecting**: No sensitive personal data (PII) is stored; the system relies strictly on anonymous identifier codes (`farmer_id` and `scan_id`).
Open & Modular: Written in clean, modular Python code following PEP 8 standards, making it easy to inspect, test, and reuse.

 How to Run
1. Ensure Python is installed on your system.
2. Open the project folder in PyCharm or any Python IDE.
3. Run `main.py`:
   ```bash
   python main.py
