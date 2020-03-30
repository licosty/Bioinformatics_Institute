''' Решение заданий по темам:
    1.5 Операции с целыми числами
    1.6 Операции с вещественными числами
    1.7 Типы данных
    1.8 Переменные. Стандартный ввод/вывод
'''

# task 1
X = int(input())
Y = int(input())
print(X*60 + Y)

# task 2
X = int(input())
print(X // 60)
print(X % 60)

# task 3
X = int(input())
H = int(input())
M = int(input())
wakeUp = H * 60 + M + X
print(wakeUp // 60)
print(wakeUp % 60)