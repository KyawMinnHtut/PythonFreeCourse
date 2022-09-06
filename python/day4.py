decimal_literal = 100
binary_literal = 0b100
octal_literal = 0o100
hexadecimal_literal = 0x100

print(decimal_literal)
print(binary_literal)
print(octal_literal)
print(hexadecimal_literal)

print(bin(4))
print(oct(64))
print(hex(256))

print(bin(binary_literal))
print(oct(octal_literal))
print(hex(hexadecimal_literal))
print("   =========x=========\n")

str_with_single_quote = 'Hello. "Welcome from my channel." I\'m Kyaw Min Htut.' # escape character is used
str_with_double_quote = "Hello. 'Welcome from my channel.' I'm Kyaw Min Htut."
print(str_with_single_quote)
print(str_with_double_quote)
print("   =========x=========\n")

#Type Casting
my_str = "123"
my_num = 10
print("my_str + my_num = ", int(my_str)+my_num)
print("string concat for my_str and my_num is", my_str+str(my_num))
print("   =========x=========\n")
 
x = 150000
y = 150000
print(x is y) #is should be used to check same memory address or not, id() should not be used
print (id(x), id(y), id(150000))
print(hex(x), hex(y), hex(150000))
print(hex(id(x)), hex(id(y)), (hex(id(150000))))
print("   =========x=========\n")

x = [3,6,8,10]
y = bytes(x)
print(type(x))
print(type(y))
print(y[0])
#y[0]=1 bytes type ဖြစ်လို့ assignလုပ်လို့ မရ၊
z = bytearray(x)
print(type(z))
print("original bytearray z[0] :",z[0])
z[0]=1
print("after updating z[0] :", z[0])
print("   =========x=========\n")

x = range(3)
for i in x:
    print(i)
x = range(1,6)
for i in x:
    print(i)
