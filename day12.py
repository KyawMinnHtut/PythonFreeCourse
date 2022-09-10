profile = {
    "name":"Kyaw Min Htut",
    "age":30,
    "address":"Monywa"
}

#don't do this
for element in profile: #elementရဲ့ keyကို ပေး
    print(element, profile[element])

for key, value in profile.items(): #dici.items()နဲ့ elementတစ်ခုချင်းဆီခေါ်ပီး tuple unpackingလုပ်
    print(key, value)

#dict.get()
key = "Phone"
value = profile.get(key) #dict.get(key,ReturnValue)
print(value)

marks = profile.fromkeys(["Myanmar", "English", "Maths"], 40) #create a dictionary
print(marks)
marks.pop("Myanmar")
print(marks.pop("Myanmar", "Key not found")) #KeyErrorဖြစ် 
print(marks)

marks.popitem() #as lifo of pop in sequence
print(marks)

marks.update(English=75, Physics=75, Biology=67) #အဲ keyရှိရင် item update၊ မရှိရင် item insert 
print(marks)

#no returnဖြစ်ရင် Pythonက Default return valueအနေနဲ့ Noneကို ပြန်ပေးတယ်
def function():  #===> function header                       these two lines is
    print("This is function.") # ===> function body          function definition

function()   # ===> function call

#function with parameter passing and return a value
def small_number(a,b):
    if a < b:
        return a # return a value by conditional
    else:
        return b
result = small_number(10,20) #assign return value to a variable
print("The return value of small_number function is ", result)

def small_number(a,b):
    if a < b:
        return a,b
    else:
        return b,a # tupleနဲ့ valueတစ်ခုထက်ပိုပီး returnပြန်နိုင်
min, max = small_number(10,20)
print("Return values of a function with tuple unpacking", min, max)

#default arguments
def append(lst=[]):
    lst.append(100)
    return lst
my_list = [1,2,3,4,5]
print("List append", append(my_list))
print("List append", append()) #print မထုတ်ဘဲ variableတစ်ခုထဲ assignအရင်လုပ်ရင် ဒီလို errorမဖြစ်
print("List append", append())

#Variable Length Arguments  ==> နောက်ဆုံးမှာ ဖြစ်ရ
def sum_result(*varargs):
    print(type(varargs))
    return sum(varargs)
print("Sum result ", sum_result(1,2,3,4,5))

#Varargs is tuple = immutable
def update(a):
    a = a+1
my_num = 10
update(my_num)
print(my_num)  #can't modify the argument value but listလိုမျိုး objဖြစ်နေရင် reference passဖြစ်လို့ listကို modifyလုပ်လို့ရ