import unittest
import library

class TestLibrary(unittest.TestCase):
    def test_available_books(self):
        test_library = library.Library() # Create an instance of the Library class
        # test_library.check_out_book() # Call the check_out_book method
        book_list = test_library.available_books() # Call the available_books method
        self.assertEquals(book_list, ["Advanced Potions", "The Art of Invisibility", "Defence Against Dog Magic", "Dark Magic and How to Claw It"])

unittest.main()