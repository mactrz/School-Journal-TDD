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
        assert_that(calling(self.tmp.editStudent).with_args(studid, name, surname),
                    raises(type(Exception('Mess'))))

    def test_edit_student_has_key(self):
        self.tmp.addStudent('Jarek', 'Testowy', 2)
        assert_that(self.tmp.students, has_key(2))

    def test_edit_student_empty_vals(self):
        self.tmp.addStudent('Maciej', 'Testowy', 3)
        self.tmp.editStudent(3, '', '')
        assert_that(self.tmp.students, all_of(has_entry(3, {'name': 'Maciej', 'surname': 'Testowy',
                                                            'Subjects': {}, 'Comments': []}), has_key(3)))

    def test_add_student_empty_vals(self):
        assert_that(calling(self.tmp.addStudent).with_args('', '', 1),
                    raises(type(Exception('Mess'))))

    def test_delete_student(self):
        self.tmp.addStudent('Maciej', 'Testowy', 3)
        assert_that(self.tmp.deleteStudent(3), equal_to(3))

    def test_delete_student_contains(self):
        self.tmp.addStudent('Maciej', 'Testowy', 3)
        self.tmp.deleteStudent(3)
        assert_that(self.tmp.students, not_(has_entry(3, {'name': 'Maciej', 'surname': 'Testowy'})))

    def test_deleteSubject2(self):
        self.tmp.addStudent('Maciej', 'Testowy', 3)
        self.tmp.addSubject(3, 'Przyroda')
        self.tmp.addSubject(3,'Matematyka')
        self.tmp.deleteSubject(3, 'Przyroda')
        assert_that(self.tmp.students[3]['Subjects'], not_(has_entry('Przyroda', [])))

    def test_addGrade(self):
        self.tmp.addStudent('Maciej', 'Testowy', 3)
        self.tmp.addSubject(3, 'Przyroda')
        assert_that(self.tmp.addGrade(3, 'Przyroda', 5), equal_to(5))

    def test_addGrade1(self):
        self.tmp.addStudent('Maciej', 'Testowy', 3)
        self.tmp.addSubject(3, 'Przyroda')
        self.tmp.addGrade(3, 'Przyroda', 4)
        assert_that(self.tmp.students[3]['Subjects']['Przyroda'], has_item(4))


    def tearDown(self):
        self.tmp = None