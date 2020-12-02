import unittest
from assertpy import assert_that
from src.sample.Journal import Journal
from parameterized import parameterized

class TestJournal(unittest.TestCase):
    def setUp(self):
        self.tmp = Journal()
        self.tmp.students = {
            0: {
                'name': 'Ola',
                'surname': 'Inna',
                'Subjects': {'Przyroda': [4, 4, 5]},
                'Comments': {}
            },
            1: {
                'name': 'Aleks',
                'surname': 'Ciekawy',
                'Subjects': {'Przyroda': []},
                'Comments': {0: 'Comment', 1: 'Comment1'}
            },
            2: {
                'name': 'Mirek',
                'surname': 'Testowy',
                'Subjects': {'Przyroda': [], 'WF': []},
                'Comments': {}
            },
            3: {
                'name': 'Maciej',
                'surname': 'Testowy',
                'Subjects': {'Przyroda': [3], 'Matematyka': []},
                'Comments': {0: 'Comment'}
            }
        }

    def test_addStudentAssert(self):
        assert_that(self.tmp.addStudent('Paweł', 'Wolek')).is_equal_to(4)

    @parameterized.expand([
        (6, "Student doesn't exist"),
        (True, 'Id must be an integer'),
        (-3, "Student doesn't exist"),
    ])
    def test_exception_deleteStudent(self, arg, mess):
        assert_that(self.tmp.deleteStudent).raises(Exception).when_called_with(arg).is_equal_to(mess)


    def test_addSubject1(self):
        assert_that(self.tmp.students[1]['Subjects']).is_equal_to({'Przyroda':[]})

    def test_addSubject2(self):
        assert_that(self.tmp.students[2]['Subjects']).is_equal_to({'Przyroda': [], 'WF': []})

    def test_addSubject_exception1(self):
        assert_that(self.tmp.addSubject).raises(Exception).when_called_with(3, '').is_equal_to('Empty values are invalid')

    def test_addSubject_exception2(self):
        assert_that(self.tmp.addSubject).raises(Exception).when_called_with(3, 3).is_equal_to('Subject name must be a string')

    def test_addSubject_exception3(self):
        assert_that(self.tmp.addSubject).raises(Exception).when_called_with(6, 'New').is_equal_to("Student doesn't exist")

    def test_addSubject_exception4(self):
        assert_that(self.tmp.addSubject).raises(Exception).when_called_with(True, 'New').is_equal_to('Id must be an integer')

    def test_editSubject1(self):
        assert_that(self.tmp.students[1]['Subjects']).is_length(1)

    def test_editSubject2(self):
        self.tmp.editSubject(1, 'Przyroda', 'Matematyka')
        assert_that(self.tmp.students[1]['Subjects']).contains('Matematyka')

    def test_editSubject3(self):
        self.tmp.editSubject(1, 'Przyroda', 'Matematyka')
        assert_that(self.tmp.students[1]['Subjects']).does_not_contain('Przyroda')

    def test_editSubject_exception1(self):
        assert_that(self.tmp.editSubject).raises(Exception).when_called_with(6, 'Przyroda', 'WF').is_equal_to("Student doesn't exist")

    def test_editSubject_exception2(self):
        assert_that(self.tmp.editSubject).raises(Exception).when_called_with(1, 'Matematyka', 'WF').is_equal_to("Subject doesn't exist")


    def test_editSubject_exception4(self):
        assert_that(self.tmp.editSubject).raises(Exception).when_called_with('string', 'Przyroda', 'WF').is_equal_to('Id must be an integer')

    def test_editSubject_exception5(self):
        self.tmp.addStudent('Maciej', 'Testowy', 3)
        self.tmp.addSubject(3, 'Przyroda')
        assert_that(self.tmp.editSubject).raises(Exception).when_called_with(3, 5, 'WF')

    def test_editSubject_exception6(self):
        self.tmp.addStudent('Maciej', 'Testowy', 3)
        self.tmp.addSubject(3, 'Przyroda')
        assert_that(self.tmp.editSubject).raises(Exception).when_called_with(3, 'Przyroda', 10)

    def test_averageSubject(self):
        self.tmp.addStudent('Maciej', 'Testowy', 3)
        self.tmp.addSubject(3, 'Przyroda')
        self.tmp.addGrade(3, 'Przyroda', 3)
        self.tmp.addGrade(3, 'Przyroda', 4)
        self.tmp.addGrade(3, 'Przyroda', 5)
        assert_that(self.tmp.averageSubject(3, 'Przyroda')).is_equal_to(4)

    def test_averageSubject1(self):
        self.tmp.addStudent('Maciej', 'Testowy', 3)
        self.tmp.addSubject(3, 'Przyroda')
        self.tmp.addGrade(3, 'Przyroda', 4)
        self.tmp.addGrade(3, 'Przyroda', 4)
        self.tmp.addGrade(3, 'Przyroda', 5)
        assert_that(self.tmp.averageSubject(3, 'Przyroda')).is_close_to(4.33, 0.01)

    @parameterized.expand([
        (True, 'Przyroda'),
        (2, 'Przyroda'),
        (3, 'Przyr'),
        (3, 3)
    ])

    def test_averageSubject_exception(self, studid, subject):
        self.tmp.addStudent('Maciej', 'Testowy', 3)
        self.tmp.addSubject(3, 'Przyroda')
        self.tmp.addGrade(3, 'Przyroda', 4)
        self.tmp.addGrade(3, 'Przyroda', 4)
        self.tmp.addGrade(3, 'Przyroda', 5)
        assert_that(self.tmp.averageSubject).raises(Exception).when_called_with(studid, subject)

    def test_averageSubject_exception_zero(self):
        self.tmp.addStudent('Maciej', 'Testowy', 3)
        self.tmp.addSubject(3, 'Przyroda')
        assert_that(self.tmp.averageSubject).raises(Exception).when_called_with(3, 'Przyroda')

    def test_averageStudent1(self):
        self.tmp.addStudent('Maciej', 'Testowy', 3)
        self.tmp.addSubject(3, 'Przyroda')
        self.tmp.addGrade(3, 'Przyroda', 4)
        self.tmp.addGrade(3, 'Przyroda', 5)
        self.tmp.addSubject(3, 'WF')
        self.tmp.addGrade(3, 'WF', 2)
        self.tmp.addGrade(3, 'WF', 2)
        self.tmp.addGrade(3, 'WF', 4)
        assert_that(self.tmp.averageStudent(3)).is_close_to(3.58, 0.01)

    def test_averageStudent2(self):
        self.tmp.addStudent('Maciej', 'Testowy', 3)
        self.tmp.addSubject(3, 'Przyroda')
        self.tmp.addGrade(3, 'Przyroda', 4)
        self.tmp.addGrade(3, 'Przyroda', 5)
        self.tmp.addSubject(3, 'WF')
        self.tmp.addGrade(3, 'WF', 2)
        self.tmp.addGrade(3, 'WF', 3)
        self.tmp.addGrade(3, 'WF', 4)
        assert_that(self.tmp.averageStudent(3)).is_close_to(3.75, 0.01)

    def test_averageStudent3_one_subject(self):
        self.tmp.addStudent('Maciej', 'Testowy', 3)
        self.tmp.addSubject(3, 'Przyroda')
        self.tmp.addGrade(3, 'Przyroda', 4)
        self.tmp.addGrade(3, 'Przyroda', 5)
        assert_that(self.tmp.averageStudent(3)).is_close_to(4.5, 0.01)

    def test_averageStudent_exception1(self):
        self.tmp.addStudent('Maciej', 'Testowy', 3)
        self.tmp.addSubject(3, 'Przyroda')
        self.tmp.addGrade(3, 'Przyroda', 4)
        self.tmp.addGrade(3, 'Przyroda', 5)
        assert_that(self.tmp.averageStudent).raises(Exception).when_called_with(True)

    def test_averageStudent_exception2(self):
        self.tmp.addStudent('Maciej', 'Testowy', 3)
        self.tmp.addSubject(3, 'Przyroda')
        self.tmp.addGrade(3, 'Przyroda', 4)
        self.tmp.addGrade(3, 'Przyroda', 5)
        assert_that(self.tmp.averageStudent).raises(Exception).when_called_with(2).is_equal_to("Student doesn't exist")

    def test_averageStudent_exception3(self):
        self.tmp.addStudent('Maciej', 'Testowy', 3)
        assert_that(self.tmp.averageStudent).raises(Exception).when_called_with(3)\
        .is_equal_to('Student has no subjects')

    def test_averageStudent4(self):
        self.tmp.addStudent('Maciej', 'Testowy', 3)
        self.tmp.addSubject(3, 'Przyroda')
        self.tmp.addSubject(3, 'WF')
        self.tmp.addGrade(3, 'Przyroda', 4)
        self.tmp.addGrade(3, 'Przyroda', 5)
        assert_that(self.tmp.averageStudent(3)).is_close_to(4.5, 0.01)

    def test_averageStudent_exception4(self):
        self.tmp.addStudent('Maciej', 'Testowy', 3)
        self.tmp.addSubject(3, 'Przyroda')
        self.tmp.addSubject(3, 'WF')
        assert_that(self.tmp.averageStudent).raises(Exception).when_called_with(3)\
        .is_equal_to("Student's subjects have no grades")


    def tearDown(self):
        self.tmp = None

if __name__ == '__main__':
    unittest.main()