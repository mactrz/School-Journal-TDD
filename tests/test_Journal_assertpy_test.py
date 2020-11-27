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


    def test_addSubject1(self):
        self.tmp.addStudent('Maciej', 'Testowy', 3)
        self.tmp.addSubject(3, 'Przyroda')
        assert_that(self.tmp.students[3]['Subjects']).is_equal_to({'Przyroda':[]})

    def test_addSubject2(self):
        self.tmp.addStudent('Maciej', 'Testowy', 3)
        self.tmp.addSubject(3, 'Przyroda')
        self.tmp.addSubject(3, 'WF')
        assert_that(self.tmp.students[3]['Subjects']).is_equal_to({'Przyroda':[], 'WF':[]})

    def test_addSubject_exception1(self):
        self.tmp.addStudent('Maciej', 'Testowy', 3)
        assert_that(self.tmp.addSubject).raises(Exception).when_called_with(3, '')

    def test_addSubject_exception2(self):
        self.tmp.addStudent('Maciej', 'Testowy', 3)
        assert_that(self.tmp.addSubject).raises(Exception).when_called_with(3, 3)

    def test_addSubject_exception3(self):
        self.tmp.addStudent('Maciej', 'Testowy', 3)
        assert_that(self.tmp.addSubject).raises(Exception).when_called_with(2, 'New')

    def test_addSubject_exception4(self):
        self.tmp.addStudent('Maciej', 'Testowy', 3)
        assert_that(self.tmp.addSubject).raises(Exception).when_called_with(True, 'New')

    def test_editSubject1(self):
        self.tmp.addStudent('Maciej', 'Testowy', 3)
        self.tmp.addSubject(3, 'Przyroda')
        self.tmp.editSubject(3, 'Przyroda', 'Matematyka')
        assert_that(self.tmp.students[3]['Subjects']).is_length(1)

    def test_editSubject2(self):
        self.tmp.addStudent('Maciej', 'Testowy', 3)
        self.tmp.addSubject(3, 'Przyroda')
        self.tmp.editSubject(3, 'Przyroda', 'Matematyka')
        assert_that(self.tmp.students[3]['Subjects']).contains('Matematyka')

    def test_editSubject3(self):
        self.tmp.addStudent('Maciej', 'Testowy', 3)
        self.tmp.addSubject(3, 'Przyroda')
        self.tmp.editSubject(3, 'Przyroda', 'Matematyka')
        assert_that(self.tmp.students[3]['Subjects']).does_not_contain('Przyroda')

    def test_editSubject_exception1(self):
        self.tmp.addStudent('Maciej', 'Testowy', 3)
        self.tmp.addSubject(3, 'Przyroda')
        assert_that(self.tmp.editSubject).raises(Exception).when_called_with(2, 'Przyroda')

    def tearDown(self):
        self.tmp = None