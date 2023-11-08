# Potential Structure for the MAC Library 2.0

# Import required modules
import csv
import books
import library

def main():
    mac_library = library.Library()  # Create an instance of the Library class
    mac_library.load_books('books.csv')  # Load books
    mac_library.load_students('students.csv')  # Load students

    student_name = input("Please enter your name: ")  # Get student name

    if student_name not in mac_library.students:
        print("You are not registered.")
        return
    
    mac_library.current_student = student_name  # Set the current student

    mac_library.library_menu()  # Call the instance method, not the class method


if __name__ == '__main__':
    main()
