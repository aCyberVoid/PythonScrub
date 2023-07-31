class Student:
    # initialize a new student object
    def __init__(self, name, subject):
        self.name = name  # The name of the student
        self.subject = subject  # Current class of student
        self.books_checked_out = {}  # Dictionary to store books checked out by the student and current page
