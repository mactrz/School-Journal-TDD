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

        self.students[id] = {'name': name, 'surname': surname}
        return id

    def editStudent(self, studid, name='', surname=''):
        if name != '':
            self.students[studid]['name'] = name
        if surname != '':
            self.students[studid]['surname'] = surname


j = Journal()
j.addStudent('mac', 'kek', 2)