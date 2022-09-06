import operator


my_tuple = ()  # tuple literal
my_list = range(0,10)
my_tuple = tuple(my_list)
print(my_tuple)
my_tuple = ([1,2,3], "Kyaw Min Htut", 3.3)
my_tuple[0].append(4)
print(my_tuple[0])

def division(num, divisor): #Error handlingအားကိုးရင် Software Engineeringနဲ့ မကိုက်
    if divisor == 0:
        return "Division by zero error",0
    else:
        return None, num/divisor
print(division(3,2))
print(division(3,0))     #Error handlingနဲ့ဖမ်းလို့ရသော်လည်း functionက သူ့ဘာသာ တာဝန်ယူသင့်၊

#Tuple unpacking
err, result = division(3,0) # as x,y,z = (a,b,c)
if not err:
    print("Result is ", result)
else:
    print("Error :", err)

#Tuple packing
def process(*argv):
    print(type(argv))
process(1,2,"Hello")

# {} is empty dictionary and set() function produces emplty set
my_string = """
Programming in Java
Programming in javascript with node
Programming in Python with django
"""
words = my_string.split()
print(words)
unique_words = set(words) #printထုတ်ကြည့်ရင် String orderအတိုင်းမဖြစ်တာ တွေ့ရ
for word in unique_words:
    print("Count ", word, " ==>", words.count(word))

results = [(word,words.count(word)) for word in unique_words]
results.sort(key=operator.itemgetter(1), reverse=True)
print("Sorted result ==>", results)

my_set = {1,2,3,5}
my_set.add(4)
print(my_set)
my_set.update([6,7,8,9,10])     #update()က iterable collectionဖြစ်မှ ရ
print(my_set)

#Set မှ elementတစ်ခု ဖယ်ထုတ်ခြင်း
element = 9
element in my_set and my_set.remove(element) #remove() methodကို error မထွက်ရန် member operator inနဲ့ စစ် ==။ not recommend
my_set.discard(9) # discard() not raise error message
print(my_set)

#Mathematical Operations on Set
print("Union ", {1,2,3} | {4,5,1}), {1,2,3}.union({4,5,1})
print("Intersection ", {1,2,3} & {4,5,1}), {1,2,3}.intersection({4,5,1})
print("Difference ", {1,2,3} - {4,5,1}), {1,2,3}.difference({4,5,1})