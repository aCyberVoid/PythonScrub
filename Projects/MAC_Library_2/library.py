import csv
from books import Book, RestrictedBook
from students import load_students

class Library:
    def __init__(self):
        self.books = {}  # Dictionary to store books in the library
        self.students = {}  # Dictionary to store students in the library
        self.current_student = None  # The current student using the library program

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
    
    def load_books(self, filename):
        """Load books from a CSV file."""
        books = []
        with open(filename, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['restriction'] == 'no':
                    book = Book(row['title'], row['author'], row['checked_out_by'])
                else:
                    book = RestrictedBook(row['title'], row['author'], row['restricted_class'], row['checked_out_by'])
                books.append(book)
        self.books = books

#    def load_books(self, filename):
#         with open(filename, 'r') as file:  # Open the CSV file with book information
#             books_reader = csv.reader(file)  # Create a reader for the CSV file
#             next(books_reader)  # Skip the header row
#             for row in books_reader:
#                 print(f"\nRow data: {row}") # - TESTING to view books.csv data
#                 if len(row) == 5:
#                     title, author, restriction, restricted_class, checked_out_by = row
#                 elif len(row) == 4:
#                     title, author, restriction, restricted_class = row
#                     checked_out_by = None
#                 else:
#                     print(f"\nSkipping row due to unexpected number of columns: {row}")
#                     continue

    def load_students(self, filename):
        self.students = load_students(filename)

    def check_out_book(self):
        # Display available books
        print("\nAvailable books:")
        for book in self.books.keys():
            print(book)

        # Ask for the book title to check out
        book_title = input("\nEnter the title of the book you want to check out: ")

        if book_title not in self.books:
            print("\nSorry, we don't have that book.")
            return

        # Check if the book is available
        self.books[book_title].checked_out_by = self.current_student
        # Set current page to 0
        self.students[self.current_student].books_checked_out[book_title] = 0 

        # Update the books.csv file
        self.update_books_csv()

    def update_books_csv(self):
        with open('books.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["title", "author", "restriction", "restricted_class", "checked_out_by"])  # Update the header
            for book in self.books.values():
                if isinstance(book, RestrictedBook):
                    writer.writerow([book.title, book.author, 'yes', ','.join(book.restricted_class), book.checked_out_by])
                else:
                    writer.writerow([book.title, book.author, 'no', '', book.checked_out_by])

    def display_checked_out_books(self):
        checked_out_books = [book.title for book in self.books.values() if book.checked_out_by == self.current_student]
        print(f"Books checked out by {self.current_student}: {', '.join(checked_out_books)}")

    def return_book(self):
        book_title = input("Enter the title of the book you wish to return: ")

        if book_title not in self.books:
            print("Sorry, that book doesn't exist in our library.")
            return
    
        if self.books[book_title].checked_out_by == self.current_student:
            self.books[book_title].checked_out_by = None  # Reset the 'checked_out_by' attribute
            self.update_books_csv()  # Update the CSV file
            print(f"Successfully returned {book_title}.")
        else:
            print("This book was not checked out by you.")
