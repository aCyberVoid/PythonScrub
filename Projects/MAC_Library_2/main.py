# Potential Structure for the MAC Library 2.0

# Import required modules
import csv
import books
import students
from library import Library  # Assuming Library is a class you want to use directly

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

def main():
    """Main function of the program."""
    # Load books and students from CSV files
    loaded_books = books.load_books('books.csv')  # Qualified with module name
    loaded_students = students.load_students('students.csv')  # Qualified with module name

    # Create a library and add books and students to it
    library_instance = Library()  # Renamed to avoid name clash with library module
    for book in loaded_books:
        library_instance.add_book(book)
    for student in loaded_students:
        library_instance.add_student(student)

    # Start of the program
    print("Welcome to the Magical Academy for Cats Library Management System!")
    student_name = input("Please enter your name: ")
    library_instance.library_menu(student_name)  # Qualified with instance name

if __name__ == '__main__':
    main()
