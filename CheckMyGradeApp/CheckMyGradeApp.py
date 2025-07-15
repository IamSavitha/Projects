import csv
import random
import string
import time
from datetime import datetime
import shutil
import statistics
class Login:
    def __init__(self, email_address, password, role):
        self.email = email_address
        self.password = password
        self.role = role
  #email_id, password, role
    def encrypt_password(self, password):
        """Simple password 'encryption' (for demonstration only - VERY INSECURE)."""
        # Example: Reverse the password
        return password[::-1]


    def login(self, filename="login.csv"):
        """Compares the entered password with the encrypted password from the file."""
        try:
            with open(filename, 'r', newline='') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    if len(row) == 3 and row[0] == self.email:
                        stored_email, stored_encrypted_password, role = row
                        entered_encrypted_password = self.encrypt_password(self.password)
                        if entered_encrypted_password == stored_encrypted_password and stored_email == self.email:
                            print("Login successful!")
                            self.role = role
                            return True
                print("Invalid credentials")
                return False
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")
            return False
        except Exception as e:
            print(f"An error occurred: {e}")
            return False
                

    def logout(self):
        print("Logged out successfully")
        main_menu()

    def change_password(self):
        new_password = input("Enter new password: ")
        self.password = self.encrypt_password(new_password)
        print("Password changed successfully")

   # def encrypt_password(self, password):
    #    return ''.join(chr(ord(c) + 1) for c in password)

    def decrypt_password(self, encrypted):
        return ''.join(chr(ord(c) - 1) for c in encrypted)

    def signup(self):
        email_address = input("Enter your email address: ")
        password = input("Enter your password: ")
        role = input("Enter your role (student/professor/admin): ").lower()

        # Basic role validation
        if role not in ['student', 'professor', 'admin']:
            print("Invalid role. Please choose student, professor, or admin.")
            return False

        # Encrypt the password
        encrypted_password = self.encrypt_password(password)

        # Store the signup information in login.csv
        with open("login.csv", "a", newline='') as file:
            writer = csv.writer(file)
            writer.writerow([email_address, encrypted_password, role])

        print("Signup successful!")
        return True

class Admin:
    def __init__(self):
        self.student_id = self.generate_student_id()
        self.professor_id = self.generate_professor_id()
        self.course_id = self.generate_course_id()

    def generate_professor_id(self):
        return ''.join([str(random.randint(0, 9)) for _ in range(10)])

    def generate_student_id(self):
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for _ in range(10))

    def generate_course_id(self):
        digit = ''.join([str(random.randint(0,3)) for _ in range(3)])
        return "DATA" + digit

    def add_student(self):
        first_name = input("Enter the student First name: ")
        last_name = input("Enter the student Last name: ")
        email_address = input("Enter the email_address: ")
        
        with open("students.csv", "a", newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.student_id, email_address, first_name, last_name])

        print("Student added successfully")

        self.student_id = self.generate_student_id()
        choice = input("do you want to add student score ? yes/no ")
        if choice.lower() == "yes":
            Admin.add_student_score(self.student_id)
        else:
            return

    def add_student_score(self):
        student_id = self.student_id
        course_id = input("Enter the course id: ")
        mark = input("Enter the mark: ")
        grades = Grade.compute_grade(mark)
        with open("student_score.csv", "a", newline='') as file:
            writer = csv.writer(file)
            writer.writerow([student_id, course_id.upper(), grades, mark])
        print("Student score added successfully")

    def add_professor(self):
        professor_name = input("Enter the professor name: ")
        professor_id = self.professor_id
        rank = input("Enter the rank: ")
        course_id = input("Enter the course id: ")
        email_address = input("Enter the email_address: ")
        with open("professor.csv", "a", newline='') as file:
            writer = csv.writer(file)
            writer.writerow([professor_id, professor_name, rank, email_address, course_id.upper()])
        print("Professor added successfully")

    def add_course(self):
        course_name = input("Enter the course name: ")
        course_id = self.course_id
        credits = input("Enter the credits: ")
        description = input("Enter the description: ")
        description = description if description else "No description"
        with open("course.csv", "a", newline='') as file:
            writer = csv.writer(file)
            writer.writerow([course_id.upper(), course_name, credits, description])
        print("Course added successfully")
    
        choice = input("Do you want to compute course statistics for this course ? yes/no")
        if choice.lower() == "yes":
            Statistics.compute_course_statistics(course_id.upper())
            
        

    def add_grade(self):
        grade = input("Enter the grade: ")
        marks_min = input("Enter the mark range min:")
        marks_max = input("Enter the mark range max:")
        credits = input("Enter the credits: ")
        with open("grade.csv", "a", newline='') as file:
            writer = csv.writer(file)
            writer.writerow([grade, f"{marks_min}to{marks_max}", credits])
        print("Grade added successfully")

