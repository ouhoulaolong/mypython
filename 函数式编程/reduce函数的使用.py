from functools import reduce


def add(a,b):
    return a+b

sum = reduce(add,[1,3,5,7,9])
print(sum)