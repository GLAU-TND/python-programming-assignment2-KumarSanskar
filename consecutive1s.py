a = int(input())  # takes input in integer
b = bin(a).split("0")  # splits the input separated by "0" and creates a list b
b = b[2:]  # starts moving inlist from position 2
d = map(len, b)  # maps length to each element of b
e = max(d)  # after mapping extracts the one with  the maximum length
print(e)