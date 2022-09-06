my_list = []
my_list.append(10)  #in js => .push()
my_list.append(20)
print(my_list)
my_list.pop()
my_list.pop()
print(my_list)

#xml validate with stack data structure
xml_str = """<message>
    <body>
        Something
        <p>
        Other thing
        </p>
    </body>
</message>"""
stack = []
valid = True
lines = xml_str.splitlines()
for line in lines:
    line = line.strip()
    if line.startswith("</"):
        tag = line[2:-1]
        pop_tag = stack.pop()
        if tag != pop_tag:
            valid = False
            break
    elif line.startswith("<"):
        tag = line[1:-1]
        stack.append(tag)
    else:
        pass
if valid == False:
    print("Invalid")
elif len(stack) == 0:
    print("Valid")
else:
    print("Valid")

#disassembly
import dis
a = 2
b = 3
c = 4
def fun():
    d = a + b * c
    return d
print(dis.dis(fun))
#by ByteCode
execution_stack=[]
variables = {
    "a":2,
    "b":3,
    "c":4
}
# variables = globals() # အပေါ်က dictionaryပုံစံဖြင့် သိမ်းထားသော global variablesတွေကို ပြန်လည် assignပေး
byte_codes = [  ("LOAD_GLOBAL","a"),
                ("LOAD_GLOBAL","b"),
                ("LOAD_GLOBAL","c"),
                ("BINARY_MULTIPLY",),
                ("BINARY_ADD",)
                ]
for byte_code in byte_codes:
    op_code = byte_code[0]
    if op_code == "LOAD_GLOBAL":
        var_name = byte_code[1]
        operand = variables[var_name]
        execution_stack.append(operand)
    elif op_code == "BINARY_MULTIPLY":
        operand_two = execution_stack.pop()
        operand_one = execution_stack.pop()
        execution_stack.append(operand_one * operand_two)
    elif op_code == "BINARY_ADD":
        operand_two = execution_stack.pop()
        operand_one = execution_stack.pop()
        execution_stack.append(operand_one + operand_two)
    else:
        print("Unknown Code")
print("Result ", execution_stack.pop())

#Nested List
n_list = [[1,2,3],[4,5,6],[7,8,9]]
print(n_list)
print(n_list[0][1])
for l in n_list:
    for item in l:
        print(item)
for i, l in enumerate(n_list):
    for j, item in enumerate(l):
        print(item)

#List Comprehension = create a new list from a list
list_one = [1,2,3,4,5]
list_two = []
for item in list_one:
    list_two.append(item*2)
list_three = [x**2 for x in list_one]
print(list_one)
print(list_two)
print(list_three)

fruits = ["apple", "banana", "orange"]
tuple_fruits = [(x.upper(), len(x)) for x in fruits if len(x)>5]
print(tuple_fruits)

marks = [("Myanmar",30),("English",40),("Maths", 70)]
pass_subject = [subject for subject in marks if subject[1]>=40]
print(pass_subject)
if len(marks) == len(pass_subject):
    print("Pass the exam")
else:
    print("Fail the exam")

my_tuple = "Kyaw Min Htut", 30
print(my_tuple)
print(my_tuple[0])
print(my_tuple[1])
# , လေးမပါရင် String ဖြစ်သွားလိမ့်မယ်
name_string = "Kyaw Min Htut"
name_tuple = "Kyaw Min Htut",
print('"Kyaw Min Htut" is ',type(name_string))
print('"Kyaw Min Htut", is ',type(name_tuple))