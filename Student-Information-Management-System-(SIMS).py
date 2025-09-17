# Program-ID   : Student-Information-Management-System-(SIMS).py
# Author       : Muhaimin  & Topa & Arsad 
# OS           : Windows 11
# Interpreter  : Python 3.12
# Note         : Student Information Management System (SIMS) for adding, viewing, searching, and reporting student details.

import os

# File names
student_file = "studentsdetails.txt"
report_file = "studentReport.txt"

# Function to detect empty input
def get_non_empty_input(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty. Please try again.")


# Function to add student details
def add_student():
    print("\n--- Enter Student Details ---")
    student_id = get_non_empty_input("Enter Student ID: ")
    fname = get_non_empty_input("Enter First Name: ")
    sname = get_non_empty_input("Enter Surname: ")
    dob = get_non_empty_input("Enter Date of Birth (dd/mm/yyyy): ")
    address = get_non_empty_input("Enter Address: ")
    gender = get_non_empty_input("Enter Gender: ")
    intake = get_non_empty_input("Enter Intake: ")
    email = get_non_empty_input("Enter Email: ")


    with open(student_file, "a") as f:
        
        f.write(f"{student_id}|{fname}|{sname}|{dob}|{address}|{gender}|{intake}|{email}\n") #instead of seperate it using  comma, we use pipe

    print("✅ Student details saved successfully!\n")

# Function to view all student details (TABLE FORMAT)
def view_students():
    print("\n--- All Student Details ---")
    if not os.path.exists(student_file):
        print("⚠ No records found.\n")
        return

    # Header
    print("="*140)
    print(f"{'ID':<15}{'Name':<30}{'DOB':<12}{'Address':<50}{'Gender':<10}{'Intake':<12}{'Email':<25}")
    print("="*140)

    # Data
    with open(student_file, "r") as f:
        for line in f:
            data = line.strip().split("|")
            if len(data) < 8:  # Skip incomplete records
                continue
            else:
                student_id, fname, sname, dob, address, gender, intake, email = data
                full_name = f"{fname} {sname}"
                print(f"{student_id:<15}{full_name:<30}{dob:<12}{address:<50}{gender:<10}{intake:<12}{email:<25}")

    print("="*140 + "\n")

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
            data = line.strip().split("|")
            if len(data) < 8:
                continue
            if data[0] == search_id:
                print("\n✅ Student Found!")
                print("-"*50)
                print(f"ID      : {data[0]}")
                print(f"Name    : {data[1]} {data[2]}")
                print(f"DOB     : {data[3]}")
                print(f"Address : {data[4]}")
                print(f"Gender  : {data[5]}")
                print(f"Intake  : {data[6]}")
                print(f"Email   : {data[7]}")
                print("-"*50)
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
        f_out.write("===== STUDENT REPORT =====\n\n")
        f_out.write(f"{'ID':<15}{'Name':<30}{'DOB':<12}{'Address':<50}{'Gender':<10}{'Intake':<12}{'Email':<25}\n")
        f_out.write("="*140 + "\n")
        for line in f_in:
            data = line.strip().split("|")
            if len(data) < 8:
                continue
            student_id, fname, sname, dob, address, gender, intake, email = data
            full_name = f"{fname} {sname}"
            f_out.write(f"{student_id:<15}{full_name:<30}{dob:<12}{address:<50}{gender:<10}{intake:<12}{email:<25}\n")

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
            print("👋 Logged out.\n")
            break
        else:
            print("⚠ Invalid option! Please choose A-E.\n")

# Run the program
if __name__ == "__main__":
    main_menu()