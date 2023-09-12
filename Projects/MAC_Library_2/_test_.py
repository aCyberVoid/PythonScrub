import unittest
from books import Book, RestrictedBook

class TestBook(unittest.TestCase):
    def setUp(self):
        self.book1 = Book("Potion Brewing 101", "Prof. Whiskers")
        self.book2 = RestrictedBook("Advanced Necromancy", "Sir Meowsalot", "Necromancy")

    def test_book_creation(self):
        self.assertEqual(self.book1.title, "Potion Brewing 101")
        self.assertEqual(self.book1.author, "Prof. Whiskers")
        self.assertEqual(self.book2.title, "Advanced Necromancy")
        self.assertEqual(self.book2.author, "Sir Meowsalot")
        self.assertEqual(self.book2.classes_allowed, "Necromancy")

if __name__ == '__main__':
    unittest.main()
