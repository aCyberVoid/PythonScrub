# Student Class
class Student:
    def __init__(self, name, restricted_class):
        # Create the attributes of a student object
        self.name = name
        self.restricted_class = restricted_class
        self.books = []  # Initialize an empty list to store books

    def __str__(self):
        book_info = "\n".join(
            [f"Title: {book.title}, Page: {book.current_page}, Due Date: {book.due_date}" for
             book in self.books])
        return f"{self.name} is in {self.restricted_class}.\nBooks checked out:\n{book_info}"

    def check_out_book(self, book):
        if self.has_access(book):
            if not book.is_checked_out():
                self.books.append(book)
                book.set_due_date("2023-07-01")  # Set a default due date
                print(f"{self.name} has checked out the book: {book}")
            else:
                print(f"The book '{book.title}' is already checked out.")
        else:
            print(f"{self.name} is not allowed to check out the book: {book}")

    def check_in_book(self, book):
        if book in self.books:
            self.books.remove(book)
            book.set_due_date(None)  # Reset the due date
            print(f"{self.name} has returned the book: {book}")
        else:
            print(f"{self.name} does not have the book: {book}")

    def return_book(self, book_title):
        # Return a book by removing it from the student's list of books
        if book_title in self.books:
            self.books.remove(book_title)
            book_title.update_current_page(1)  # Reset current page to 1
            book_title.set_due_date(None)  # Reset due date to None

    def get_current_page(self, book_title):
        # Retrieve the current page of a book for the student
        if book_title in self.books:
            return book_title.current_page
        else:
            return "Book not checked out"

    def get_due_date(self, book_title):
        # Retrieve the due date of a book for the student
        if book_title in self.books:
            return book_title.due_date
        else:
            return "Book not checked out"

    def has_access(self, book):
        if book.restriction == "Yes" and book.restricted_class != self.restricted_class:
            return False
        elif book.is_checked_out():
            return False
        else:
            return True
