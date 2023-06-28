class Library:
    def __init__(self, books):
        # Constructor to initialize the Library object with a list of books
        self.books = books

    def check_out_book(self, student, book):
        # Method to handle the book checkout process for a student
        if self.is_book_available(book):
            # Check if the book is available
            student.check_out_book(book)
        else:
            print(f"The book '{book.title}' is not available.")

    def check_in_book(self, student, book):
        # Method to handle the book check-in process for a student
        if book in student.books:
            # Check if the student has the book
            student.check_in_book(book)
        else:
            print(f"{student.name} does not have the book: {book}")

    def is_book_available(self, book):
        pass
