''' Задачи по материалам недели,
    включая тему 'Строки'
'''

# task 1
a = int(input())
b = int(input())
c = int(input())
p = (a + b + c) / 2
S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
print(S)

# task 2
num = int(input())
if -15 < num <= 12 or 14 < num < 17 or 19 <= num:
    print(True)
else:
    print(False)

# task 3
num1 = float(input())
num2 = float(input())
operation = input()

if operation == 'mod':
    if num2 == 0.0:
        print('Деление на 0!')
    else:
        print(num1 % num2)
elif operation == 'pow':
    print(num1 ** num2)
elif operation == 'div':
    if num2 == 0.0:
        print('Деление на 0!')
    else:
        print(num1 // num2)
elif operation == '+':
    print(num1 + num2)
elif operation == '-':
    print(num1 - num2)
elif operation == '/':
    if num2 == 0.0:
        print('Деление на 0!')
    else:
        print(num1 / num2)
elif operation == '*':
    print(num1 * num2)

# task 4
pi = 3.14
S = 0

figure = input()
a = float(input())

if figure == 'треугольник':
    b = float(input())
    c = float(input())
    p = (a + b + c) / 2
    S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
elif figure == 'прямоугольник':
    b = float(input())
    S = a * b
elif figure == 'круг':
    S = pi * a**2

print(S)

# task 5
a = int(input())
b = int(input())
c = int(input())

if a < b:
    a, b = b, a
if a < c:
    a, c = c, a
if b < c:
    c, b = b, c

print(a)
print(b)
print(c)

# task 6
n = int(input())
string = 'программист'

if (n % 10) == 1 and (n % 100) != 11:
    string = string
elif 2 <= (n % 10) <= 4 and not (11 <= (n % 100) <= 14):
    string += 'а'
else:
    string += 'ов'

print(n, string)

# task 7
ticket = int(input())

block1 = ticket // 1_000
block2 = ticket % 1_000

sumOne = (block1 // 100) + ((block1 % 100) // 10) + block1 % 10
sumTwo = (block2 // 100) + ((block2 % 100) // 10) + block2 % 10

if sumOne == sumTwo:
    print('Счастливый')
else:
    print('Обычный')
