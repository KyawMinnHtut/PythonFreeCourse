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