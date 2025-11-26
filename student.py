class Student:
    def __init__(self, name, gpa):
        self.name = name
        if 0.0 <= gpa <= 4.0:
            self.__gpa = gpa
        else:
            raise ValueError("GPA must be between 0.0 and 4.0")

    @property
    def gpa(self):
        return self.__gpa

    @gpa.setter
    def gpa(self, value):
        if 0.0 <= value <= 4.0:
            self.__gpa = value
        else:
            raise ValueError("GPA must be between 0.0 and 4.0")

    def display(self):
        print(f"Student: {self.name}, GPA: {self.gpa}")
