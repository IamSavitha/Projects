CheckMyGrade Application

Overview

The CheckMyGrade application is a console-based Python tool for managing student grades and academic information. It helps with user authentication, access control based on user roles, data management, reporting, and basic statistical analysis.

Features

User Authentication:
Users can create accounts as students, professors, or administrators.
Users can log in, and passwords are encrypted.
Role-Based Access: Different features are available depending on the user's role:
Administrator: Manages data for students, professors, courses, and grades.
Student: Can view details for students and courses, search for students, and create reports.
Professor: Can view details for professors and courses, search for professors, update course information, and create reports.
Data Management:
Data is stored and retrieved using CSV files.
The application handles information about students, professors, courses, and grades.
Reporting and Statistics:
The application creates reports for students, professors, and courses.
It calculates statistics like mean, median, mode, and standard deviation for student scores and course grades.
Grade Computation: The application calculates grades from marks using set grade ranges.
Search Feature: The application lets you search for students, professors, and courses.
Data Structures: Uses arrays or linked lists for storing student data.
Sorting: Can display sorted data by student names and grades or marks.
Unique IDs: Student_id, course_id, and professor_id must be unique.
Installation

Python: Make sure you have Python 3.x installed.
Dependencies: You don't need to install any extra libraries beyond what comes with Python (like csv and os).
Usage

To run the application:
Go to the application's folder in your terminal.
Run the main script: python main.py (or whatever your main file is named).
To use the application:
Follow the instructions on the screen to log in or sign up.
Use the menu options to do different things, depending on your user role.
File Structure

The application uses these CSV files to save data:

students.csv: For student information.
professors.csv: For professor information.
course.csv: For course information.
login.csv: For user login information.
student_score.csv: For student scores.
grade.csv: For grade information.
Testing

Make a copy of the repository.
Create a new branch for your changes.
Save your changes.
Upload the branch.
Submit a pull request.

Author
Savitha Vijayarangan
