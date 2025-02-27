class School:

    def __init__(self, name):
        self.__name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)


    def get_name(self):
        return self.__name

    @property
    def name(self):
        return self.__name + str(len(self.students))

    @name.setter
    def name(self, name):
        self.__name = name

    @classmethod
    def export_json(cls, school):
        pass



class Epsi(School):

    def __init__(self):
        super().__init__('epsi')

class Ifag(School):

    def __init__(self):
        super().__init__('ifag')

epsi = Epsi()

ifag = Ifag()

epsi.add_student('student1')

print(f'{epsi.get_name()} {epsi.students}')

ifag.add_student('ifag_student1')

print(f'{ifag.name} {ifag.students}')

print(epsi.students)