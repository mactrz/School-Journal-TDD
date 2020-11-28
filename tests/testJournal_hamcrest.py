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
                                                            'Subjects': {}, 'Comments': {}}), has_key(3)))

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

    @parameterized.expand([
        (2, 'Przyroda', 3),
        (True, 'Przyroda', 3),
        (3, '', 3),
        (3, 'WF', 3),
        (3, 3, 3),
        (3, 'Przyroda', True),
        (3, 'Przyroda', 10)
    ])

    def test_addGradeParam(self, studid, subject, grade):
        self.tmp.addStudent('Maciej', 'Testowy', 3)
        self.tmp.addSubject(3, 'Przyroda')
        assert_that(calling(self.tmp.addGrade).with_args(studid, subject, grade),
                    raises(type(Exception('Mess'))))

    def test_editComment(self):
        self.tmp.addStudent('Maciej', 'Testowy', 3)
        given = int(self.tmp.addComment(3, 'Comment'))
        assert_that(self.tmp.editComment(3, given, 'New'), equal_to('Comment'))

    def test_editComment2(self):
        self.tmp.addStudent('Maciej', 'Testowy', 3)
        given = self.tmp.addComment(3, 'Comment')
        self.tmp.editComment(3, given, 'New')
        assert_that(self.tmp.students[3]['Comments'][given], equal_to('New'))

    @parameterized.expand([
        (True, 0, 'New', 'Id must be an integer'),
        (2, 0, 'New', "Student doesn't exist"),
        (3, 1, 'New', "Comment doesn't exist"),
        (3, '1', 'New', "Comment's id must an integer")
    ])

    def test_editComment_exception(self, studid, commentid, new, pattern):
        self.tmp.addStudent('Maciej', 'Testowy', 3)
        self.tmp.addComment(3, 'Comment')
        assert_that(calling(self.tmp.editComment).with_args(studid, commentid, new), raises(Exception, pattern))

    def tearDown(self):
        self.tmp = None

if __name__ == '__main__':
    unittest.main()