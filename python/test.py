#find()
str = "Welcome from Python Programming Welcome"
start_index = 0
count = 0
#implementation of count() by find() method
while str.find("Welcome") != -1:
    start_index = str.find("Welcome", start_index) + 1
    count = count + 1 
print("Total Count :", count)

my_list = []
my_tuple = ()
my_set = {}
my_dictionary = {}

my_list.append