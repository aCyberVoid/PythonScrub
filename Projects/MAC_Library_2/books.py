# Book Class
class Book:
    def __init__(self, title, author): # Constructor for the Book class
        self.title = title  # Set the title of the book
        self.author = author  # Set the author of the book
        self.current_page = 1  # Set the current page of the book to 1
        self.due_date = None  # Set the due date of the book to None
        self.checked_out_by = None  # Set the checked out by information to None

    def __str__(self):
        status = "Checked Out" if self.is_checked_out() else "Available"  # Determine the status of the book
        return f"{self.title} by {self.author} ({status})"  # Return a formatted string representation of the book

    def is_book_available(self):
        return not self.is_checked_out()  # Check if the book is available for checkout

    def update_current_page(self, page_number):
        self.current_page = page_number  # Update the current page of the book

    def set_due_date(self, due_date):
        self.due_date = due_date  # Set the due date of the book

    def is_checked_out(self):
        return self.due_date is not None  # Check if the book is checked out


class RestrictedBook(Book):
    def __init__(self, title, author, restricted_class): # Constructor for the RestrictedBook class
        super().__init__(title, author) # Call the constructor of the parent class
        if isinstance(restricted_class, str):  # Check if a single class is provided
            restricted_class = [restricted_class]  # Convert the string to a list
        self.restricted_class = restricted_class # Set the restricted class of the book
