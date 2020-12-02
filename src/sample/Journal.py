import csv
import os
THIS_DIR = os.path.dirname(os.path.abspath(__file__))
my_data_path = os.path.join(THIS_DIR, os.pardir, '../data/export_data')



class Journal:
    def __init__(self):
        self.students = {}

    def addStudent(self, name, surname):

        id = len(self.students)

        if type(name) != str or type(surname) != str:
            raise TypeError('Must be a string')

        if type(id) != int or id < 0:
            raise TypeError('Id must be a unique positive number')

        if self.students.get(id, -1) != -1:
            raise Exception('Id must be unique')

        if name == '' or surname == '':
            raise Exception('Cannot give empty values')

        self.students[id] = {'name': name, 'surname': surname, 'Subjects': {}, 'Comments': {}}
        return id

    def editStudent(self, studid, name='', surname=''):

        if type(name) != str:
            raise Exception('Must be a string')
        if type(studid) != int:
            raise Exception('Id must be an integer')
        if type(surname) != str:
            raise Exception('Surname must be a string')
        if not self.students.keys().__contains__(studid):
            raise Exception("Student doesn't exist")
        if name != '':
            self.students[studid]['name'] = name
        if surname != '':
            self.students[studid]['surname'] = surname

    def deleteStudent(self, studid):
        if type(studid) != int:
            raise Exception('Id must be an integer')
        self.students.pop(studid)
        return studid

    def addSubject(self, studid, name):
        if not self.students.keys().__contains__(studid):
            raise Exception("Student doesn't exist")

        if type(studid) != int:
            raise Exception('Id must be an integer')

        if name == '':
            raise Exception('Empty values are invalid')

        if type(name) != str:
            raise Exception('Subject name must be a string')

        if not self.students[studid].keys().__contains__('Subjects'):
            self.students[studid]['Subjects'] = {}

        self.students[studid]['Subjects'][name] = []
        return studid

    def editSubject(self, studid, subject, newName):
        if not self.students.keys().__contains__(studid):
            raise Exception("Student doesn't exist")

        if not self.students[studid]['Subjects'].keys().__contains__(subject):
            raise Exception("Subject doesn't exist")

        if type(studid) != int:
            raise Exception('Id must be an integer')

        if type(subject) != str or type(newName) != str:
            raise Exception('Names must be strings')

        if subject == '' or newName == '':
            raise Exception('Empty values are invalid')

        grades = self.students[studid]['Subjects'][subject]
        self.students[studid]['Subjects'].pop(subject)
        self.addSubject(studid, newName)
        self.students[studid]['Subjects'][newName] = grades

    def deleteSubject(self, studid, subject):
        if not self.students[studid]['Subjects'].keys().__contains__(subject):
            raise Exception("Subject doesn't exist")

        if type(studid) != int:
            raise Exception('Id must be an integer')

        if not self.students.keys().__contains__(studid):
            raise Exception("Student doesn't exist")

        if type(subject) != str:
            raise Exception('Subject name must be a string')

        self.students[studid]['Subjects'].pop(subject)

    def addGrade(self, studid, subject, grade):

        if type(studid) != int:
            raise Exception('Id must be an integer')

        if not self.students.keys().__contains__(studid):
            raise Exception("Student doesn't exist")

        if type(subject) != str:
            raise Exception('Subject name must be a string')

        if len(subject) == 0:
            raise Exception('Empty values are invalid')

        if not self.students[studid]['Subjects'].keys().__contains__(subject):
            raise Exception("Subject doesn't exist")

        if type(grade) != int or grade > 6 or grade < 1:
            raise Exception("Grade must be a number betweeen 1 and 6")


        self.students[studid]['Subjects'][subject].append(grade)
        return True

    def editGrade(self, studid, subject, grade, change):

        if type(studid) != int:
            raise Exception('Id must be an integer')

        if type(subject) != str:
            raise Exception('Subject name must be a string')

        if not self.students.keys().__contains__(studid):
            raise Exception("Student doesn't exist")

        if not self.students[studid]['Subjects'].keys().__contains__(subject):
            raise Exception("Subject doesn't exist")

        if type(grade) != int or grade > 6 or grade < 1:
            raise Exception("Grade must be a number betweeen 1 and 6")

        if type(change) != int or change > 6 or change < 1:
            raise Exception("Grade must be a number betweeen 1 and 6")

        self.students[studid]['Subjects'][subject].remove(grade)
        self.students[studid]['Subjects'][subject].append(change)
        return True

    def averageSubject(self, studid, subject):

        if type(studid) != int:
            raise Exception('Id must be an integer')

        if type(subject) != str:
            raise Exception('Subject name must be a string')

        if not self.students.keys().__contains__(studid):
            raise Exception("Student doesn't exist")

        if not self.students[studid]['Subjects'].keys().__contains__(subject):
            raise Exception("Subject doesn't exist")

        all = sum(self.students[studid]['Subjects'][subject])

        count = len(self.students[studid]['Subjects'][subject])

        if count == 0:
            raise Exception('This student has no grades')

        return all / count

    def averageStudent(self, studid):

        if type(studid) != int:
            raise Exception('Id must be an integer')

        if not self.students.keys().__contains__(studid):
            raise Exception("Student doesn't exist")

        if self.students[studid]['Subjects'] == {}:
            raise Exception("Student has no subjects")

        returnVal = 0
        length = 0
        for i in self.students[studid]['Subjects']:
            if len(self.students[studid]['Subjects'][i]) != 0:
                all = sum(self.students[studid]['Subjects'][i])
                length1 = len(self.students[studid]['Subjects'][i])
                returnVal += all / length1
                length += 1

        if length == 0:
            raise Exception("Student's subjects have no grades")

        return returnVal / length

    def addComment(self, studid, message):

        if type(studid) != int:
            raise Exception('Id must be an integer')

        if not self.students.keys().__contains__(studid):
            raise Exception("Student doesn't exist")

        if type(message) != str:
            raise Exception("A comment must be a string")

        if len(message) == 0:
            raise Exception("A comment cannot be empty")

        length = len(self.students[studid]['Comments'])
        self.students[studid]['Comments'][length] = message
        return True

    def editComment(self, studid, commentid, newmessage):

        if type(studid) != int:
            raise Exception('Id must be an integer')

        if not self.students.keys().__contains__(studid):
            raise Exception("Student doesn't exist")

        if type(commentid) != int:
            raise Exception("Comment's id must an integer")

        if not self.students[studid]['Comments'].keys().__contains__(commentid):
            raise Exception("Comment doesn't exist")

        if type(newmessage) != str:
            raise Exception("A comment must be a string")

        if len(newmessage) == 0:
            raise Exception("A comment cannot be empty")


        self.students[studid]['Comments'][commentid] = newmessage

        return True

    def exportToFile(self):
        open(my_data_path, 'w+').close()
        with open(my_data_path, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['id', 'name', 'surname', 'Subjects', 'Comments'])
            writer.writeheader()
            for data in self.students:
                newOne = self.students[data]
                newOne['id'] = data
                writer.writerow(newOne)


    def importFromFile(self, path):
        my_data_path2 = os.path.abspath(path)
        with open(my_data_path2, 'r') as data:
            for line in csv.DictReader(data):
                studid = int(line['id'])
                name = line['name']
                surname = line['surname']
                subjects = eval(line['Subjects'])
                comments = eval(line['Comments'])
                self.addStudent(name, surname, studid)

                for subject in subjects:
                    self.addSubject(studid, subject)
                    for grade in subjects[subject]:
                        self.addGrade(studid, subject, grade)

                for comment in comments:
                    self.addComment(studid, comments[comment])
        data.close()






