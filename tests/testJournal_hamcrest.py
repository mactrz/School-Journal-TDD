from hamcrest import *
from src.sample.Journal import Journal
import unittest
from parameterized import parameterized
import os
THIS_DIR = os.path.dirname(os.path.abspath(__file__))
my_data_path = os.path.join(THIS_DIR, os.pardir, 'data/export_data')

class TestJournal(unittest.TestCase):
    def setUp(self):
        self.tmp = Journal()
        self.tmp.students = {
            0: {
                'name': 'Ola',
                'surname': 'Inna',
                'Subjects': {},
                'Comments': {}
            },
            1: {
                'name': 'Aleks',
                'surname': 'Ciekawy',
                'Subjects': {'Przyroda':[2]},
                'Comments': {0:'Comment'}
            },
            2: {
                'name': 'Mirek',
                'surname': 'Testowy',
                'Subjects': {'WF': []},
                'Comments': {}
            },
            3: {
                'name': 'Maciej',
                'surname': 'Testowy',
                'Subjects': {'Przyroda':[3], 'Matematyka': []},
                'Comments': {0: 'Comment'}
            }
        }

    def test_addStudentHam(self):
        assert_that(self.tmp.addStudent('Aleks', 'Mareks'), equal_to(4))

    def test_edit_student4(self):
        self.tmp.editStudent(3, 'Inny')
        assert_that(self.tmp.students[3]['surname'], equal_to('Testowy'))

    @parameterized.expand([
        (True, 'Maciej', 'Test', 'Id must be an integer'),
        (3, 4, 'Test', 'Must be a string'),
        (3, 'Maciej', False, 'Surname must be a string'),
        (4, 'Maciej', 'Test', "Student doesn't exist")
    ])
    def test_exception_edit_student(self, studid, name, surname, mess):
        assert_that(calling(self.tmp.editStudent).with_args(studid, name, surname),
                    raises(type(Exception('Mess')), mess))

    def test_edit_student_has_key(self):
        assert_that(self.tmp.students, has_key(2))

    def test_edit_student_empty_vals(self):
        self.tmp.editStudent(3, '', '')
        assert_that(self.tmp.students, all_of(has_entry(3, {'name': 'Maciej', 'surname': 'Testowy',
                                                            'Subjects': {'Przyroda': [3], 'Matematyka': []}, 'Comments': {0: 'Comment'}}), has_key(3)))

    def test_add_student_empty_vals(self):
        assert_that(calling(self.tmp.addStudent).with_args('', ''),
                    raises(type(Exception('Mess')), 'Cannot give empty values'))

    def test_delete_student(self):
        assert_that(self.tmp.deleteStudent(3), equal_to(3))

    def test_delete_student_contains(self):
        self.tmp.deleteStudent(3)
        assert_that(self.tmp.students, not_(has_entry(3, {'name': 'Maciej', 'surname': 'Testowy'})))

    def test_deleteSubject2(self):
        self.tmp.deleteSubject(3, 'Przyroda')
        assert_that(self.tmp.students[3]['Subjects'], not_(has_entry('Przyroda', [])))

    def test_addGrade(self):
        assert_that(self.tmp.addGrade(3, 'Przyroda', 5), equal_to(True))

    def test_addGrade1(self):
        self.tmp.addGrade(3, 'Przyroda', 4)
        assert_that(self.tmp.students[3]['Subjects']['Przyroda'], has_item(4))

    @parameterized.expand([
        (6, 'Przyroda', 3, "Student doesn't exist"),
        (True, 'Przyroda', 3, 'Id must be an integer'),
        (3, '', 3, 'Empty values are invalid'),
        (3, 'WF', 3,"Subject doesn't exist"),
        (3, 3, 3, 'Subject name must be a string'),
        (3, 'Przyroda', True, "Grade must be a number betweeen 1 and 6"),
        (3, 'Przyroda', 10,"Grade must be a number betweeen 1 and 6")
    ])

    def test_addGradeParam(self, studid, subject, grade, mess):
        assert_that(calling(self.tmp.addGrade).with_args(studid, subject, grade),
                    raises(type(Exception('Mess')), mess))

    def test_editComment(self):
        assert_that(self.tmp.editComment(3, 0, 'New'), equal_to(True))

    def test_editComment2(self):
        self.tmp.editComment(3, 0, 'New')
        assert_that(self.tmp.students[3]['Comments'][0], equal_to('New'))

    @parameterized.expand([
        (True, 0, 'New', 'Id must be an integer'),
        (6, 0, 'New', "Student doesn't exist"),
        (3, 1, 'New', "Comment doesn't exist"),
        (3, '1', 'New', "Comment's id must an integer"),
        (3, 0, 1, "A comment must be a string"),
        (3, 0, '', "A comment cannot be empty")
    ])

    def test_editComment_exception(self, studid, commentid, new, pattern):
        assert_that(calling(self.tmp.editComment).with_args(studid, commentid, new), raises(Exception, pattern))

    def test_exportToFile(self):
        self.tmp.exportToFile()
        file = open(my_data_path)
        assert_that(file.readlines()[2], equal_to('0,Ola,Inna,{},{}\n'))
        file.close()

    def test_exportToFile1(self):
        self.tmp.exportToFile()
        file = open(my_data_path)
        assert_that(file.readlines()[4], equal_to("1,Aleks,Ciekawy,{'Przyroda': [2]},{0: 'Comment'}\n"))
        file.close()

    def test_exportToFile_empty(self):
        self.tmp.students = {}
        self.tmp.exportToFile()
        file = open(my_data_path)
        assert_that(len(file.readlines()), equal_to(2))
        file.close()

    def test_importFromFile(self):
        self.tmp.importFromFile('C:\\Users\\Maciek\\Desktop\\TestowanieProjetk1\\projekt-1-mactrz\\data\\import_data')
        assert_that(len(self.tmp.students), equal_to(6))

    def tearDown(self):
        self.tmp = None

if __name__ == '__main__':
    unittest.main()