from hamcrest import *
from src.sample.Journal import Journal
import unittest
from parameterized import parameterized

class TestJournal(unittest.TestCase):
    def setUp(self):
        self.tmp = Journal()

    def test_addStudentHam(self):
        assert_that(self.tmp.addStudent('Aleks', 'Mareks', 3), equal_to(3))

    def test_edit_student4(self):
        self.tmp.addStudent('Maciej', 'Testowy', 3)
        self.tmp.editStudent(3, 'Inny')
        assert_that(self.tmp.students[3]['surname'], equal_to('Testowy'))

    @parameterized.expand([
        (True, 'Maciej', 'Test'),
        (3, 4, 'Test'),
        (3, 'Maciej', False),
        (4, 'Maciej', 'Test')
    ])
    def test_exception_edit_student(self, studid, name, surname):
        self.tmp.addStudent('Maciej', 'Testowy', 3)
        assert_that(calling(self.tmp.editStudent).with_args([studid, name, surname]),
                    raises(type(Exception('kek'))))

    def test_edit_student_has_key(self):
        self.tmp.addStudent('Jarek', 'Testowy', 2)
        assert_that(self.tmp.students, has_key(2))

    def tearDown(self):
        self.tmp = None