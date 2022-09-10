class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def work(self):
        print(self.name, " works")
    def eat(self):
        print(self.name, " eat")
class Doctor(Human):
    def __init__(self, name, age, medical_field):
        super().__init__(name, age)
        self.medical_field = medical_field
    def work(self):
        super().work()
        print("Doctor is working")
class Robot:
    def work(self):
        print("Robot work")


d = Doctor("Dr Aye Ko", 60, "OG")
d.work()
d = Robot()     #Duck typing ==> ဘာ type နေနေ Dynamic Programmingကြောင့် Inheritanceမလိုဘဲ Polimorphismရ
d.work()

#Composition    ==> has a relationship
class Car:              #car is not a relation with engine
    def __init__(self,engine):
        self.engine = engine
    def start(self):
        self.engine.start()
class GasolineEngine:           #Engine is a part of car. Not sub-type or inheritance
    def start(self):
        print("Gasoline Engine Start")
class DieselEngline:
    def start(self):
        print("Diesel Engine Start")
# car = Car()
# car.start()

#Depedency Inversion
gasolineEngine = GasolineEngine()
dieselEngine = DieselEngline()
engine = dieselEngine
car = Car(engine)
car.start()

#Operator Overloading ==> as +,-,*,/,<,> operator redefining
lst = [1,2,3] + [4,5]
print(lst)
class Money:
    def __init__(self, value):
        self.value = value
    def __add__(self, other):   #Objရဲ့ addဆိုတဲ့ operator methodကို overload လုပ်ခြင်း
        print("Add called")
        return Money(self.value+other.value)
    def __repr__(self): #representation of the class
        return "Money {}".format(self.value)
m1 = Money(100)
m2 = Money(200)
m3 = m1 + m2
print("m3 value is ", m3.value)
m4 = m1 + m2 + Money(300)
print("m4 value is ", m4)
