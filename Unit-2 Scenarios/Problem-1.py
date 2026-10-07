import csv
import argparse

# Create argument parser
parser = argparse.ArgumentParser()
parser.add_argument("--file", required=True)

args = parser.parse_args()

# Read student records from CSV file
with open(args.file, "r") as file:
    reader = csv.DictReader(file)
    students = list(reader)

# Display all student records
print("Student Records:")
for student in students:
    print(student)

# Search for a student using Roll Number
roll_no = input("\nEnter Roll Number to search: ")

print("\nSearch Result:")
found = False

for student in students:
    if student["Roll Number"] == roll_no:
        print("Roll Number:", student["Roll Number"])
        print("Name:", student["Name"])
        print("Age:", student["Age"])
        print("Course:", student["Course"])
        found = True
        break

if not found:
    print("Student not found.")


# students.csv:
# Roll Number,Name,Age,Course
# 101,Amit,20,CSE
# 102,Neha,19,IT
# 103,Rahul,21,CSE
# 104,Priya,20,ENTC


# COMMAND:
# python student.py --file students.csv


# OUTPUT:
# Student Records:
# {'Roll Number': '101', 'Name': 'Amit', 'Age': '20', 'Course': 'CSE'}
# {'Roll Number': '102', 'Name': 'Neha', 'Age': '19', 'Course': 'IT'}
# {'Roll Number': '103', 'Name': 'Rahul', 'Age': '21', 'Course': 'CSE'}
# {'Roll Number': '104', 'Name': 'Priya', 'Age': '20', 'Course': 'ENTC'}
#
# Enter Roll Number to search: 103
#
# Search Result:
# Roll Number: 103
# Name: Rahul
# Age: 21
# Course: CSE
