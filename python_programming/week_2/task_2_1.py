''' 2.1 Цикл while '''

# task 1
i = int(input())
sumNum = i

while i != 0:
    i = int(input())
    sumNum += i

print(sumNum)

# task 2
a = int(input())
b = int(input())
i = 1
d = a * b

while i % a or i % b:
    i += 1
    d = i

print(d)