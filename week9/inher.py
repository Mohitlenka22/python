class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
class Student(Person):
    super().__init__(self, name, age)

    def getDetails(self):
        return f'Name: {self.name}, Age: {self.age}'
obj = Student("mphit", 19)
print(obj.getDetails())