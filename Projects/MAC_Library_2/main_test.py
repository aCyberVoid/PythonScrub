from library import Library

def main():
    library = Library()
    library.load_books("books.csv")
    library.load_students("students.csv")

    # Set the current student to Snowball
    library.current_student = "Snowball"
    print("Testing with Snowball:")
    library.library_menu()

if __name__ == "__main__":
    main()