from random import random
from secrets import choice
import string

print(string.ascii_letters)
print(string.digits)
print(string.punctuation)

def gen_password(pwd_length):
    pwd=""
    for i in range(pwd_length):
        if random() > 0.4:
            pwd += choice(string.ascii_letters)
        else:
            pwd += choice(string.digits)
    return pwd
print(gen_password(10))


#Imperative version max_stack-adt
def push(stack_tuple, ele):    #stack_tuple = (lst,max_length) သူ့ dataနဲ့ သူဖြစ်အောင်လို့ tupleနဲ့ packလုပ်
    if(len(stack_tuple[0])<stack_tuple[1]):
        stack_tuple[0].append(ele)
def pop(stack_tuple):
    if len(stack_tuple[0]) > 0:
        return stack_tuple[0].pop()
    else:
        return None
def is_empty(stack_tuple):
    return len(stack_tuple[0]) == 0

my_stack = []
max_length = 5
stack_tuple = (my_stack, max_length)    #parameterတွေများကြီး ထည့်ရ၊ မှားနိုင်
push(stack_tuple, 100)
push(stack_tuple, 200)
push(stack_tuple, 300)
push(stack_tuple, 400)
push(stack_tuple, 500)

while not is_empty(stack_tuple):
    print("Pop ", pop(stack_tuple))

another_list = ["Hello"]
another_tuple = (another_list, max_length)
push(another_tuple, 100)

#max_stack_closure version
def stack(max_length):
    lst = []
    def push(ele):
        if len(lst) < max_length:
            lst.append(ele)
    def pop():
        if not is_empty():
            return lst.pop()
        else:
            return None
    def is_empty():
        return len(lst) == 0
    return(push, pop, is_empty)
push, pop, is_empty = stack(5) #ဆိုးကျိုးက another stackဆောက်မယ်ဆို var_nameမတူအောင် ပေးရမယ်
push(10)
push(20)
push(30)
print(pop())
print(pop())
print(pop())
print(is_empty())

#OO version stack
class Stack:
    def __init__(self, max_length): # Constructor
        self.lst = []
        self.max_length = max_length
        print("Constructor run with max length ", max_length)
    def push(self, ele):
        if len(self.lst) < self.max_length:
            self.lst.append(ele)
        else:
            print("Error")
    def pop(self):
        if not self.is_empty():
            return self.lst.pop()
        else:
            return None
    def is_empty(self):
        return len(self.lst) == 0

s1 = Stack(5)
s1.push(100)
s1.push(200)
s1.push(300)
s1.push(400)
s1.push(500)
print(s1.pop())
print(s1.pop())
print(s1.pop())
print(s1.is_empty())
s2 = Stack(3)
s2.push(1)
s2.push(2)
s2.push(3)
while not s2.is_empty():
    s2.pop()
print(s2.is_empty())

class Student():
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
stu = Student("Kyaw Min Htut", "Grade 12")
print(stu.__dict__)
stu.gender = "Male" #BAD
print(stu.__dict__)
