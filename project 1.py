import json
import os

FILE_NAME = '../../AppData/Roaming/JetBrains/PyCharm2025.1/scratches/projects TPWITS/students.json'


# Load student data from file
def load_data():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, 'r') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []


# Save student data to file
def save_data(data):
    with open(FILE_NAME, 'w') as file:
        json.dump(data, file, indent=2)


# Add a new student
def add_student():
    name = input('Enter name: ')
    roll = input('Enter roll number: ')
    class_name = input('Enter class: ')
    marks_input = input('Enter marks: ')

    try:
        marks = float(marks_input)
    except ValueError:
        print('Invalid marks! Please enter a number.\n')
        return

    student = {'name': name, 'roll': roll, 'class': class_name, 'marks': marks}
    data = load_data()
    data.append(student)
    save_data(data)
    print('Student added successfully!\n')


# Display all students
def display_students():
    data = load_data()
    if not data:
        print('No student records found.\n')
    else:
        print('\nAll Student Records:\n')
        for i, student in enumerate(data, 1):
            print(
                f"{i}. {student['name']} | Roll: {student['roll']} | Class: {student['class']} | Marks: {student['marks']}")
        print()


# Search for a student by roll number
def search_student():
    roll = input('Enter roll number to search: ')
    data = load_data()
    for student in data:
        if student['roll'] == roll:
            print('\nStudent Found:')
            print(f"Name: {student['name']}")
            print(f"Roll Number: {student['roll']}")
            print(f"Class: {student['class']}")
            print(f"Marks: {student['marks']}\n")
            return
    print('Student not found.\n')


# Update student record by roll number
def update_student():
    roll = input('Enter roll number to update: ')
    data = load_data()
    for student in data:
        if student['roll'] == roll:
            student['name'] = input('Enter new name: ')
            student['class'] = input('Enter new class: ')
            marks_input = input('Enter new marks: ')
            try:
                student['marks'] = float(marks_input)
            except ValueError:
                print('Invalid marks!\n')
                return
            save_data(data)
            print('Student record updated successfully!\n')
            return
    print('Student not found.\n')


# Delete student by roll number
def delete_student():
    roll = input('Enter roll number to delete: ')
    data = load_data()
    for i, student in enumerate(data):
        if student['roll'] == roll:
            del data[i]
            save_data(data)
            print('Student record deleted successfully!\n')
            return
    print('Student not found.\n')


# Main menu
def main_menu():
    while True:
        print('''
========== Student Management System ==========
1. Add Student
2. Display All Students
3. Search Student by Roll Number
4. Update Student
5. Delete Student
6. Exit
        ''')
        choice = input('Enter your choice (1-6): ')
        if choice == '1':
            add_student()
        elif choice == '2':
            display_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            update_student()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            print('Exiting the program. Goodbye!')
            break
        else:
            print('Invalid choice. Please try again.\n')


# Run the program
main_menu()
