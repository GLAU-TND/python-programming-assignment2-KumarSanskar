lst1 = eval(input())  # takes input from user as ,separated value
lst_new = list(map(str, lst1))  # maps the items into a list
from itertools import permutations  # imports permutation from itertools module
a = list(permutations(lst_new))
max = 0
for i in a:
    b = ""
    for j in i:
        b = b + j
    if int(b)>max:
        max = int(b)
print(max)

