import csv
from books import Book, RestrictedBook
from students import load_students

class Library:
    def __init__(self):
        self.books = {}  # Dictionary to store books in the library
        self.students = {}  # Dictionary to store students in the library

    def library_menu(self):
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
                self.see_checked_out_books()
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

    def load_books(self, filename):
        with open(filename, 'r') as file:  # Open the CSV file with book information
            books_reader = csv.reader(file)  # Create a reader for the CSV file
            next(books_reader)  # Skip the header row
            for row in books_reader:  # For each row in the CSV file...
                title, author, restriction, restricted_class = row  # ...unpack the row into variables
                if restriction.lower() == 'yes':  # If the book is restricted...
                    # ...add it as a RestrictedBook, with the restricted class(es)
                    self.add_book(RestrictedBook(title, author, restricted_class.split(',')))
                else:
                    # If the book is not restricted, add it as a regular Book
                    self.add_book(Book(title, author, restriction, restricted_class))

    def load_students(self, filename):
        self.students = load_students(filename)

    def check_out_book(self):
        # Display available books
        print("Available books:")
        for book in self.books.keys():
            print(book)

        # Ask for the book title to check out
        book_title = input("Enter the title of the book you want to check out: ")

        if book_title not in self.books:
            print("Sorry, we don't have that book.")
            return

        # Update the student's records
        self.students[student_name].books_checked_out[book_title] = 0  # Adding book to student's checked_out_books and setting current page to 0

        # Remove book from the library
        del self.books[book_title]

        # Update the books.csv file
        self.update_books_csv()

    def update_books_csv(self):
        with open('books.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["title", "author", "restriction", "restricted_class"])  # Write the header
            for book in self.books.values():
                if isinstance(book, RestrictedBook):
                    writer.writerow([book.title, book.author, 'yes', ','.join(book.restricted_class)])
                else:
                    writer.writerow([book.title, book.author, 'no', ''])