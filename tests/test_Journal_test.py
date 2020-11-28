import unittest
from src.sample.Journal import Journal
from parameterized import parameterized, parameterized_class

class TestJournal(unittest.TestCase):
    def setUp(self):
        self.tmp = Journal()

    def test_add_student(self):
        self.assertEqual(self.tmp.addStudent('Jaroslaw', 'Bogdaniec', 2), 2)

    def test_add_student_len(self):
        self.tmp.addStudent('Mirek', 'Nowy', 5)
        self.assertEqual(len(self.tmp.students), 1)

    def test_add_student_name(self):
        self.tmp.addStudent('Arek', 'Asdfa', 4)
        self.assertEqual(self.tmp.students[4]['name'], 'Arek')

    def test_add_student_surname(self):
        self.tmp.addStudent('Arek', 'Asdfa', 4)
        self.assertEqual(self.tmp.students[4]['surname'], 'Asdfa')

    def test_add_student_exception_type1(self):
        with self.assertRaises(TypeError):
            self.tmp.addStudent(123, 'Surname', 3)

    def test_add_student_exception_type2(self):
        with self.assertRaises(TypeError):
            self.tmp.addStudent('Name', True, 2)

    def test_add_student_exception_type3(self):
        with self.assertRaises(TypeError):
            self.tmp.addStudent('Name', 'Surname', 'MyId')

    def test_add_student_exception_type4(self):
        with self.assertRaises(Exception):
            self.tmp.addStudent('Maciej', 'Testowy', 2)
            self.tmp.addStudent('Name', 'Surname', 2)

    def test_add_student_exception_type5(self):
        with self.assertRaises(Exception):
            self.tmp.addStudent('Maciej', 'Testowy', -2)

    def test_edit_student1(self):
        self.tmp.addStudent('Maciej', 'Testowy', 3)
        self.tmp.editStudent(3, 'Jarek')
        self.assertEqual(self.tmp.students[3]['name'], 'Jarek')

    def test_edit_student2(self):
        self.tmp.addStudent('Maciej', 'Testowy', 3)
        self.tmp.editStudent(3, surname='Inny')
        self.assertEqual(self.tmp.students[3]['surname'], 'Inny')

    def test_edit_student3(self):
        self.tmp.addStudent('Maciej', 'Testowy', 3)
        self.tmp.editStudent(3, surname='Inny')
        self.assertEqual(self.tmp.students[3]['name'], 'Maciej')

    def test_deleteSubject(self):
        self.tmp.addStudent('Maciej', 'Testowy', 3)
        self.tmp.addSubject(3, 'Przyroda')
        self.tmp.deleteSubject(3, 'Przyroda')
        self.assertEqual(self.tmp.students[3]['Subjects'], {})

    def test_deleteSubject_exception1(self):
        self.tmp.addStudent('Maciej', 'Testowy', 3)
        self.tmp.addSubject(3, 'Przyroda')
        self.assertRaises(Exception, self.tmp.deleteSubject, 2, 'Przyroda')

    def test_deleteSubject_exception2(self):
        self.tmp.addStudent('Maciej', 'Testowy', 3)
        self.tmp.addSubject(3, 'Przyroda')
        self.assertRaises(Exception, self.tmp.deleteSubject, 3, 'None')

    def test_deleteSubject_exception3(self):
        self.tmp.addStudent('Maciej', 'Testowy', 3)
        self.tmp.addSubject(3, 'Przyroda')
        self.assertRaises(Exception, self.tmp.deleteSubject, '2', 'Przyroda')

    def test_deleteSubject_exception4(self):
        self.tmp.addStudent('Maciej', 'Testowy', 3)
        self.tmp.addSubject(3, 'Przyroda')
        self.assertRaises(Exception, self.tmp.deleteSubject, 2, 5)

    def test_editSubject_exception_length(self):
        self.tmp.addStudent('Maciej', 'Testowy', 3)
        self.tmp.addSubject(3, 'Przyroda')
        self.assertRaises(Exception, self.tmp.editSubject, 3, 'Przyroda', '')

    def test_editGrade(self):
        self.tmp.addStudent('Maciej', 'Testowy', 3)
        self.tmp.addSubject(3, 'Przyroda')
        self.tmp.addGrade(3, 'Przyroda', 4)
        self.assertEqual(self.tmp.editGrade(3, 'Przyroda', 4, 5), 5)

    def test_editGrade1(self):
        self.tmp.addStudent('Maciej', 'Testowy', 3)
        self.tmp.addSubject(3, 'Przyroda')
        self.tmp.addGrade(3, 'Przyroda', 4)
        self.tmp.editGrade(3, 'Przyroda', 4, 5)
        self.assertEqual(self.tmp.students[3]['Subjects']['Przyroda'], [5])

    def test_editGrade2(self):
        self.tmp.addStudent('Maciej', 'Testowy', 3)
        self.tmp.addSubject(3, 'Przyroda')
        self.tmp.addGrade(3, 'Przyroda', 4)
        self.tmp.addGrade(3, 'Przyroda', 4)
        self.tmp.addGrade(3, 'Przyroda', 5)
        self.tmp.editGrade(3, 'Przyroda', 4, 5)
        self.assertEqual(self.tmp.students[3]['Subjects']['Przyroda'], [4, 5, 5])

    def test_addComment(self):
        self.tmp.addStudent('Maciej', 'Testowy', 3)
        self.assertEqual(self.tmp.addComment(3, 'Comment'), 0)

    def test_addComment1(self):
        self.tmp.addStudent('Maciej', 'Testowy', 3)
        self.tmp.addComment(3, 'Comment')
        self.assertEqual(self.tmp.students[3]['Comments'], {0: 'Comment'})

    def test_addComment2(self):
        self.tmp.addStudent('Maciej', 'Testowy', 3)
        self.tmp.addComment(3, 'Comment')
        self.tmp.addComment(3, 'Comment2')
        self.assertEqual(len(self.tmp.students[3]['Comments']), 2)

    def test_addComment3(self):
        self.tmp.addStudent('Maciej', 'Testowy', 3)
        self.tmp.addComment(3, 'Comment')
        self.assertEqual(self.tmp.addComment(3, 'Comment2'), 1)



    def tearDown(self):
        self.tmp = None



@parameterized_class(('studid', 'subject', 'grade', 'change'), [
    (True, 'Przyroda', 4, 6),
    (2, 'Przyroda', 4, 6),
    (3, 3, 4, 6),
    (3, 'Przyro', 4, 6),
    (3, 'Przyroda', 'str', 6),
    (3, 'Przyroda', 3, 6),
    (3, 'Przyroda', 4, 8),
    (3, 'Przyroda', 4, False),
])

class TestParametrized(unittest.TestCase):

    def test_editGrade_exception(self):
        self.tmp = Journal()
        self.tmp.addStudent('Maciej', 'Testowy', 3)
        self.tmp.addSubject(3, 'Przyroda')
        self.tmp.addGrade(3, 'Przyroda', 4)
        self.tmp.addGrade(3, 'Przyroda', 4)
        self.tmp.addGrade(3, 'Przyroda', 5)
        self.assertRaises(Exception, self.tmp.editGrade, self.studid, self.subject, self.grade, self.change)

    def tearDown(self):
        self.tmp = None

if __name__ == '__main__':
    unittest.main()


