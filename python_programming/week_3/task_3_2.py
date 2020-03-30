''' 3.2 Словари '''

# task 1
def update_dictionary(d, key, value):
    if key in d:
        d[key].append(value)
    elif 2 * key in d:
        d[2 * key].append(value)
    else:
        d[2 * key] = [value]

# task 2
s = input().lower()
a = [i for i in s.split()]
map = {i: a.count(i) for i in a}

for key, value in map.items():
    print(key, value)

# task 3
# Считается, что функция f(x) уже реализована и доступна для вызова.
def f(x):
    pass

n = int(input())
map = {}
for i in range(n):
    x = int(input())
    if x not in map:
        map[x] = f(x)
    print(map[x])