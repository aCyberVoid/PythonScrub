import csv
import random

from books import Book, RestrictedBook
from students import load_students

class Library:
    def __init__(self):
        self.books = {}  # Dictionary to store books in the library
        self.students = {}  # Dictionary to store students in the library
        self.current_student = None # The current student using the library program

    def library_menu(self): # Library menu
        while True:
            choice = input(
                "1. Check out a book\n"
                "2. Return a book\n"
                "3. See checked out books\n"
                "4. See current page of a book\n"
                "5. Exit\n"
                "Enter choice: "
            )

            if choice == '1':
                self.check_out_book()
            elif choice == '2':
                self.return_book()
            elif choice == '3':
                self.display_checked_out_books()
            elif choice == '4':
                self.see_current_page()
            elif choice == '5':
                break
            else:
                print("Invalid option. Please try again.")

    def add_book(self, book):
        self.books[book.title] = book  # Adds a new book to the library

    def add_student(self, student):
        self.students[student.name] = student  # Adds a new student to the library

    def load_students(self, filename): # 
        self.students = load_students(filename)  # Load students from a CSV file

    def load_books(self, filename): # Load books from a CSV file
        try: # Try to open the file - exception handling
            with open(filename, 'r') as file: # Open the file
                books_reader = csv.reader(file) # Create books_reader object
                next(books_reader) # Skip the header row
                for row in books_reader: # Iterate over the rows
                    title = row[0] # Get the title
                    author = row[1] # Get the author
                    restriction = row[2] # Get the restriction
                    restricted_class = row[3] if len(row) >= 4 else None # Get the restricted class
                    checked_out_by = row[4] if len(row) >= 5 and row[4] else None
            
                    if restriction.lower() == 'yes': # Check if the book is restricted
                        book = RestrictedBook(title, author, restricted_class) # Create a RestrictedBook object
                    else:
                        book = Book(title, author) # Create a Book object
            
                    book.checked_out_by = checked_out_by # Set the checked out by attribute
                    self.add_book(book) # Add the book to the library catalogue [books.csv]
        except FileNotFoundError: # Catch the FileNotFoundError exception
            print(f"Error: File '{filename}' not found.") # Print an error message

    def update_books_csv(self):
        with open('books.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["title", "author", "restriction", "restricted_class", "checked_out_by", "current_page"])  # Update the header
            for book in self.books.values():
                print(f"Book: {book.title}, Checked out by: {book.checked_out_by}")  # Debug print statement
                if isinstance(book, RestrictedBook):
                    writer.writerow([book.title, book.author, 'yes', ','.join(book.restricted_class), book.checked_out_by, book.current_page]) # Write the row to the file
                else:
                    writer.writerow([book.title, book.author, 'no', '', book.checked_out_by, book.current_page]) # Write the row to the file

# =========================================================================
# This section of the code focuses on the menu options from library_menu()
# =========================================================================

    def check_out_book(self): # Check out a book
        print("\nAvailable books:") # Print the available books
        for book in self.books.keys(): # Iterate over the books
            print(book) # Print the book
    
        book_title = input("Enter the title of the book you wish to check out: ") # Get the book title

        if book_title not in self.books: # Check if the book exists
            print("Sorry, that book doesn't exist in our library.\n") # Print an error message
            return 

        if self.books[book_title].checked_out_by is not None: # Check if the book is checked out
            print("Sorry, that book is already checked out.\n") # Print an error message
            return

        self.books[book_title].checked_out_by = self.current_student # Set the checked out by attribute
        self.update_books_csv() # Update the books.csv file
        print(f"Successfully checked out {book_title}.\n") # Print a success message


    def display_checked_out_books(self): # Display the checked out books
        checked_out_books = [book.title for book in self.books.values() if book.checked_out_by == self.current_student] # Get checked out books
        print(f"Books checked out by {self.current_student}: {', '.join(checked_out_books)}\n") # Print the checked out books
                             

    def return_book(self): # Return a book
        book_title = input("Enter the title of the book you wish to return: ") # Get the book title

        if book_title not in self.books: # Check if the book exists
            print("Sorry, that book doesn't exist in our library.") # Print an error message
            return

        if self.books[book_title].checked_out_by is None: # Check if the book is checked out
            print(f"The book {book_title} is already returned.") # Print an error message
            return

        if self.books[book_title].checked_out_by != self.current_student: # Check if the book is checked out by the current student
            print(f"You don't have {book_title} checked out.") # Print an error message
            return

        self.books[book_title].checked_out_by = None # Set the checked out by attribute to None
        self.update_books_csv() # Update the books.csv file
        print(f"Successfully returned {book_title}.") # Print a success message


    def see_current_page(self):
        book_title = input("Enter the title of the book: ")

        if book_title not in self.books:
            print("Sorry, that book doesn't exist in our library.")
            return

        if self.books[book_title].checked_out_by != self.current_student:
            print("You haven't checked out this book.")
            return

        current_page = self.books[book_title].current_page
        if current_page is None:
            current_page = 5
            self.books[book_title].current_page = current_page
            self.update_books_csv()

        print(f"Current page of {book_title}: {current_page}")
