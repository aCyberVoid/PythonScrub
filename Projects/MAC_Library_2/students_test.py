import unittest
from students import Student

class TestStudent(unittest.TestCase):
    def setUp(self):
        self.student1 = Student("Mittens", "Potion Making")
        self.student2 = Student("Tibbles", "")

    def test_student_creation(self):
        self.assertEqual(self.student1.name, "Mittens")
        self.assertEqual(self.student1.subject, "Potion Making")
        self.assertEqual(self.student2.name, "Tibbles")
        self.assertEqual(self.student2.subject, "")

if __name__ == '__main__':
    unittest.main()
