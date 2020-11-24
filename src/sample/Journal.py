class Journal:
    def __init__(self):
        self.students = {}

    def addStudent(self, name, surname, id):
        self.students[id] = name
        return id