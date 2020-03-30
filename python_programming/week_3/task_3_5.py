''' 3.5 Модули '''

# task 1
from math import *

r = float(input())
print(2 * pi * r)

# task 2
from sys import argv
for i in argv[1:]:
    print(i, end=' ')