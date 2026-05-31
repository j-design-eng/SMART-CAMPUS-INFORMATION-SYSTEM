import os
import csv
import pandas as pd
import matplotlib.pyplot as plt

students = {}

# Student Registration
def register_student():
    usn = input("Enter USN: ")
    name = input("Enter Name: ")
    marks = float(input("Enter Marks: "))

    students[usn] = {
        "Name": name,
        "Marks": marks,
        "Grade": calculate_grade(marks)
    }

    print("Student Registered Successfully!")

# Grade Calculation
def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    else:
        return "F"

# Course Enrollment
def enroll_course():
    usn = input("Enter USN: ")

    if usn in students:
        course = input("Enter Course Name: ")
        students[usn]["Course"] = course
        print("Course Enrolled Successfully!")
    else:
        print("Student Not Found!")

# Display Records
def display_students():
    if not students:
        print("No Records Available!")
        return

    print("\n----- Student Records -----")

    for usn, details in students.items():
        print("USN:", usn)
        print("Name:", details["Name"])
        print("Marks:", details["Marks"])
        print("Grade:", details["Grade"])
        print("Course:", details.get("Course", "Not Enrolled"))
        print("-" * 30)

# Search Student
def search_student():
    usn = input("Enter USN to Search: ")

    if usn in students:
        print(students[usn])
    else:
        print("Student Not Found!")

# Sort Students
def sort_students():
    sorted_data = sorted(
        students.items(),
        key=lambda x: x[1]["Marks"],
        reverse=True
    )

    print("\nStudents Sorted by Marks")

    for usn, data in sorted_data:
        print(usn, data["Name"], data["Marks"])

# Fee Calculation
def calculate_fee():
    tuition_fee = 50000
    lab_fee = 5000
    library_fee = 2000

    total_fee = tuition_fee + lab_fee + library_fee

    print("Total Fee =", total_fee)

# Save Records
def save_records():
    try:
        with open("students.csv", "w", newline="") as file:
            writer = csv.writer(file)

            writer.writerow(
                ["USN", "Name", "Marks", "Grade", "Course"]
            )

            for usn, details in students.items():
                writer.writerow([
                    usn,
                    details["Name"],
                    details["Marks"],
                    details["Grade"],
                    details.get("Course", "")
                ])

        print("Records Saved Successfully!")

    except Exception as e:
        print("Error:", e)

# Read Records
def read_records():
    try:
        with open("students.csv", "r") as file:
            print(file.read())

    except FileNotFoundError:
        print("File Not Found!")

# Directory Scan
def scan_directory():
    try:
        path = "."
        files = os.listdir(path)

        print("\nFiles in Directory:")
        for file in files:
            print(file)

    except Exception as e:
        print("Directory Error:", e)

# Performance Analytics
def performance_analysis():
    if len(students) == 0:
        print("No Student Data Available!")
        return

    data = {
        "USN": list(students.keys()),
        "Marks": [students[s]["Marks"] for s in students]
    }

    df = pd.DataFrame(data)

    print("\nStatistics")
    print(df.describe())

    plt.figure(figsize=(8,5))
    plt.bar(df["USN"], df["Marks"])
    plt.title("Student Performance Analysis")
    plt.xlabel("USN")
    plt.ylabel("Marks")
    plt.grid(True)
    plt.show()

# Main Menu
while True:

    print("\nSMART CAMPUS INFORMATION SYSTEM")
    print("1. Register Student")
    print("2. Course Enrollment")
    print("3. Display Students")
    print("4. Search Student")
    print("5. Sort Students")
    print("6. Calculate Fee")
    print("7. Save Records")
    print("8. Read Records")
    print("9. Scan Directory")
    print("10. Performance Analysis")
    print("11. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        register_student()

    elif choice == "2":
        enroll_course()

    elif choice == "3":
        display_students()

    elif choice == "4":
        search_student()

    elif choice == "5":
        sort_students()

    elif choice == "6":
        calculate_fee()

    elif choice == "7":
        save_records()

    elif choice == "8":
        read_records()

    elif choice == "9":
        scan_directory()

    elif choice == "10":
        performance_analysis()

    elif choice == "11":
        print("Thank You")
        break

    else:
        print("Invalid Choice")
