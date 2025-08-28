# Program-ID   : student_system.py
# Author       : Muhaimin Bin Mahadi & Topa & Arsad bin ckjbsa
# OS           : Windows 11
# Interpreter  : Python 3.12
# Note         : Student Information Management System (SIMS) for adding, viewing, searching, and reporting student details.

import os

# File names
student_file = "studentsdetails.txt"
report_file = "studentReport.txt"

# Function to add student details
def add_student():
    print("\n--- Enter Student Details ---")
    student_id = input("Enter Student ID: ")
    fname = input("Enter First Name: ")
    sname = input("Enter Surname: ")
    dob = input("Enter Date of Birth (dd/mm/yy): ")
    address = input("Enter Address: ")
    gender = input("Enter Gender: ")
    intake = input("Enter Intake: ")
    email = input("Enter Email: ")

    with open(student_file, "a") as f:
        f.write(f"{student_id},{fname},{sname},{dob},{address},{gender},{intake},{email}\n")

    print("✅ Student details saved successfully!\n")

# Function to view all student details
def view_students():
    print("\n--- All Student Details ---")
    if not os.path.exists(student_file):
        print("⚠ No records found.\n")
        return

    with open(student_file, "r") as f:
        for line in f:
            data = line.strip().split(",")
            print(f"ID: {data[0]}, Name: {data[1]} {data[2]}, DOB: {data[3]}, Address: {data[4]}, Gender: {data[5]}, Intake: {data[6]}, Email: {data[7]}")
    print()

# Function to search by ID
def search_student():
    print("\n--- Search Student By ID ---")
    search_id = input("Enter Student ID: ")

    if not os.path.exists(student_file):
        print("⚠ No records found.\n")
        return

    found = False
    with open(student_file, "r") as f:
        for line in f:
            data = line.strip().split(",")
            if data[0] == search_id:
                print(f"✅ Student Found: ID: {data[0]}, Name: {data[1]} {data[2]}, DOB: {data[3]}, Address: {data[4]}, Gender: {data[5]}, Intake: {data[6]}, Email: {data[7]}")
                found = True
                break

    if not found:
        print("❌ Student not found.\n")

# Function to produce report
def produce_report():
    print("\n--- Generating Student Report ---")
    if not os.path.exists(student_file):
        print("⚠ No records found.\n")
        return

    with open(student_file, "r") as f_in, open(report_file, "w") as f_out:
        f_out.write("STUDENT REPORT\n")
        f_out.write("====================\n\n")
        for line in f_in:
            data = line.strip().split(",")
            f_out.write(f"ID: {data[0]}\nName: {data[1]} {data[2]}\nDOB: {data[3]}\nAddress: {data[4]}\nGender: {data[5]}\nIntake: {data[6]}\nEmail: {data[7]}\n\n")

    print(f"✅ Report generated successfully as {report_file}\n")

# Function to clear screen
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# Main Menu
def main_menu():
    while True:
        print("===== Student Information Management System (SIMS) =====")
        print("A. Enter Student Details")
        print("B. View All Student Details")
        print("C. Search By ID")
        print("D. Produce Report")
        print("E. Quit / Logout")
        choice = input("Choose an option (A-E): ").upper()

        if choice == "A":
            add_student()
        elif choice == "B":
            view_students()
        elif choice == "C":
            search_student()
        elif choice == "D":
            produce_report()
        elif choice == "E":
            clear_screen()
            print("👋 Logged out. Returning to Main Menu...\n")
            break
        else:
            print("⚠ Invalid option! Please choose A-E.\n")

# Run the program
if __name__ == "__main__":
    main_menu()
