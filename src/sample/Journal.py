class Journal:
    def __init__(self):
        self.students = {}

    def addStudent(self, name, surname, id):

        if type(name) != str or type(surname) != str:
            raise TypeError('Must be a string')

        if type(id) != int:
            raise TypeError('Id must be a unique number')

        if self.students.get(id, -1) != -1:
            raise Exception('Id must be unique')

        self.students[id] = {'name': name, 'surname': surname}
        return id


j = Journal()
j.addStudent('mac', 'kek', 2)