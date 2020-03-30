''' 3.1 Функции '''

# task 1
''' Находит f от x '''
def f(x):
    if x <= -2:
        return 1 - (x + 2) ** 2
    elif -2 < x <= 2:
        return -x / 2
    elif 2 < x:
        return (x - 2) ** 2 + 1


# task 2
''' Удаляет из списка целых чисел все нечётные значения,
    а чётные нацело делит на два
'''
def modify_list(l):
    l[:] = [i // 2 for i in l if i % 2 == 0]


