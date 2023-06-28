# Book Class
class Book:
    def __init__(self, title, author, restriction, restricted_class):
        # Initialize the attributes of a book object
        self.title = title
        self.author = author
        self.restriction = restriction
        self.restricted_class = restricted_class
        self.current_page = 1  # Initialize current page to 1
        self.due_date = None  # Initialize due date as None

    def __str__(self):
        # String representation of a book object including checkout status
        status = "Checked Out" if self.is_checked_out() else "Available"
        return f"{self.title} by {self.author} ({status})"

    def is_book_available(self):
        return not self.is_checked_out()

    def update_current_page(self, page_number):
        # Update the current page of the book
        self.current_page = page_number

    def set_due_date(self, due_date):
        # Set the due date for the book
        self.due_date = due_date

    def is_checked_out(self):
        # Check if the book is checked out
        return self.due_date is not None
