mark = int(input("Enter mark : "))
if mark >= 80:
    print("Pass with distinction")
elif mark >= 40:
    print("Pass")
else:
    print("Fail")
print("Code End")

myanmar = int(input("Enter your mark for Myanmar : "))
english = int(input("Enter your mark for English : "))
maths = int(input("Enter your mark for Maths : "))
pass_mark = 40
#check with boolean operators
if myanmar >= 75 or english >= 75 or maths >= 80:
    print("Pass with Distinction")
elif myanmar >= pass_mark and english >= pass_mark and maths >= pass_mark:
    print("Pass")
else:
    print("Fail")

#check with conditional statements
if maths >= pass_mark:
    if english >= pass_mark:        
        if myanmar >= pass_mark:
            print("Pass")
        else:
            print("Fail")
    else:
        print("Fail")
else:
    print("Fail")
print("   =========x=========\n")

week_days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
day_week = int(input("Enter a number from 1 to 7 : "))
print(week_days[day_week-1])
print("   =========x=========\n")

subjects = int(input("Enter the number of Subject : "))
marks = []
for i in range(subjects):
    mark = int(input("Enter mark for subject " + str(i+1) + ":"))
    marks.append(mark)
print("Marks = ", marks)
isPass = True
for i in marks:
    isPass = isPass and i >= 40
if isPass:
    print("Pass the exam.")
else:
    print("Fail the exam.")

#Refractoring the above program to have good design
subjects = int(input("Enter the number of Subject : "))
#marks = []
isPass = True
for i in range(subjects):
    mark = int(input("Enter mark for subject " + str(i+1) + ":"))
    isPass = isPass and i >= 40    
if isPass:
    print("Pass the exam.")
else:
    print("Fail the exam.")
print("   =========x=========\n")

my_list = [10,20,30,40,50]
for i in my_list:   #read- only
    i*=2 #i = i *2
print(my_list)
for i in range(len(my_list)):  # noteice =>not pythnoic
    my_list[i]*=2 # my_list = my_list * 2
print(my_list)
print("   =========x=========\n")

"""for loops also have an else clause. The else clause executes after the loop completes normally. This means
that the loop did not encounter a break statement
"""
for n in range(2,10):
    for x in range(2,n):
        if n % x ==0:
            print( n, 'equals', x, '*', n/x)
            break
    else:
        #loop fell through finding a factor
        print(n, 'is a prime number')
print("   =========x=========\n")

#C stype for loop
#1,3,5,7,9
for i in range(1,10,2): #(start,end,step)
    print(i)