class Student:
    def __init__(self, name, email, student_id):
        self.student_id = student_id
        self.name = name
        self.email = email

    @staticmethod
    def display_student_detail():
        student_id = input("Enter student ID: ")
        with open("students.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == student_id:
                    print(f"ID: {row[0]}, Email: {row[1]}, Name: {row[2]} {row[3]}")
                    choice = input(" Do you want to compute student statistics for this student ? yes/no")
                    if choice.lower() == "yes":
                        Statistics.compute_student_statistics(student_id)
                    return
        print("Student not found")

    @staticmethod
    def update_student_detail():
        student_id = input("Enter student ID to update: ")
        new_email = input("Enter new email: ")
        new_first_name = input("Enter new first name: ")
        new_last_name = input("Enter new last name: ")
        
        updated = False
        rows = []
        with open("students.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == student_id:
                    row = [student_id, new_email, new_first_name, new_last_name]
                    updated = True
                rows.append(row)
        
        if updated:
            with open("students.csv", "w", newline='') as file:
                writer = csv.writer(file)
                writer.writerows(rows)
            print("Student details updated successfully")
            print ("Do you want to add  student Score? yes/no")
            student_id == row[0]
            choice = input()
            if choice.lower() == "yes":
                Admin.add_student_score(student_id)
            else:
                return
        else:
            print("Student not found")

    @staticmethod
    def delete_student():
        student_id = input("Enter student ID to delete: ")
        rows = []
        deleted = False
        with open("students.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] != student_id:
                    rows.append(row)
                else:
                    deleted = True
        
        if deleted:
            with open("students.csv", "w", newline='') as file:
                writer = csv.writer(file)
                writer.writerows(rows)
            print("Student deleted successfully")
        else:
            print("Student not found")

    @staticmethod
    def search_student():
        search_term = input("Enter student name or email to search: ")
        start_time = time.time()
        found = False
        with open("students.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if search_term.lower() in row[1].lower() or search_term.lower() in row[2].lower() or search_term.lower() in row[3].lower():
                    print(f"ID: {row[0]}, Email: {row[1]}, Name: {row[2]} {row[3]}")
                    found = True
                    student_id = row[0]
                    choice = input(" Do you want to compute student statistics for this student ? yes/no")
                    if choice.lower() == "yes":
                        Statistics.compute_student_statistics(student_id)
        end_time = time.time()
        if not found:
            print("No matching students found")
        print(f"Search completed in {end_time - start_time:.4f} seconds")

    @staticmethod
    def display_all_students():
        with open("students.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                print(f"ID: {row[0]}, Email: {row[1]}, Name: {row[2]} {row[3]}")

    @staticmethod
    def generate_student_report():
        student_id = input("Enter student ID for report: ")
        with open("students.csv", "r") as file:
            reader = csv.reader(file)
            student_info = None
            for row in reader:
                if row[0] == student_id:
                    student_info = row
                    break
        
        if student_info:
            print(f"Report for Student: {student_info[2]} {student_info[3]} (ID: {student_info[0]})")
            print("Courses and Grades:")
            with open("student_score.csv", "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[0] == student_id:
                        print(f"Course: {row[1]}, Grade: {row[2]}, Mark: {row[3]}")
        else:
            print("Student not found")

class Professor:
    def __init__(self, Professor_name, email_address):
        self.Professor_name = Professor_name  
        self.email_address = email_address

    @staticmethod
    def display_professor_detail():
        professor_id = input("Enter professor ID: ")
        with open("professor.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == professor_id:
                    print(f"ID: {row[0]}, Name: {row[1]}, Rank: {row[2]}, Email: {row[3]}, Course: {row[4]}")
                    return
        print("Professor not found")

    @staticmethod
    def update_professor_detail():
        professor_id = input("Enter professor ID to update: ")

        updated = False
        rows = []
        with open("professor.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == professor_id:
                    new_name = input("Enter new name: ")
                    new_rank = input("Enter new rank: ")
                    new_email = input("Enter new email: ")
                    new_course = input("Enter new course ID: ")

                    new_name = new_name if new_name else row[1]
                    new_rank = new_rank if new_rank else row[2]
                    new_email = new_email if new_email else row[3]
                    new_course = new_course if new_course else row[4]

                    row = [professor_id, new_name, new_rank, new_email, new_course]
                    updated = True
                rows.append(row)
            else:
                print("Professor not found")
                return
        
        if updated:
            with open("professor.csv", "w", newline='') as file:
                writer = csv.writer(file)
                writer.writerows(rows)
            print("Professor details updated successfully")
        else:
            print("Professor not found")

    @staticmethod
    def delete_professor():
        professor_id = input("Enter professor ID to delete: ")
        rows = []
        deleted = False
        with open("professor.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] != professor_id:
                    rows.append(row)
                else:
                    deleted = True
        
        if deleted:
            with open("professor.csv", "w", newline='') as file:
                writer = csv.writer(file)
                writer.writerows(rows)
            print("Professor deleted successfully")
        else:
            print("Professor not found")

    @staticmethod
    def search_professor():
        search_term = input("Enter professor name or email to search: ")
        start_time = time.time()
        found = False
        with open("professor.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if search_term.lower() in row[1].lower() or search_term.lower() in row[3].lower():
                    print("Professor Found!")
                    #print(f"ID: {row[0]}, Name: {row[1]}, Rank: {row[2]}, Email: {row[3]}, Course: {row[4]}")
                    found = True
        end_time = time.time()
        if not found:
            print("No matching professors found")
        print(f"Search completed in {end_time - start_time:.4f} seconds")

    @staticmethod
    def display_all_professors():
        with open("professor.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                print(f"ID: {row[0]}, Name: {row[1]}, Rank: {row[2]}, Email: {row[3]}, Course: {row[4]}")


    @staticmethod
    def generate_professors_report():
        with open("professor.csv", "r") as file:
            reader = csv.reader(file)
            professors = list(reader)
        
        print("Professor Report:")
        for professor in professors:
            print(f"ID: {professor[0]}, Name: {professor[1]}, Rank: {professor[2]}, Email: {professor[3]}, Course: {professor[4]}")
            print("Students in their course:")
            with open("student_score.csv", "r") as score_file:
                score_reader = csv.reader(score_file)
                for score in score_reader:
                    if score[1] == professor[4]:  # If course ID matches
                        print(f"  Student ID: {score[0]}, Grade: {score[2]}, Mark: {score[3]}")
            print()

    @staticmethod
    def course_detail_by_professor():
        professor_id = input("Enter professor ID: ")
        with open("professor.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == professor_id:
                    course_id = row[4]
                    print(f"Professor {row[1]} teaches course {course_id}")
                    with open("course.csv", "r") as course_file:
                        course_reader = csv.reader(course_file)
                        for course_row in course_reader:
                            if course_row[0] == course_id.upper():
                                print(f"Course Name: {course_row[1]}")
                                print(f"Credits: {course_row[2]}")
                                print(f"Description: {course_row[3]}")
                    return
        print("Professor not found")

class Course:
    def __init__(self, course_name, course_id):
        self.course_name = course_name  
        self.course_id = course_id
        
    @staticmethod
    def display_course():
        course_id = input("Enter course ID: ")
        with open("course.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == course_id.upper():
                    print(f"ID: {row[0]}, Name: {row[1]}, Credits: {row[2]}, Description: {row[3]}")
                    return
        print("Course not found")

    @staticmethod
    def update_course():
        course_id = input("Enter course ID to update: ")      
        updated = False
        rows = []
        with open("course.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == course_id.upper():
                    new_name = input("Enter new course name: ")
                    new_credits = input("Enter new credits: ")
                    new_description = input("Enter new description: ")
                    row = [course_id, new_name, new_credits, new_description]
                    updated = True
                rows.append(row)
        
        if updated:
            with open("course.csv", "w", newline='') as file:
                writer = csv.writer(file)
                writer.writerows(rows)
            print("Course updated successfully")
        else:
            print("Course not found")
    @staticmethod
    def delete_course():
        course_id = input("Enter course ID to delete: ")
        rows = []
        deleted = False
        with open("course.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] != course_id.upper():
                    rows.append(row)
                else:
                    deleted = True
        if deleted:
            with open("course.csv", "w", newline='') as file:
                writer = csv.writer(file)
                writer.writerows(rows)
            print("Course deleted successfully")
        else:
            print("Course not found")  
    @staticmethod
    def search_course():
        search_term = input("Enter course name or ID to search: ")
        found = False
        with open("course.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if search_term.lower() in row[0].lower() or search_term.lower() in row[1].lower():
                    print(f"ID: {row[0]}, Name: {row[1]}, Credits: {row[2]}, Description: {row[3]}")
                    print("Course Found")
                    course_id = row[0]
                    choice = input("Do you want to compute course statistics for this course ? yes/no")
                    if choice.lower() == "yes":
                        Statistics.compute_course_statistics(course_id.upper())
                    found = True             
        if not found:
            print("No matching courses found")
    @staticmethod
    def display_all_courses():
        with open("course.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                print(f"ID: {row[0]}, Name: {row[1]}, Credits: {row[2]}, Description: {row[3]}")
    @staticmethod
    def generate_course_report():
        course_id = input("Enter course ID for report: ")
        with open("course.csv", "r") as file:
            reader = csv.reader(file)
            course_info = None
            for row in reader:
                if row[0] == course_id.upper():
                    course_info = row
                    break    
        if course_info:
            print(f"Report for Course: {course_info[1]} (ID: {course_info[0]})")
            print("Students Enrolled:")
            with open("student_score.csv", "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[1] == course_id.upper():
                        print(f"Student ID: {row[0]}, Grade: {row[2]}, Mark: {row[3]}")
        else:
            print("Course not found")
class Grade:
    def __init__(self): # grade, marks_range, credits
        pass    
    @staticmethod
    def compute_grade(mark):  #mark is in student score csv - and grade.csv has grades and marks range
        """Computes the grade based on the mark."""
        with open("grade.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                grade_letter = row[0]
                marks_range_str = row[1]
                
                # Extract min and max marks from the range string
                marks_min, marks_max = map(int, marks_range_str.split("to"))

                if marks_min <= mark <= marks_max:
                    return grade_letter
        return "F"  # Default grade if no match is found
    
    @staticmethod
    def display_grade():
        """Displays a specific grade based on user input."""
        grade_id = input("Enter the grade to display: ")
        with open("grade.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == grade_id:  # Assuming the first element is the grade itself
                    print(f"Grade: {row[0]}, Marks Range: {row[1]}, Credits: {row[2]}")
                    return
        print("Grade not found.")
    @staticmethod
    def update_grade():
        """Updates a specific grade based on user input."""
        grade_id = input("Enter the grade to update: ")
        new_marks_min = input("Enter the new minimum mark: ")
        new_marks_max = input("Enter the new maximum mark: ")
        new_credits = input("Enter the new credits: ")
        rows = []
        updated = False
        with open("grade.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == grade_id:
                    row = [grade_id, f"{new_marks_min}to{new_marks_max}", new_credits]
                    updated = True
                rows.append(row)

        if updated:
            with open("grade.csv", "w", newline='') as file:
                writer = csv.writer(file)
                writer.writerows(rows)
            print("Grade updated successfully.")
        else:
            print("Grade not found.")
    @staticmethod
    def delete_grade():
        """Deletes a specific grade based on user input."""
        grade_id = input("Enter the grade to delete: ")
        rows = []
        deleted = False
        with open("grade.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] != grade_id:
                    rows.append(row)
                else:
                    deleted = True
        if deleted:
            with open("grade.csv", "w", newline='') as file:
                writer = csv.writer(file)
                writer.writerows(rows)
            print("Grade deleted successfully.")
        else:
            print("Grade not found.")
    @staticmethod
    def display_all_grades():
        """Displays all grades in the grade.csv file."""
        with open("grade.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                print(f"Grade: {row[0]}, Marks Range: {row[1]}, Credits: {row[2]}")
    @staticmethod
    def generate_grade_report():
        """Generates a report of all grades."""
        print("Generating Grade Report:")
        with open("grade.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                print(f"Grade: {row[0]}, Marks Range: {row[1]}, Credits: {row[2]}")
class Statistics:
    @staticmethod
    def compute_course_statistics(course_id):
        marks = []
        with open("student_score.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[1] == course_id:
                    marks.append(float(row[3]))     
        if marks:
            mean = statistics.mean(marks)
            median = statistics.median(marks)
            mode = statistics.mode(marks)
            std_dev = statistics.stdev(marks) if len(marks) > 1 else 0
            
            print(f"Statistics for Course {course_id}:")
            print(f"Mean: {mean:.2f}")
            print(f"Median: {median:.2f}")
            print(f"Mode: {mode:.2f}")
            print(f"Standard Deviation: {std_dev:.2f}")
        else:
            print("No data available for this course")
    @staticmethod
    def compute_student_statistics(student_id):
        marks = []
        with open("student_score.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == student_id:
                    marks.append(float(row[3]))  
        if marks:
            mean = statistics.mean(marks)
            median = statistics.median(marks)
            mode = statistics.mode(marks)
            std_dev = statistics.stdev(marks) if len(marks) > 1 else 0          
            print(f"Statistics for Student {student_id}:")
            print(f"Mean: {mean:.2f}")
            print(f"Median: {median:.2f}")
            print(f"Mode: {mode:.2f}")
            print(f"Standard Deviation: {std_dev:.2f}")
        else:
            print("No data available for this student")
def main_menu():
    while True:
        columns = shutil.get_terminal_size().columns
        print("\n WELCOME TO CHECK MY GRADE APP".center(columns))
        print("1. Login")
        print("2. Signup")
        print("3. Back to main menu")
        choice = input("Enter your choice: ")
        if choice == "1":
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            role = input("Enter your role: ")
            login_obj = Login(email,password,role)  
            login_obj.login()

            if  login_obj.login():

                checkmygradeapp(role)
            else:
                print("Login failed. Please try again.")
                break

        elif choice == "2":
            Login("email","password","role").signup()
            break
        elif choice == "3":
            break
def checkmygradeapp(role):
    """Welcome to Check My Grade App"""
    while True:
        columns = shutil.get_terminal_size().columns
            #role = input("Enter your role: ")
        if role == "student":
            print("Student  management".center(columns))
            while True:
                columns = shutil.get_terminal_size().columns
                print("\n What would you like to do? ".center(columns))
                print("1. Display All Students")
                print("2. Update student")
                print("3. View student")
                print("4. Search student")
                print("5. Generate Report student")
                print("6. work on course")
                print("7. work on grades" )
                print("8. Back to main menu")
                choice = input("Enter your choice: ")
                if choice == "1":
                    Student.display_all_students()    
                elif choice == "2":
                    Student.update_student_detail()
                elif choice == "3":
                    Student.display_student_detail()
                elif choice == "4":
                    Student.search_student()
                elif choice == "5":
                    Student.generate_student_report()  
                elif choice == "6":
                    work_on_course()
                elif choice == "7":
                    work_on_grade() 
                elif choice == "8": 
                    break
        elif role == "professor":
            print("Professor management".center(columns))
            while True:
                columns = shutil.get_terminal_size().columns
                print("\n What would you like to do? ".center(columns))
                print("1. Display All Professors")
                print("2. Update Professor")
                print("3. View Professor")
                print("4. Search Professor")
                print("5. Generate Report Professor")
                print("6. Course detail by professor")
                print("7. work on course")
                print("8. Update Course") #professor
                print("9. work on grades" )
                print("10. Back to main menu")
                choice = input("Enter your choice: ")
                if choice == "1":
                    Professor.display_all_professors()
                elif choice == "2":
                    Professor.update_professor_detail()
                elif choice == "3":
                    Professor.display_professor_detail()
                elif choice == "4":
                    Professor.search_professor()
                elif choice == "5":
                    Professor.generate_professors_report()  
                elif choice == "6":
                    Professor.course_detail_by_professor()  
                elif choice == "7":
                    work_on_course()
                if choice == "8":
                    Course.update_course()
                elif choice == "9":
                    work_on_grade()  
                elif choice == "10":
                    break
        elif role == "admin":
            print("Admin Task".center(columns))
            while True:
                columns = shutil.get_terminal_size().columns
                print("\n What would you like to do? ".center(columns))
                print("1. Add Student")
                print("2. Add Professor")
                print("3. Add Grade details")
                print("4. Add course details")
                print("5. Delete Course")
                print("6. Delete Grade")
                print("7. Delete Student")
                print("8. Delete Professor")
                print("9. Back to main menu")
                choice = input("Enter your choice: ")

                if choice == "1":
                    Admin().add_student()
                elif choice == "2":
                    Admin().add_professor()
                elif choice == "3":
                    Admin().add_grade()
                elif choice == "4":
                    Admin().add_course()
                elif choice == "5":
                    Course.delete_course()
                elif choice == "6":
                    Grade().delete_grade()
                elif choice == "7":
                    Student.delete_student()
                elif choice == "8":
                    Professor.delete_professor()
                elif choice == "9":
                    break
        else:
            print("Invalid choice. Please try again.")
def work_on_course():
     while True:
        print("1. View Course") #professor #student 
        print("2. Search Course") #professor #student
        print("3. Generate Course Report") #professor #student
        print("4. Display All Courses") #professor #student
        print("5. Back to main menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            Course.display_course()
        elif choice == "2":
            Course.search_course()
        elif choice == "3":
            Course.generate_course_report()
        elif choice == "4":
            Course.display_all_courses()
        elif choice == "5":
            break
def work_on_grade():
    while True:
        print("1. Display grade")
        print("2. Update_grade ")
        print("3. Display all Grade")
        print("4. Back to main menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            grade = Grade()
            grade.display_grade()
        elif choice == "2":
            Grade().update_grade()
        elif choice == "3":
            Grade().display_all_grades()
        elif choice == "4":
            break
if __name__ == "__main__":
    main_menu()

