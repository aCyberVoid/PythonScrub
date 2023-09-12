# Title ---------- Magical Academy for Cats' Library Program
# Description ---- Library Management System

# Import the Book and Student class
import csv
from book import Book
from student import Student

# Open books.csv and read it into a list of dictionaries
with open('books.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    next(reader)  # Skip the header row
    books = []
    for row in reader:
        # Append each row as a dictionary to the books' list
        books.append({
            'Book Title': row[0],
            'Author': row[1],
            'Restriction': row[2],
            'Restricted Class': row[3]
        })

# Open students.csv and read it into a list of dictionaries
with open('students.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    next(reader)  # Skip the header row
    students = []
    for row in reader:
        # Append each row as a dictionary to the students' list
        students.append({
            'Name': row[0],
            'Restricted Class': row[1],
        })

# Create Book instances using the data from books.csv
book_objects = []
for book_data in books:
    book = Book(
        book_data['Book Title'],
        book_data['Author'],
        book_data['Restriction'],
        book_data['Restricted Class']
    )
    book_objects.append(book)

# Print the initial details of all books
print("Library Inventory:")
for book in book_objects:
    print(book)  # Print book details

# Create Student instances using the data from students.csv
student_objects = []
for student_data in students:
    student = Student(
        student_data['Name'],
        student_data['Restricted Class']
    )
    student_objects.append(student)

# Interaction with the Library
while True:
    print("\n==== Library Menu ====")
    print("1. Check out a book")
    print("2. Check in a book")
    print("3. View checked out books")
    print("4. View due dates and page numbers")
    print("5. Quit")

    choice = input("Enter your choice: ")  # Get user choice

    if choice == "1":
        # Check out a book
        print("\n--- Check Out a Book ---")
        student_name = input("Enter student name: ")  # Get student name from user
        book_title = input("Enter book title: ")  # Get book title from user

        # Find the student and book objects based on user input
        student = next((s for s in student_objects if s.name == student_name), None)
        book = next((b for b in book_objects if b.title == book_title), None)

        if student is not None and book is not None:
            student.check_out_book(book)  # Check out the book for the student
        else:
            print("Student or book not found. Please try again.")

    elif choice == "2":
        # Check in a book
        print("\n--- Check In a Book ---")
        student_name = input("Enter student name: ")  # Get student name from user
        book_title = input("Enter book title: ")  # Get book title from user

        # Find the student and book objects based on user input
        student = next((s for s in student_objects if s.name == student_name), None)
        book = next((b for b in book_objects if b.title == book_title), None)

        if student is not None and book is not None:
            student.check_in_book(book)  # Check in the book for the student
        else:
            print("Student or book not found. Please try again.")

    elif choice == "3":
        # View checked out books
        print("\n--- Checked Out Books ---")
        student_name = input("Enter student name: ")  # Get student name from user

        # Find the student object based on user input
        student = next((s for s in student_objects if s.name == student_name), None)

        if student is not None:
            print(f"{student.name} has checked out the following books:")
            for book in student.books:
                print(book)  # Print book details
        else:
            print("Student not found. Please try again.")

    elif choice == "4":
        # View due dates and page numbers
        print("\n--- Due Dates and Page Numbers ---")
        student_name = input("Enter student name: ")  # Get student name from user

        # Find the student object based on user input
        student = next((s for s in student_objects if s.name == student_name), None)

        if student is not None:
            print(f"{student.name} has the following checked out books:")
            for book in student.books:
                print(f"Book: {book.title}")
                print(f"Current Page: {book.current_page}")
                print(f"Due Date: {book.due_date}")
                print()
        else:
            print("Student not found. Please try again.")

    elif choice == "5":
        # Quit the program
        print("Exiting the Library program...")
        break

    else:
        print("Invalid choice. Please try again.")

    # Print the updated details of all books after each interaction
    print("Updated Library Inventory:")
    for book in book_objects:
        print(book)  # Print book details
