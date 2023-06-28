# Magical Academy for Cats (MAC) Library Project

> This is mostly to explain to myself what each line of code was doing as I was working through the project.

## MAC Library Project Explanation

```python
# Import the Book and Student class
import csv
from book import Book
from student import Student
```

- Importing the necessary modules and classes required for the program.
- `import csv` used here as the program makes use of 2 CSV files, books.csv and students.csv

---

```python
# Open books.csv and read it into a list of dictionaries
with open('books.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    next(reader)  # Skip the header row
    books = []
    for row in reader:
        # Append each row as a dictionary to the books' list
        books.append({
            'Book Title': row[0],
            'Author': row[1],
            'Restriction': row[2],
            'Restricted Class': row[3]
        })
```

- Opening the `books.csv` file in read mode and creating a reader object using the csv module.
- Skipping the header row using `next(reader)` to move the reader to the next row.
- Created an empty list `books` to store the book data from books.csv.
- Iterating over each row in the reader and appending a dictionary representing each row to the `books` list.

---

```python
# Open students.csv and read it into a list of dictionaries
with open('students.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    next(reader)  # Skip the header row
    students = []
    for row in reader:
        # Append each row as a dictionary to the students' list
        students.append({
            'Name': row[0],
            'Restricted Class': row[1],
        })
```

- Opening the `students.csv` file in read mode and creating a reader object using the csv module.
- Skipping the header row using `next(reader)` to move the reader to the next row.
- Created an empty list `students` to store the student data from students.csv.
- Iterating over each row in the reader and appending a dictionary representing each row to the `students` list.

---

```python
# Create Book instances using the data from books.csv
book_objects = []
for book_data in books:
    book = Book(
        book_data['Book Title'],
        book_data['Author'],
        book_data['Restriction'],
        book_data['Restricted Class']
    )
    book_objects.append(book)
```

- Creating instances of the `Book` class for each book in the `books` list using the book data.
- Creating a list called `book_objects` to store the created book instances.

---

```python
# Print the initial details of all books
print("Library Inventory:")
for book in book_objects:
    print(book)  # Print book details
```

- Printing the initial details of all books in the library inventory by iterating over the `book_objects` list and calling the `print()` function on each book.

---

```python
# Create Student instances using the data from students.csv
student_objects = []
for student_data in students:
    student = Student(
        student_data['Name'],
        student_data['Restricted Class']
    )
    student_objects.append(student)
```

- Creating instances of the `Student` class for each student in the `students` list using the student data.
- Created a list `student_objects` to store the created student instances.

---

The code beyond this point interacts with the library system through a menu-driven approach, allowing users to perform various operations such as checking out books, checking in books, viewing checked out books, viewing due dates and page numbers, and quitting the program. It uses the `student_objects` and `book_objects` to access the student and book instances and perform the corresponding actions. After each interaction, the updated details of all books in the library inventory are printed.

Menu Preview

```
Library Inventory:
The Enchanted Chronicles by Luna Whiskerfrost (Available)
Spellbinding Secrets by Midnight Starshine (Available)
Paws and Potions by Mystic Moonwhisker (Available)
Whiskers of Wisdom by Sparkle Spellpaw (Available)
Casting Catnip Curses by Willow Mistypaws (Available)
Purr-fectly Bewitching Spells by Stardust Whiskerwitch (Available)
Wands and Whiskers by Misty Moonshadow (Available)
The Cat's Grimoire by Whispering Whiskertail (Available)
Spells and Sorcery by Mystic Moonwhisker (Available)
Magical Meows by Merlin Whiskerweaver (Available)

==== Library Menu ====
1. Check out a book
2. Check in a book
3. View checked out books
4. View due dates and page numbers
5. Quit
Enter your choice:
```

> To be fair, I just realized I can make an option to print the available books, but for now I am happy with this. It at least shows that the library list works.