# Magical Academy for Cats Library

### Program Analysis

##### 1. Write or draw about the problem

The problem involves creating a library management system for the Magical Academy for Cats. The library contains regular and resitrcted books, and is accessed by student cats. The main componenents we need to manage are:

* Books
* Students
* Interactions between the students and the books [checking out, reading, tracking due dates, and progress in books]
* Restrictions for certain books

##### 2. Extract key concepts from Step 1 and research them

I've identified the following key concepts:

* **Library**: This is a collection of books. It should track the books it contains and their check out status. It also holds the restricted section.
* **Book**: A book has properties like title, author, genre, page count, etc. It has a status [checked out or available] and can belong to the restricted section or not.
* **Student**: A student can check out books, read books, and track their progress and due dates for checked out books.
* **Restricted Section**: This is a special section of the library. Only students in corresponding classes are allowed to access these books.

What I beleive I need to research:

* How to model these entities in Python [i.e. which properties and methods they should have]
* How to efficiently load and save data to CSV files
* How to handle the data and time operations in Python [for due dates]
* How to enforce the access restrictions for the restricted section

##### 3. Create a class hierarchy and object map for the concepts

Based on the problem analysis, the following classes can be identified:

* **Library**: Contains a list of books [both regular and restricted] and methods to manage them
* **Book**: Represents a single book. Can be a base class for regular and restricted book titles
* **Student**: Contains information about a student and methods to manage their interactions with the library

I identified two subclasses of **Book**:

* **RegularBook**: A book that any student can access
* **RestrictedBook**: A book that only certain students can access

The relationship between these classes can be summarized as follows:

* A **Library** contains multiple Books [both RegularBook and RestrictedBook]
* A **Student** can check out and read Books
* A **Student** needs special permission to access a Restrictedbook

I can use composition to model these relationships. For instance, a Library object can contain a list of Book objects.

---

# Next Steps

I will start by defining the classes and their properties. Then I will write methods for the classes and use unit tests to verify that they are working correctly.

For every code block we write, I need to make sure it follows the guidelines set out in PEP 8 for Python code style. I will also need to set up CSV file handling for storing and retrieving data about the students and books.

Lastly, I will write the `if __name__=='__main__'` part of the script where I'll create some initial objects and call the appropriate functions to start the library simulation.

I will iterate on this plan as necessary as I proceed with the development.
