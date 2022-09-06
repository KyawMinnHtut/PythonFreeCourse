#Sequence Comparison  (base typeမတူတာတော့ စစ်မရ)
"""
pairwise comparator = elementချင်းတိုက်
go next element if the elements are same
if list id shorter, then smaller
"""
print("[10,20] > [10,20,30]  : ", [10,20] > [10,20,30]) #len(first) > len(second)
print("[10,20] > [5,20,30]   : ", [10,20] > [5,20,30]) #10>5
print("[10,5] < [10,20,30]   : ", [10,5] < [10,20,30]) #5<20
print("[10,20] >= [10,20,30] : ", [10,20] >= [10,20,30]) #not equal so = is ignored

#Bitwise Operators = bit by bit
#print(bin(decimal_value))
print(6&8)      # 00000110 & 00001000 =   00000000
print(4|5)      # 00000100 | 00000101 =   00000101
print(6^8)      # 00000110 ^ 00001000 =   00001110  (^မှာ 1 1 ဆို 0)
print(~5)       # 00000101 + 00000001 = - 00000110  ~a = -(a+1)
print(10<<3)    # 00001010  ဘယ်ဘက်ကို 000နဲ့ တွန်း  =   1010000
print(10>>3)    # 00001010   ညာဘက်ကို 000နဲ့ တွန်း  =   0000001

#Parallel Assignment
#funမှာ valueတစ်ခုပဲ ပြန်၊ Pythonမှာ Tupleကို parallel assignmentနဲ့ valueတစ်ခုထက်မက returnပြန်ပေးနိုင်
#In some languages
x = 1
y = 2
temp = x #ခွက်အလွတ်ထဲ ခဏထည့်
x = y
y = temp
print(x, y)
#In python
x,y = y,x
print(x,y)
#Example usage
a = [10,20,30]
i=0
i,a[i] = 1,40
print(a)

#if as expression
a = 10
b = 20
maximum = a if a > b else b
print(maximum)

#Identity Operator ( is )
x = 10
y = 10
print(x is y) #same object as primitive obj
x = [1,2,3]
y = [1,2,3]
print(x is y) # cached mutable list
x = "String"
y = "String"
print(x is y) # same obj of cached immutable string