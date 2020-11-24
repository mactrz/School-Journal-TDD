class Journal:
    def __init__(self):
        self.students = {}

    def addStudent(self, name, surname, id):
        if type(name) != str or type(surname) != str:
            raise TypeError('Must be a string!')
        self.students[id] = {'name': name, 'surname': surname}
        return id