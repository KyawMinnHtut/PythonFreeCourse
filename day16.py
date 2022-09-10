class Human():
    planet = "Earth"
    def __init__(self, name, age):  #self points to an Instance and can modify both Instance state and Class state
        self.name = name
        self.age = age
    def display(self):
        print("Name : ", self.name, ", Age : ", self.age, ", Planet :", self.planet)   #selfဆိုတဲ့ အတွက် global valueကို instance variableတစ်ခုအဖြစ် generateလုပ်သွား = naming lookup
        #print("Name : ", self.name, ", Age : ", self.age, ", Planet :", Human.planet)
    @classmethod
    def class_method(cls):  #cls referd to Class(Human) itself and modify Class state
        cls.planet = "Satun"
        print("Class variable access with @classmethod ==>", cls.planet)
    @staticmethod   #like regular function and access neither Instance nor Class state
    def static_method():
        print("Static method called ")
h1 = Human("Kyaw Min Htut", 30)
#h1.planet = "Mars" #ဒီလိုဆို instance varမှာ assign valueရှိပီး global valueကို မယူ
h1.display()
h2 = Human("Mon Mon", 30)
h2.display()
Human.class_method()
Human.static_method()

#Naming Lookup ==> search if available in local, else global scope
class Lookup:
    planet = "Earth"
    def display(self):
        print("self.planet =>", self.planet)
l1 = Lookup()
print(l1.__dict__)
l1.planet = "Mars"
print(l1.__dict__)
l1.display()
l2 = Lookup()
l2.display()
print(l2.__dict__)

#program to interface, not implementation
#internal dataတွေကို တိုက်ရိုက် accessမလုပ်ဘဲ setter/getter(interface) ကနေဘဲ လုပ်
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


#Property
#_(underscore) = protected member
class StudentProperty:
    def __init__(self, name, age):
        self._name = name
        self._age = age
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, age):     #verity invalid data
        if 0 < age < 100:
            self._age = age
    @age.deleter
    def age(self):
        del self._age
    def display(self):
        print("Name ", self._name, ", Age ", self.age)
stu1 = StudentProperty("Kyaw Min Htut", 30)
#stu1.name = "Mon Mon"  #name change from outside
print(stu1.age)
stu1.age = 16
stu1.display()
#del stu1.age

#Passing members of one class to another class
class School:
    def __init__(self):
        self._student_list = []
    def enroll(self, student):
        self._student_list.append(student)
        print(student._name, "have been enrolled.")
school = School()
school.enroll(stu1)

#Get reference count
import sys
import gc
lst = [100,200,300]
print("Reference count ", sys.getrefcount(lst))
lst_two = lst
print("Reference count ", sys.getrefcount(lst))
lst_two = None
print("Reference count ", sys.getrefcount(lst))

print(gc.collect())
print(gc.garbage)

#Destructor
class MyClass:
    def __init__(self):
        self.list = [x for x in range(100000)]
    def __del__(self):
        print("Destructor called")
        self.list = None
a = MyClass()
del a

#Inheritance => code reuse in hierachy
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def work(self):
        print(self.name, " work")
    def eat(self):
        print(self.name, " eat")
class Doctor(Human):
    def __init__(self, name, age, medical_field):
        super().__init__(name, age)
        self.medical_field = medical_field
    def work(self):
        super().work()
        print("Doctor is working")
drAyeKo = Doctor("Dr Aye Ko", 40, "OG")
drAyeKo.work()
drAyeKo.eat()