class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def set_age(self, age):     #verity invalid data
        if 0 < age < 100:
            self.age = age
    def get_age(self):
        return self.age
    def display(self):
        print("Name ", self.name, ", Age ", self.age)
stu = Student("Kyaw Min Htut", 30)
print(stu.get_age())
stu.set_age(11)
stu.display()