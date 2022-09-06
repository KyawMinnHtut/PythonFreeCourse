from curses.ascii import isdigit


key = input("Please enter a number or a keyword : ")
if key.isdigit():
    key = int(key)
    print("Your Decimal number in Binary        = {0:b}".format(key))
    print("Your Decimal number in Octal         = {0:o}".format(key))
    print("Your Decimal number in Hexadecimal   = {0:x}".format(key))
else:
    key = ord(key)
    print("Your keyword in Binary        = {}".format(bin(key)))
    print("Your keyword in Octal         = {}".format(oct(key)))
    print("Your keyword in Hexadecimal   = {}".format(hex(key)))
