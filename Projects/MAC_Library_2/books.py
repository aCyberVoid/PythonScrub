# =======================================================================================
# This module contains the definition for the Book class and its subclass RestrictedBook.
# 
# Please review the README.md file for more information about this project.
# =======================================================================================
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


import csv

class RestrictedBook(Book):
    # initialize a sub class of Book called RestrictedBook
    def __init__(self, title, author, classes_allowed):
        super().__init__(title, author)
        self.classes_allowed = classes_allowed