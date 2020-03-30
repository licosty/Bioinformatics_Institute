''' Решение заданий по темам:
    1.9 Логические операции, операции сравнения
    1.10 Условия if, else, elif
'''

# task 1
A = int(input())
B = int(input())
H = int(input())
if A <= H <= B:
    print('Это нормально')
elif H < A:
    print('Недосып')
else:
    print('Пересып')

# task 2
year = int(input())
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('Високосный')
else:
    print('Обычный')