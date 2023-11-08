import unittest  # Import the unittest module

from library import Library  # Import library class

# This class will contain all the test cases for library.py
class TestLibrary(unittest.TestCase):

    def test_load_books(self):
        lib = Library()  # Create a Library object
        result = lib.load_books('books.csv')  # Call load_books() method on the instance
        self.assertIsNotNone(result)  # Assert that the result of the function is not None


# unittest.main() hich runs all the test cases
if __name__ == '__main__':
    unittest.main()