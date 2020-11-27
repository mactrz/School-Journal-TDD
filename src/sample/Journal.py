class Journal:
    def __init__(self):
        self.students = {}

    def addStudent(self, name, surname, id, subjects=None, comments=None):

        if type(name) != str or type(surname) != str:
            raise TypeError('Must be a string')

        if type(id) != int or id < 0:
            raise TypeError('Id must be a unique positive number')

        if self.students.get(id, -1) != -1:
            raise Exception('Id must be unique')

        if name == '' or surname == '':
            raise Exception('Cannot give empty values')

        if subjects == None:
            subjects = {}

        if comments == None:
            comments = []

        self.students[id] = {'name': name, 'surname': surname, 'Subjects': subjects, 'Comments': comments}
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
            raise Exception("Student doesn't exist")

        grades = self.students[studid]['Subjects'][subject]
        self.students[studid]['Subjects'].pop(subject)
        self.addSubject(studid, newName)
        self.students[studid]['Subjects'][newName] = grades

j = Journal()



