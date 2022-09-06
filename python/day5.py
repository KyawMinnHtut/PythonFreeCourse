# my_list = [1,2,3,4,5]
# my_tuple = (1,2,3,4,5)
# my_set = {1,2,3,4,5} #not accept duplicate element
# #set is mutable, frozenset is immutable
# frozen_set = frozenset(my_set);
# print(frozen_set)
# print("   =========x=========\n")

# my_list = input("Enter two numbers :").split()
# a = int(my_list[0])
# b = int(my_list[1])
# print("Division : ", a//b)
# #same program in one line
# a,b = [int(i) for i in input("Enter two numbers : ").split()]
# print("Division : ", a//b)
# print("   =========x=========\n")

# #eval()
# a = int(input("Enter a :"))
# b = int(input("Enter b :"))
# equation = input("Enter equation :")
# c = eval(equation)
# print("Output =", c)
# print("   =========x=========\n")

#Command Line Arguments
from sys import argv
sum=0
args = argv[1:]
for x in args:
    print(x)
    n=int(x)
    sum=sum+n
print("The sum : ",sum)
print("   =========x=========\n")

#boolean operators
#AND
print("True and True :", True and True) #left truthy => return right hand side
print("True and False :", True and False)
print("False and True :", False and True) #left falsy => return left hand side
print("False and False :", False and False) 


print("a" and 1)
print("a" and 0)
print([] and 1)
print(() and 0)

#OR
print("True or True :", True or True) #left truthy => return left hand side
print("True or False :", True or False)
print("False or True :", False or True) #left falsy => return right hand side
print("False or False :", False or False) 


print("a" or 1)
print("a" or 0)
print([] or 1)
print(() or 0)

#semantic of AND and OR
def getTrue():
    print("Get True")
    return True
def getFalse():
    print("Get False")
    return False
print("True and True", getTrue() and getTrue())
print("False and True", getFalse() and getTrue())
print("True or True", getTrue() or getTrue())
print("False or True", getFalse() or getTrue())
