# Book Class
class Book:
    def __init__(self, title, author): # Constructor for the Book class
        self.title = title  # Set the title of the book
        self.author = author  # Set the author of the book
        self.current_page = 1  # Set the current page of the book to 1
        self.due_date = None  # Set the due date of the book to None
        self.checked_out_by = ''  # Set the checked out by attribute to an empty string

class RestrictedBook(Book):
    def __init__(self, title, author, restricted_class): # Constructor for the RestrictedBook class
        super().__init__(title, author) # Call the constructor of the parent class
        if isinstance(restricted_class, str):  # Check if a single class is provided
            restricted_class = [restricted_class]  # Convert the string to a list
        self.restricted_class = restricted_class # Set the restricted class of the book
