import unittest
from src.sample.Journal import *
import os
THIS_DIR = os.path.dirname(os.path.abspath(__file__))
my_data_path = os.path.join(THIS_DIR, os.pardir, 'data/Journal_data_test')

class JournalParameterizedFile(unittest.TestCase):

    def test_from_file(self):
      fileTest = open(my_data_path)
      tmp = Journal()
      tmp.addStudent('Maciej', 'Testowy')
      for line in fileTest:
        if line.startswith("#") or line.startswith(" ") or line.startswith("\n"):
            continue
        else:
            data = line.split(" ")
            name, surname, what, result = str(data[0]), str(data[1]), str(data[2]), str(data[3].strip("\n"))
            tmp.editStudent(0, name, surname)
            self.assertEqual(tmp.students[0][what], result)
      fileTest.close()


if __name__ == '__main__':
    unittest.main()