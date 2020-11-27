class Journal:
    def __init__(self):
        self.students = {}

    def addStudent(self, name, surname, id):

        if type(name) != str or type(surname) != str:
            raise TypeError('Must be a string')

        if type(id) != int or id < 0:
            raise TypeError('Id must be a unique positive number')

        if self.students.get(id, -1) != -1:
            raise Exception('Id must be unique')

        if name == '' or surname == '':
            raise Exception('Cannot give empty values')

        self.students[id] = {'name': name, 'surname': surname, 'Subjects': {}, 'Comments': []}
        return id

    def editStudent(self, studid, name='', surname=''):

        if type(name) != str:
            raise Exception
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

        if not self.students[studid]['Subjects'].keys().__contains__(subject):
            raise Exception("Subject doesn't exist")

        if type(grade) != int or grade > 6 or grade < 1:
            raise Exception("Grade must be a number betweeen 1 and 6")

        self.students[studid]['Subjects'][subject].append(grade)
        return grade

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
        return change

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


j = Journal()



