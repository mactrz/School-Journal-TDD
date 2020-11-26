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

        self.students[id] = {'name': name, 'surname': surname}
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
        grades = self.students[studid]['Subjects'][subject]
        self.addSubject(studid, newName)
        self.students[studid]['Subjects'][newName] = grades

j = Journal()



