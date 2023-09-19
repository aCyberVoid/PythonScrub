# Potential Structure for the MAC Library 2.0

# Import required modules
import csv

from books import Book, RestrictedBook
from library import Library

def main():
    library = Library()  # Create an instance of the Library class
    library.load_books('books.csv')  # Load books
    library.load_students('students.csv')  # Load students

    student_name = input("Please enter your name: ")  # Get student name

    if student_name not in library.students:
        print("You are not registered.")
        return
    
    library.current_student = student_name  # Set the current student

    library.library_menu()  # Call the instance method, not the class method


if __name__ == '__main__':
    main()
