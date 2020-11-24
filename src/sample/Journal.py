class Journal:
    def __init__(self):
        self.students = {}

    def addStudent(self, name, surname, id):
        if type(name) != str:
            raise TypeError('Name must be a string!')
        self.students[id] = {'name': name, 'surname': surname}
        return id