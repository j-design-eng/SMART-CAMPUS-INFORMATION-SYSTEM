
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ==========================================
# LAB 7: Custom Exceptions & Setup
# ==========================================
class MissingFileOrFolderError(Exception):
    """Raised when a required file or folder is missing."""
    pass

# Ensure we have data structures to hold runtime data
runtime_students = []  # For Lab 3 memory records

# ==========================================
# LAB 5: Fee Calculation Function
# ==========================================
def calculate_fee(tuition_fee, hostel_fee=0, transportation_fee=0):
    """Calculates total fee using optional keyword arguments."""
    total_fee=tuition_fee + hostel_fee + transportation_fee
    return total_fee

# ==========================================
# LAB 4: Sorting & Searching Algorithms
# ==========================================
def bubble_sort_ids(student_list):
    """Sorts students by ID using Bubble Sort."""
    n = len(student_list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if student_list[j]['id'] > student_list[j + 1]['id']:
                student_list[j], student_list[j + 1] = student_list[j + 1], student_list[j]
    return student_list

def binary_search_id(sorted_students, target_id):
    """Searches for a student ID using Binary Search."""
    low = 0
    high = len(sorted_students) - 1
    while low <= high:
        mid = (low + high) // 2
        if sorted_students[mid]['id'] == target_id:
            return mid
        elif sorted_students[mid]['id'] < target_id:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# ==========================================
# CORE MENU MODULES
# ==========================================


#===========LAB--01===============
#  STUDENT REGISTRATION AND GRADE EVALUATION

def module_1_registration():
    """Lab 1: Student Registration and Grade Evaluation"""
    print("\n--- [Lab 1] Student Registration & Grade Evaluation ---")
    name = input("Enter student name: ")
    while True:
        try:
            score = float(input("Enter exam score (0-100): "))
            if 0 <= score <= 100:
                break
            print("Score must be between 0 and 100.")
        except ValueError:
            print("Invalid input! Please enter a numerical score.")
            
    # Grade Evaluation Matrix
    if score >= 90:
        grade, remark = "A", "Excellent"
    elif score >= 75:
        grade, remark = "B", "Very Good"
    elif score >= 60:
        grade, remark = "C", "Good"
    elif score >= 40:
        grade, remark = "D", "Average"
    else:
        grade, remark = "F", "Needs Improvement"
        
    print("\n--- Student Report ---")
    print(f"Name: {name}\nScore: {score}\nGrade: {grade}\nPerformance Remark: {remark}")


#=============LAB--02==============
#   COURSE  ENROLLMENT  MANAGEMENT  SYSTEM

def module_2_course_enrollment():
    """Lab 2: Course Enrollment Management System"""
    print("\n--- [Lab 2] Course Enrollment Management System ---")
    courses = []
    max_courses = 5
    
    while True:
        if len(courses) >= max_courses:
            print("Maximum course limit reached!")
            break
            
        course_name = input("Enter course name (or 'done' to finish): ").strip()
        if course_name.lower() == "done":
            break
        if not course_name:
            print("Course name cannot be empty. Skipping...")
            continue
            
        credits = input("Enter credit value: ")
        if not credits.isdigit():
            print("Invalid credit value! Skipping entry...")
            continue
            
        credits = int(credits)
        if credits <= 0:
            print("Credit must be positive! Skipping entry...")
            continue
            
        courses.append((course_name, credits))
        print(f"Course '{course_name}' with {credits} credits added.\n")
        
    print("\n--- Enrollment Report ---")
    for course, credit in courses:
        print(f"Course: {course}, Credits: {credit}")
    print("Total courses enrolled:", len(courses))


#==============LAB--03=============
#   STUDENT  RECORD  DATA  MANAGEMENT  USING  DATA  STRUCTURES

def module_3_record_management():
    """Lab 3: Student Record Data Management using Lists, Dicts, & Sets"""
    print("\n--- [Lab 3] Student Record Data Management ---")
    # Adding in-memory records
    runtime_students.clear()
    runtime_students.append({"id": 105, "name": "Priya", "age": 20, "grades": [85, 90, 78]})
    runtime_students.append({"id": 102, "name": "Rahul", "age": 21, "grades": [72, 88, 91]})
    runtime_students.append({"id": 110, "name": "Anita", "age": 19, "grades": [95, 89, 92]})
    
    print("Student Records Loaded:")
    for student in runtime_students:
        print(f"ID: {student['id']} | Name: {student['name']} | Age: {student['age']} | Grades: {student['grades']}")
        
    # Set Operations for Events
    event_A = {"Priya", "Rahul", "Anita", "Kiran"}
    event_B = {"Rahul", "Anita", "Sneha"}
    
    print("\n--- Event Participation Analysis ---")
    print("Common Participants:", event_A & event_B)
    print("All Participants:", event_A | event_B)
    print("Only Event A Participants:", event_A - event_B)


#===============LAB--04====================
#      SORTING  AND  SEARCHING  OF  STUDENT  IDs

def module_4_search_sort():
    """Lab 4: Sorting and Searching of Student IDs"""
    print("\n--- [Lab 4] Sorting and Searching of Student IDs ---")
    if not runtime_students:
        print("No student records found in memory! Please run Module 3 first to populate data.")
        return
        
    print("Original Records:")
    for s in runtime_students:
        print(f"ID: {s['id']} - Name: {s['name']}")
        
    # Sort
    sorted_records = bubble_sort_ids(list(runtime_students))
    print("\nSorted Records (Bubble Sort):")
    for s in sorted_records:
        print(f"ID: {s['id']} - Name: {s['name']}")
        
    # Search
    try:
        target = int(input("\nEnter Student ID to search using Binary Search: "))
        idx = binary_search_id(sorted_records, target)
        if idx != -1:
            found = sorted_records[idx]
            print(f"Binary Search: ID {target} found! Match: {found['name']}, Age: {found['age']}")
        else:
            print("Binary Search: ID not found.")
    except ValueError:
        print("Invalid ID format.")


#=============LAB--05============
#     STUDENT  FEE  CALCULATION  USING  FUNCTION

def module_5_fee_calc():
    """Lab 5: Student Fee Calculation Menu Intermediary"""
    print("\n--- [Lab 5] Student Fee Calculation ---")
    try:
        tuition = float(input("Enter Tuition Fee: "))
        has_hostel = input("Add Hostel Fee? (y/n): ").lower() == 'y'
        hostel = float(input("Enter Hostel Fee: ")) if has_hostel else 0
        
        has_transport = input("Add Transportation Fee? (y/n): ").lower() == 'y'
        transport = float(input("Enter Transportation Fee: ")) if has_transport else 0
        
        total = calculate_fee(tuition, hostel_fee=hostel, transportation_fee=transport)
        print(f"\n>>> Total Calculated Fee: {total} <<<")
    except ValueError:
        print("Error: Please input structural numerical amounts.")


#==============LAB--06==============
#     FILE HANDLING FOR STUDENT ACADEMIC RECORDS


def module_6_file_handling():
    """Lab 6: File Handling for Student Academic Records"""
    print("\n--- [Lab 6] File Handling Management ---")
    filename = "student_records.txt"
    
    # 1. Writing records
    with open(filename, "w") as file:
        file.write("ID,Name,Marks\n")
        file.write("101,Arjun,85\n")
        file.write("102,Meera,92\n")
        file.write("103,Ravi,76\n")
        file.write("104,Anita,89\n")
    print(f"Sample data successfully saved to '{filename}'.")
    
    # 2. Reading and Parsing Records
    print("\nReading and Processing Data Report:")
    with open(filename, "r") as file:
        records = file.readlines()
        
    total_students = 0
    total_marks = 0
    highest_marks = -1
    top_student = ""
    
    print(records[0].strip())  # Header print
    for record in records[1:]:
        line = record.strip()
        print(line)
        parts = line.split(",")
        name = parts[1]
        marks = int(parts[2])
        
        total_students += 1
        total_marks += marks
        if marks > highest_marks:
            highest_marks = marks
            top_student = name
            
    avg_marks = total_marks / total_students
    print("\n--- Derived File Report ---")
    print(f"Total Students processed: {total_students}")
    print(f"Average System Marks: {avg_marks:.2f}")
    print(f"Top Performer: {top_student} ({highest_marks} Marks)")


#=============LAB--07=============
#      DIRECTORY SCANNING WITH EXCEPTION HANDLING

def module_7_directory_scan():
    """Lab 7: Directory Scanning with Exception Handling"""
    print("\n--- [Lab 7] Directory Scanning Structure ---")
    path = input("Enter the directory path to scan (or hit enter for current directory '.'): ").strip()
    if not path:
        path = "."
        
    try:
        if not os.path.exists(path):
            raise FileNotFoundError(f"Invalid directory path: {path}")
            
        print(f"\nScanning structural directory: {path}\n")
        for root, dirs, files in os.walk(path):
            level = root.replace(path, "").count(os.sep)
            indent = " " * 4 * level
            print(f"{indent}{os.path.basename(root)}/")
            sub_indent = " " * 4 * (level + 1)
            for f in files:
                print(f"{sub_indent}{f}")
                
            if not files and not dirs:
                raise MissingFileOrFolderError(f"Empty folder structural anomaly detected: {root}")
                
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except MissingFileOrFolderError as e:
        print(f"Custom Project Error: {e}")
    except Exception as e:
        print(f"Unexpected operational error: {e}")

#==============LAB--08=============
#      STUDENT PERFORMANCE ANALYSIS USING NumPy,Pandas,Matplotlib


def module_8_data_analytics():
    """Lab 8: Student Performance Analysis using NumPy, Pandas, Matplotlib"""
    print("\n--- [Lab 8] Data Analytics System Engine ---")
    csv_filename = "student_performance.csv"
    
    # Let's dynamically construct a mockup CSV file for execution safety if it doesn't exist
    if not os.path.exists(csv_filename):
        mock_data = {
            "Name": ["Arjun", "Meera", "Ravi", "Anita", "Priya"],
            "Math": [85, 92, 76, 89, 95],
            "Science": [78, 88, 82, 91, 89],
            "English": [90, 85, 80, 94, 88]
        }
        pd.DataFrame(mock_data).to_csv(csv_filename, index=False)
        print(f"Generated a sample '{csv_filename}' file for analysis.")

    try:
        df = pd.read_csv(csv_filename)
        print("\n--- Raw Data (Head) ---")
        print(df.head())
        
        print("\n--- Pandas Statistical Summary ---")
        print(df.describe())
        
        # NumPy computation
        scores = df[["Math", "Science", "English"]].to_numpy()
        mean_scores = np.mean(scores, axis=0)
        median_scores = np.median(scores, axis=0)
        std_dev_scores = np.std(scores, axis=0)
        
        print("\n--- NumPy Advanced Matrix Analysis ---")
        print(f"Mean Scores (Math, Science, English): {mean_scores}")
        print(f"Median Scores (Math, Science, English): {median_scores}")
        print(f"Standard Deviations: {std_dev_scores}")
        
        # Max performers
        print("\n--- Subject Top Performers ---")
        print(f"Math: {df.loc[df['Math'].idxmax(), 'Name']}")
        print(f"Science: {df.loc[df['Science'].idxmax(), 'Name']}")
        print(f"English: {df.loc[df['English'].idxmax(), 'Name']}")
        
        # Rendering Chart 1
        subjects = ["Math", "Science", "English"]
        plt.figure(figsize=(10, 4))
        plt.subplot(1, 2, 1)
        plt.bar(subjects, mean_scores, color=["blue", "green", "orange"])
        plt.title("Average Scores per Subject")
        plt.ylabel("Average Score")
        
        # Rendering Chart 2
        plt.subplot(1, 2, 2)
        for sub in subjects:
            plt.plot(df["Name"], df[sub], marker='o', label=sub)
        plt.title("Student Comparison Chart")
        plt.legend()
        
        plt.tight_layout()
        print("\nDisplaying Matplotlib Visual Analytics Charts...")
        plt.show()
        
    except FileNotFoundError:
        print("Error: The performance CSV dataset file was not located.")
    except Exception as e:
        print(f"Unexpected Analytic Error: {e}")

# ==========================================
# MAIN SYSTEM APPLICATION DASHBOARD
# ==========================================
def main_dashboard():
    """Integrated Main System Application Dashboard."""
    while True:
        print("\n" + "="*50)
        print("  SMART CAMPUS INFORMATION SYSTEM MAIN DASHBOARD  ")
        print("="*50)
        print("1. Student Registration & Grade Evaluation (Lab 1)")
        print("2. Course Enrollment Management (Lab 2)")
        print("3. Student Record Storage & Management (Lab 3)")
        print("4. Searching and Sorting Student IDs (Lab 4)")
        print("5. Fee Calculation Using Functions (Lab 5)")
        print("6. File-Based Academic Record Management (Lab 6)")
        print("7. Directory Scanning with Exception Handling (Lab 7)")
        print("8. Student Performance Analytics [NumPy/Pandas] (Lab 8)")
        print("9. EXIT System Application")
        print("="*50)
        
        choice = input("Select a functional module component (1-9): ").strip()
        
        if choice == "1":
            module_1_registration()
        elif choice == "2":
            module_2_course_enrollment()
        elif choice == "3":
            module_3_record_management()
        elif choice == "4":
            module_4_search_sort()
        elif choice == "5":
            module_5_fee_calc()
        elif choice == "6":
            module_6_file_handling()
        elif choice == "7":
            module_7_directory_scan()
        elif choice == "8":
            module_8_data_analytics()
        elif choice == "9":
            print("\nShutting down Smart Campus Dashboard... Goodbye!")
            break
        else:
            print("Invalid Selection! Please specify an option between 1 and 9.")

if __name__ == "__main__":
    main_dashboard()
