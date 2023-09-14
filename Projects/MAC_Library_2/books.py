# def load_books(filename):
#     """Load books from a CSV file."""
#     books = []
#     with open(filename, 'r') as csvfile:
#         reader = csv.DictReader(csvfile)
#         for row in reader:
#             if row['Restriction'].lower() == 'no':
#                 book = Book(row['Title'], row['Author'])
#             else:
#                 book = RestrictedBook(row['Title'], row['Author'], row['Restricted Class'])
#             books.append(book)
#     return books

# Book Class
class Book:
    def __init__(self, title, author, checked_out_by):
        # Initialize the attributes of a book object
        self.title = title
        self.author = author
        self.current_page = 1  # Initialize current page to 1
        self.due_date = None  # Initialize due date as None
        self.checked_out_by = checked_out_by

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

class RestrictedBook(Book):
    # initialize the attributes of a restricted book object
    def __init__(self, title, author, restricted_class, checked_out_by):
        super().__init__(title, author, checked_out_by)
        self.restricted_class = restricted_class