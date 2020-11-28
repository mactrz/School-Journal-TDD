import unittest
from src.sample.Journal import *

class JournalParameterizedFile(unittest.TestCase):

    def test_from_file(self):
      fileTest = open("../data/Journal_data_test")
      tmp = Journal()
      tmp.addStudent('Maciej', 'Testowy', 3)
      for line in fileTest:
        if line.startswith("#") or line.startswith(" ") or line.startswith("\n"):
            continue
        else:
            data = line.split(" ")
            name, surname, what, result = str(data[0]), str(data[1]), str(data[2]), str(data[3].strip("\n"))
            tmp.editStudent(3, name, surname)
            self.assertEqual(tmp.students[3][what], result)
      fileTest.close()


if __name__ == '__main__':
    unittest.main()