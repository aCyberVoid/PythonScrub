# Potential Structure for Library 2.0
class Library:
    # initialize a new library object
    def __init__(self):
        self.books = {}  # Dictionary to store books in the library
        self.students = {}  # Dictionary to store students in the library

    # ... other methods ...

    def library_menu(self, student_name):
        """Display the library menu and handle the student's actions."""
        if not self.is_valid_student(student_name):
            print("You are not a registered student. Exiting...")
            return

        current_student = self.get_student(student_name)

        while True:
            print("\n1. List available books")
            print("2. Check out a book")
            print("3. Return a book")
            print("4. See your checked out books")
            print("5. Exit")

            option = int(input("\nSelect an option from the menu: "))

            if option == 1:
                self.list_books()
            elif option == 2:
                book_title = input("Enter the title of the book you want to check out: ")
                self.check_out_book(current_student, book_title)
            elif option == 3:
                book_title = input("Enter the title of the book you want to return: ")
                self.return_book(current_student, book_title)
            elif option == 4:
                current_student.list_checked_out_books()
            elif option == 5:
                print("Exiting...")
                break
            else:
                print("Invalid option. Please choose a number from 1-5.")
