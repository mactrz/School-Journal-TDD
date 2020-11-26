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


j = Journal()

