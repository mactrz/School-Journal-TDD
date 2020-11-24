import unittest
from assertpy import assert_that
from src.sample.Journal import Journal


class TestJournal(unittest.TestCase):
    def setUp(self):
        self.tmp = Journal()

    def test_addStudentAssert(self):
        assert_that(self.tmp.addStudent('Paweł', 'Wolek', 5)).is_equal_to(5)

    def tearDown(self):
        self.tmp = None