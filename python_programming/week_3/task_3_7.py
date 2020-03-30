''' Задачи по материалам недели '''

# task 1
games = int(input())
team = {}
for i in range(games):
    a = input().split(';')
    if int(a[1]) < int(a[3]):
        team[a[0]] = team.get(a[0], []) + [0]
        team[a[2]] = team.get(a[2], []) + [3]
    elif int(a[1]) == int(a[3]):
        team[a[0]] = team.get(a[0], []) + [1]
        team[a[2]] = team.get(a[2], []) + [1]
    else:
        team[a[0]] = team.get(a[0], []) + [3]
        team[a[2]] = team.get(a[2], []) + [0]

win, los, draw, sum = 0, 0, 0, 0
for key, value in team.items():
    for i in value:
        if i == 3:
            win += 1
            sum += 3
        if i == 0:
            los += 1
        if i == 1:
            draw += 1
            sum += 1
    print(key + ':', len(value), win, draw, los, sum)
    win, los, draw, sum = 0, 0, 0, 0

# task 2
code_p1, code_p2 = input(), input()
s1, s2 = input(), input()

code = dict(zip(code_p1, code_p2))

for i in s1:
    for key, value in code.items():
        if i == key:
            print(value, end='')
            break
print()
for i in s2:
    for key, value in code.items():
        if i == value:
            print(key, end='')
            break

# task 3
d = int(input())
uniq = [input().lower() for i in range(d)]
l = int(input())

lists = []
for i in range(l):
    lists += [i for i in input().lower().split() if i not in uniq]
for i in set(lists):
    print(i)

# task 4
commands = {'север': 1, 'запад': -1, 'юг': -1, 'восток': 1}
x, y = 0, 0
for i in range(int(input())):
    key, value = input().split()
    if key == 'север' or key == 'юг': y += (commands[key] * int(value))
    if key == 'восток' or key == 'запад': x += (commands[key] * int(value))
print(x, y)

# task 5
with open("E:/dataset_3380_5.txt") as rfile:
    students = {i: {} for i in range(1, 12)}

    for line in rfile:
        d = line.split('\t')
        students[int(d[0])][d[1]] = d[2].strip()

for key, value in students.items():
    size = 0
    for v in value.values():
        size += int(v)
    if not size:
        print(key, '-')
    else:
        print(key, size / len(value))