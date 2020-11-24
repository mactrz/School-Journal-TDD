class Journal:
    def __init__(self):
        self.students = {}

    def addStudent(self, name, surname, id):
        if type(name) != str or type(surname) != str:
            raise TypeError('Must be a string')
        if type(id) != int:
            raise TypeError('Id must be a unique number')
        self.students[id] = {'name': name, 'surname': surname}
        return id