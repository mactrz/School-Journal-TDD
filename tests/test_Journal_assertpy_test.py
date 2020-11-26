import unittest
from assertpy import assert_that
from src.sample.Journal import Journal
from parameterized import parameterized

class TestJournal(unittest.TestCase):
    def setUp(self):
        self.tmp = Journal()

    def test_addStudentAssert(self):
        assert_that(self.tmp.addStudent('Paweł', 'Wolek', 5)).is_equal_to(5)

    @parameterized.expand([
        (2, ),
        (True, ),
        (-3, ),
    ])
    def test_exception_deleteStudent(self, arg):
        self.tmp.addStudent('Maciej', 'Testowy', 3)
        assert_that(self.tmp.deleteStudent).raises(Exception).when_called_with(arg)

    def tearDown(self):
        self.tmp = None