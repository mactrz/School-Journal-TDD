from hamcrest import *
from src.sample.Journal import Journal
import unittest

class TestJournal(unittest.TestCase):
    def setUp(self):
        self.tmp = Journal()

    def test_addStudentHam(self):
        assert_that(self.tmp.addStudent('Aleks', 'Mareks', 3), equal_to(3))

    def tearDown(self):
        self.tmp = None