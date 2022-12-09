class Person:
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
    def get_bmi_result(self):
        bmi = self.weight/(self.height**2)
        if bmi < 18.5:
            print("Under weight.")
        elif bmi <= 24.9:
            print("Healthy.")
        else:
            print("Obese.")
a = input("Enter name: ")
b = int(input("Enter age: "))
c = int(input("Enter weight: "))
d = float(input("Enter height: "))
obj = Person(a, b, c, d)
obj.get_bmi_result()