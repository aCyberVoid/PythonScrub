import csv

from books import Book, RestrictedBook
from students import Student


class Library:
    def __init__(self):
        self.books = {}  # Dictionary to store books in the library
        self.students = {}  # Dictionary to store students in the library
        self.current_student = None  # The current student using the library program

    def library_menu(self):  # Library menu
        while True:
            choice = input(
                "1. Check out a book\n"
                "2. Return a book\n"
                "3. See checked out books\n"
                "4. See current page of a book\n"
                "5. Exit\n"
                "\nEnter choice:\n> "
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

    def load_books(self, filename):  # Load books from a CSV file
        try:  # Try to open the file - exception handling
            with open(filename, 'r') as file:  # Open the file
                books_reader = csv.reader(file)  # Create books_reader object
                next(books_reader)  # Skip the header row
                for row in books_reader:  # Iterate over the rows
                    title = row[0]  # Get the title
                    author = row[1]  # Get the author
                    restriction = row[2]  # Get the restriction
                    restricted_class = row[3] if len(
                        row) >= 4 else None  # Get the restricted class
                    checked_out_by = row[4] if len(
                        row) >= 5 and row[4] else None

                    if restriction.lower() == 'yes':  # Check if the book is restricted
                        # Create a RestrictedBook object
                        book = RestrictedBook(title, author, restricted_class)
                    else:
                        book = Book(title, author)  # Create a Book object

                    book.checked_out_by = checked_out_by  # Set the checked out by attribute
                    # Add the book to the library catalogue [books.csv]
                    self.books[title] = book
        except FileNotFoundError:  # Catch the FileNotFoundError exception
            print(f"Error: File '{filename}' not found.")

    def update_books_csv(self):
        with open('books.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["title", "author", "restriction", "restricted_class",
                            "checked_out_by", "current_page"])  # Update the header
            print("==========")
            print("DEBUGGING: updates_books_csv function\n")  # Debugging
            for book in self.books.values():
                if isinstance(book, RestrictedBook):
                    writer.writerow([book.title, book.author, 'yes', ','.join(
                        book.restricted_class), book.checked_out_by, book.current_page])  # Write the row to the file
                else:
                    # Write the row to the file
                    writer.writerow(
                        [book.title, book.author, 'no', '', book.checked_out_by, book.current_page])
                # Debugging
                print(
                    "DEBUG: " + f"Book: {book.title}, Checked out by: {book.checked_out_by}, Current page numbers is {book.current_page}.")
            print("==========")

# =========================================================================
# This section of the code focuses on the menu options from library_menu()
# =========================================================================
    def available_books(self):
        book_list = []  # Create an empty list
        for book in self.books.keys():
            if self.books[book].checked_out_by is None:  # Only print available books
                print(book)
                book_list.append(book)
        return book_list

    def check_out_book(self):
        print("\nAvailable books:")
        self.available_books()

        book_title = input(
            "Enter the title of the book you wish to check out: ")

        if book_title not in self.books:
            print("Sorry, that book doesn't exist in our library.\n")
            return

        if isinstance(self.books[book_title], RestrictedBook):
            if self.books[book_title].restricted_class != self.students[self.current_student].restricted_class:
                print("You need to be in the class to check out this book.\n")
                return

        if self.books[book_title].checked_out_by is not None:
            print(
                f"Sorry, {book_title} is already checked out by {self.books[book_title].checked_out_by}.\n")
            return

        self.books[book_title].checked_out_by = self.current_student
        self.update_books_csv()
        self.books[book_title].available = False  # Set the book as unavailable
        print(f"Successfully checked out {book_title}.\n")

    def display_checked_out_books(self):  # Display the checked out books
        checked_out_books = [book.title for book in self.books.values(
        ) if book.checked_out_by == self.current_student]  # Get checked out books
        # Print the checked out books
        print(
            f"Books checked out by {self.current_student}: {', '.join(checked_out_books)}\n")

    def return_book(self):  # Return a book
        # Get the book title
        book_title = input("Enter the title of the book you wish to return: ")

        if book_title not in self.books:  # Check if the book exists
            # Print an error message
            print("Sorry, that book doesn't exist in our library.")
            return

        if self.books[book_title].checked_out_by is None:  # Check if the book is checked out
            # Print an error message
            print(f"The book {book_title} is already returned.")
            return

        # Check if the book is checked out by the current student
        if self.books[book_title].checked_out_by != self.current_student:
            # Print an error message
            print(f"You don't have {book_title} checked out.")
            return

        # Set the checked out by attribute to None
        self.books[book_title].checked_out_by = None
        self.update_books_csv()  # Update the books.csv file
        # Print a success message
        print(f"Successfully returned {book_title}.")

    def see_current_page(self):
        book_title = input("What book would you like to check?\n> ")

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
