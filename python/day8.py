from random import random


values = ["a", "b", "c"]
for i in enumerate(values):
    print(i)

#while = conditional control loop
my_list = [10,20,30,40,50]
number = int(input("Enter a number to find in the list : "))
found = False
index = 0
while not found and (index < len(my_list)):
    if my_list[index] == number:
        print("Found at index ", index)
        found = True
    else:
        index += 1
print("End of while loop")
print("   =========x=========\n")

#Nested Loop
digit = '01'    #23456789'
lowercase_char = 'abc'  #defghijklmnopqrstuvwxyz'
uppercase_char = 'ABC'  #DEFGHIJKLMNOUQRSTUVWXYZ'
special_char = '!@#'    #$%^&*()'
for d in digit:
    for l in lowercase_char:
        for u in uppercase_char:
            for s in special_char:
                print(d+l+u+s)

#String
name = "Kyaw Min Htut"
for i in name:      #by element
    print(i)
for i in range(len(name)): #by index
    print(name[i])
print(name[0:])
print(name[::-1])  #reverse string

#find()
str = "Welcome from Python Programming Welcome"
print(str.find("Python"))
print(str.index("Python"))
#Stringထဲကနေ / နောက်က typeကို ယူရန်
application_type = "application/x-www-form-urlencoded"
type = application_type[application_type.find("/")+1:]  #index+1
print("Type :", type)

start_index = 0
count = 0
#implementation of count() by find() method
while str.find("Welcome") != -1:
    start_index = str.find("Welcome", start_index) + 1
    count = count + 1 
print("Total Count :", count)