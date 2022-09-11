#File Handling
#Write
# note_file = open("note.txt", "w")
# print("filename == > ", note_file.name)
# print("file mode ==> ", note_file.mode)
# print("file is readable? ==> ", note_file.readable())
# print("file is writeable? ==> ", note_file.writable())
# print("file is closed? ==> ", note_file.closed)
# note_file.write("Hello")
# note_file.write(" From Python\r\n")
# for i in range(1,11):
#     note_file.write(str(i)+"\r\n")
# note_file.close() # prevent memory leak
# print("file is closed? ==> ", note_file.closed)

#Append
# with open("note.txt", "a") as note_file:      #open file by with ... as automatically close the file
#   note_file.writelines("Append Hello")
#   print("file is closed? ==> ", note_file.closed)

#Read
# with open("note.txt", "r") as note_file:
#     chars = note_file.read(17)      #read character by character from file
#     print(chars)
#     print(note_file.readline())   #read line by line in the file by pointer
#     print(note_file.readline())
#     print(note_file.readline())
#     lines = note_file.readlines() #read lines in the file by pointer and retrun as a list
#     for line in lines:
#         print(line, end='')

#tell() and seek()
# text = "Kyaw Min Htut is a teacher"
# file = open("note.txt", "w")
# file.write(text)
# with open("note.txt", "r+") as file:
#     line = file.read()
#     print(line)
#     print("Current position : ", file.tell())
#     file.seek(14)
#     print("Current Cursor Position after seek() : ", file.tell())
#     file.write(" was a student.")
#     file.seek(0)
#     line = file.read()
#     print(line)

# import os
# file_name = "note.txt"
# if os.path.isfile(file_name):
#     print("File exist")
# else:
#     print("File does not exist")

#Handling Binary Data
# with open("python.jpg", "rb") as original_image:
#     bytes = original_image.read()
# with open("newpython.jpg", "wb") as new_image:
#     new_image.write(bytes)

#Handling CSV files (with writer, reader)
# import csv
# with open("data.csv", "r") as file: #change file mode
    # writer = csv.writer(file)
    # id = int(input("Enter id : "))
    # name = input("Enter name : ")
    # age = int(input("Enter age : "))
    # writer.writerow([id,name,age])  #.wrterows လဲရှိ

#     reader = csv.reader(file)
#     data = list(reader)
#     for item in data:
#         print("Item : ", item)

# from zipfile import *

#zip
# zip = ZipFile("test.zip", "w", ZIP_DEFLATED)
# zip.write("note.txt")
# zip.write("data.csv")
# zip.close()

#unzip
# files = ZipFile("test.zip", "r", ZIP_STORED)
# names = files.namelist()
# for name in names:
#     print("File name : ", name)
#     with open(name, "r") as file:
#         print("File data is :", file.read())

