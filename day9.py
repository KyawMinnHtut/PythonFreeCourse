from curses.ascii import isdigit

#Using Type Checking for String Input
num_str = input("Enter number :")
while not num_str.isdigit():
    num_str = input("Please Enter Number :")
num = int(num_str)
print("Number", num)

price = 12
quantity = 3
total = price * quantity
print("price is", price,", quantity is", quantity, "and total =", total) #print ထုတ်ရာမှာ အဆင်ပြေ
print("price is {}, quantiy is {} and total is {}".format(price, quantity, total)) #fileမှာ သွားရိုက်တဲ့ အခါ အဆင်ပြေ
print("quantity is {1}, price is {0} and total is {2}".format(price, quantity, total))
print("price is {p}, quantiy is {q} and total is {t}".format(p=price, q=quantity, t=total))

#reverse the order of words
str = input("Enter String :")
words = str.split()
rts = ' '.join(words[::-1])
print(rts)

#reverse internal words
#by one line
print(' '.join([w[::-1] for w in str.split()]))
  
#as book
reverse_words = []
for word in words:
    reverse_words.append(word[::-1])
reverse_str = ' '.join(reverse_words)
print(reverse_str)

#book example
str_list = str.split()
reverse_list = []
i = len(str_list)-1
while i >= 0:
    reverse_list.append(str_list[i])
    i=i-1
opt=' '.join(reverse_list)
print(opt)


