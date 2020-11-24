class Journal:
    def __init__(self):
        self.students = {}

    def addStudent(self, name, surname, id):
        self.students[id] = {'Name': name, 'Surname': surname, 'Id': id}
        return id