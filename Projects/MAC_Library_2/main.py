# Potential Structure for the MAC Library 2.0

# Import required modules
import csv
from books import Book, RestrictedBook
from students import Student
from library import Library

def load_books(filename):
    """Load books from a CSV file."""
    books = []
    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['Restriction'].lower() == 'no':
                book = Book(row['Title'], row['Author'])
            else:
                book = RestrictedBook(row['Title'], row['Author'], row['Restricted Class'])
            books.append(book)
    return books

def load_students(filename):
    """Load students from a CSV file."""
    students = []
    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            student = Student(row['Student'], row['Restricted Class'] if row['Restricted Class'] else None)
            students.append(student)
    return students

def main():
    """Main function of the program."""
    # Load books and students from CSV files
    books = load_books('books.csv')
    students = load_students('students.csv')

    # Create a library and add books and students to it
    library = Library()
    for book in books:
        library.add_book(book)
    for student in students:
        library.add_student(student)

    # Start of the program
    print("Welcome to the Magical Academy for Cats Library Management System!")
    student_name = input("Please enter your name: ")
    library.library_menu(student_name)

if __name__ == '__main__':
    main()
