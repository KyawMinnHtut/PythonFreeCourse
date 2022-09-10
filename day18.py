from abc import abstractmethod

#As in other dynamic languages, method is a variable and the next method overwrite/assign the first method
def method():
    print("Version One")
def method(a):
    print("Version Two")
def method(a,b):
    print("Version Three")

#Abastract Class
class Human:
    @abstractmethod
    def work(self):
        pass
class Teacher:
    def __init__(self):
        print("Teacher Constructor called.")

t = Teacher()

#Exception Handling
print("Start")
try:
    a = int(input("Enter a number : "))
    b = int(input("Enter a number : "))
    print("a / b = {}", a/b)
except (ZeroDivisionError,ValueError):
    print("Error when division by zero or value error")
except:     #general exception handling for all kinds of exception
    print("Error occured by I have no idea what error it is")
else:
    print("This is else block executed only when try is free from exception")
finally:
    print("Error or not, this finally block runs")  #clean-up code
print("End of program")

#User defined Exception
class OveragedException(Exception):
    def __init__(self, arg):
        self.msg = arg
class Under13Exception(Exception):
    def __init__(self, arg):
        self.msg = arg

age = int(input("Enter your age : "))
if age>60:
    raise OveragedException("Retired AGE")
elif age<13:
    raise Under13Exception("Hey child, play with your toys")
else:
    print("Good job. You are the building the country")