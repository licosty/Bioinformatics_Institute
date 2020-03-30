''' 3.4 Файловый ввод/вывод '''

# task 1
with open("E:/dataset_3363_2.txt") as rfile:
    with open("E:/text.txt", 'w') as wfile:

        s = rfile.readline()

        abc = ''
        count = ''
        for i in range(len(s)):
            if s[i] >= 'A':
                abc = s[i]
            else:
                count += s[i]
                if i + 1 < len(s):
                    if s[i+1] >= 'A':
                        for j in range(int(count)):
                            wfile.write(abc)
                        abc = ''
                        count = ''
                else:
                    for j in range(int(count)):
                        wfile.write(abc)

# task 2
with open("E:/dataset_3363_3.txt") as rfile:
    s = []
    for line in rfile:
        s += line.lower().strip().split()

    map = {i: s.count(i) for i in set(s)}

    m = 1
    k = ''
    for key in map:
        if map[key] > m:
            m = map[key]
            k = key
        elif map[key] == m:
            if k > key:
                k = key
                m = map[key]
    print(k, m)

# task 3
with open("E:/dataset_3363_4.txt") as rfile, open("E:/text.txt", 'w') as wfile:
    students = []
    for line in rfile:
        s = line.strip().split(';')
        students.append(s)
        wfile.write(str((int(s[1]) + int(s[2]) + int(s[3])) / 3) + '\n')

    n, m = len(students), len(students[0])
    sum = 0
    for j in range(1, m):
        for i in range(n):
            sum += int(students[i][j])
        wfile.write(str(sum / n) + ' ')
        sum = 0