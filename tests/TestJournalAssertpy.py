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
                'Subjects': {'Przyroda': [4, 5], 'WF': [2, 2, 4]},
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
        self.tmp.addSubject(1, 'Matematyka')
        assert_that(self.tmp.students[1]['Subjects']).is_equal_to({'Przyroda':[], 'Matematyka': []})


    def test_addSubject_exception1(self):
        assert_that(self.tmp.addSubject).raises(Exception).when_called_with(3, '').is_equal_to('Empty values are invalid')

    def test_addSubject_exception2(self):
        assert_that(self.tmp.addSubject).raises(Exception).when_called_with(3, 3).is_equal_to('Subject name must be a string')

    def test_addSubject_exception3(self):
        assert_that(self.tmp.addSubject).raises(Exception).when_called_with(6, 'New').is_equal_to("Student doesn't exist")

    def test_addSubject_exception4(self):
        assert_that(self.tmp.addSubject).raises(Exception).when_called_with(True, 'New').is_equal_to('Id must be an integer')


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
        assert_that(self.tmp.editSubject).raises(Exception).when_called_with(3, 5, 'WF').is_equal_to('Names must be strings')

    def test_editSubject_exception6(self):
        assert_that(self.tmp.editSubject).raises(Exception).when_called_with(3, 'Przyroda', 10).is_equal_to('Names must be strings')

    def test_averageSubject(self):
        assert_that(self.tmp.averageSubject(0, 'Przyroda')).is_close_to(4.33, 0.01)

    def test_averageSubject1(self):
        assert_that(self.tmp.averageSubject(3, 'Przyroda')).is_close_to(3, 0.01)

    @parameterized.expand([
        (True, 'Przyroda', 'Id must be an integer'),
        (6, 'Przyroda', "Student doesn't exist"),
        (0, 'Przyr', "Subject doesn't exist"),
        (0, 3, 'Subject name must be a string')
    ])

    def test_averageSubject_exception(self, studid, subject, mess):
        assert_that(self.tmp.averageSubject).raises(Exception).when_called_with(studid, subject).is_equal_to(mess)

    def test_averageSubject_exception_zero(self):
        assert_that(self.tmp.averageSubject).raises(Exception).when_called_with(1, 'Przyroda')

    def test_averageStudent1(self):
        assert_that(self.tmp.averageStudent(2)).is_close_to(3.58, 0.01)

    def test_averageStudent2(self):
        assert_that(self.tmp.averageStudent(3)).is_close_to(3, 0.01)

    def test_averageStudent3_one_subject(self):
        assert_that(self.tmp.averageStudent(0)).is_close_to(4.33, 0.01)

    def test_averageStudent_exception1(self):
        assert_that(self.tmp.averageStudent).raises(Exception).when_called_with(True).is_equal_to('Id must be an integer')

    def test_averageStudent_exception2(self):
        assert_that(self.tmp.averageStudent).raises(Exception).when_called_with(6).is_equal_to("Student doesn't exist")


    def test_averageStudent_exception4(self):
        assert_that(self.tmp.averageStudent).raises(Exception).when_called_with(1)\
        .is_equal_to("Student's subjects have no grades")


    def tearDown(self):
        self.tmp = None

if __name__ == '__main__':
    unittest.main()