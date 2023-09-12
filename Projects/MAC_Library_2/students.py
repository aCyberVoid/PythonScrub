import csv

class Student:
    def __init__(self, name, subject):
        self.name = name  # The name of the student
        self.subject = subject  # Current class of student
        self.books_checked_out = {}  # Dictionary to store books checked out by the student and current page

def load_students(filename):
        students = {}
        with open(filename, 'r') as file:  # Opens the CSV file with student information
            students_reader = csv.reader(file)  # Creates a reader for the CSV file
            next(students_reader)  # Skips the header row
            for row in students_reader:  # For each row in the CSV file...
                name, subject = row  # ...unpack the row into variables
                students[name] = Student(name, subject)  # Adds a new Student to the students dictionary
        return students
