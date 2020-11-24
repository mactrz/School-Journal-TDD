import unittest
from src.sample.Journal import Journal

class TestJournal(unittest.TestCase):
    def setUp(self):
        self.tmp = Journal()

    def test_add_student(self):
        self.assertEqual(self.tmp.addStudent('Jaroslaw', 'Bogdaniec', 2), 2)


    def tearDown(self):
        self.tmp = None