import unittest
from src.sample.Journal import Journal

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

    def test_edit_student(self):
        self.tmp.addStudent('Maciej', 'Testowy', 3)
        self.tmp.editStudent('Jarek', studid=3)
        self.assertEqual(self.tmp.students[3]['name'], 'Jarek')

    def tearDown(self):
        self.tmp = None