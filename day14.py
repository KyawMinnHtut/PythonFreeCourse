#Nested Fun and Closure
from re import A


def counter():
    i = 1
    def next():
        nonlocal i
        i = i +1
        return i    #outter_funပီးသွားသော်လည်း outer_funရဲ့ variableကို သုံးလို့ရ
    return next

next_fun = counter()
print("Next ", next_fun())
print("Next ", next_fun())

#Decorator
def security(fun):
    print("Security checked")
    return fun
@security
def order():
    #security()
    print("Order processing")
def sale():
    print("Sale processing")
order()

def none_check(fun):
    def function(msg):
        if msg != None:
            return fun(msg)
        else:
            return ""
    print("None checking is done")
    return function
def strip_str(fun):
    def function(msg):
        return fun(msg.strip())
    print("String strip is done.")    
    return function
@none_check
def append_hi(msg):
    return msg + " hi"
@none_check
@strip_str
def to_upper(msg):
    return msg.upper()
print(append_hi("Hello"))
print(to_upper(" Kyaw Min Htut"))
print(to_upper(None))
print("   =========x=========\n")

#Generaotr Function  ====> for delay computation, for create custom collection
def counter():
    yield 1
    yield 2
    yield 3
    yield 4
count = counter()
print(type(count))
print(next(count))
print(next(count))
print(next(count))
print(next(count))
print("   =========x=========\n")

#Parameter Passing ==> pass by assignment
#scenario1
def fun(num):
    num += 1
    print("Value in fun ", num)
i = 100
fun(i)
fun(i)
print("After fun  ", i)
#scenario2
def append(lst):
    lst.append(100)
my_list = []
append(my_list)
append(my_list)
print("After append  ", my_list)

#scenario3
def update(lst):
    lst = [100,200]
update(my_list)
print("After update ", my_list)

#Pass by Assignment
a = 10  #immutable
b = a
a += 1
print(a , b)
lst_one = [100,200] #mutable scenario1
lst_two = lst_one
lst_one.append(300)
lst_two.append(400)
print(lst_one, lst_two)
lst1 = [1,2,3]      #mutable scenario2
lst2 = [4,5]       #lst1 and lst2 are separate objects
lst2.append(6)
print(lst1, lst2)