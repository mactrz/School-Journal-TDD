from hamcrest import *
from src.sample.Journal import Journal
import unittest

class TestJournal(unittest.TestCase):
    def setUp(self):
        self.tmp = Journal()

    def test_addStudentHam(self):
        assert_that(self.tmp.addStudent('Aleks', 'Mareks', 3), equal_to(3))

    def test_edit_student4(self):
        self.tmp.addStudent('Maciej', 'Testowy', 3)
        self.tmp.editStudent(3, 'Inny')
        assert_that(self.tmp.students['surname'], equal_to('Testowy'))

    def tearDown(self):
        self.tmp = None