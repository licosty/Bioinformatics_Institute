''' Задачи по материалам недели '''

# task 1
sumNum = int(input())
sumQ = sumNum**2

while sumNum:
    i = int(input())
    sumNum += i
    sumQ += i**2

print(sumQ)

# task 8
n = int(input())
i = 1
count = 0
while i <= n:
    for j in range(i):
        if count >= n:
            break
        print(i, end=' ')
        count += 1
    i += 1

# task 7
lst = [int(i) for i in input().split()]
x = int(input())

if x not in lst:
    print('Отсутствует')
for k in range(len(lst)):
    if x == lst[k]:
        print(k, end=' ')

# task 6
mat = []

while 1:
    s = [i for i in input().split()]
    if 'end' in s:
        break
    mat.append(s)

for i in range(len(mat)):
    for j in range(len(mat[0])):
        xL = int(mat[i-1][j])
        if i+1 >= len(mat):
            xR = int(mat[0][j])
        else:
            xR = int(mat[i + 1][j])
        yT = int(mat[i][j-1])
        if j+1 >= len(mat[0]):
            yB = int(mat[i][0])
        else:
            yB = int(mat[i][j + 1])
        print((xL + xR + yT + yB), end=' ')
    print()



# task 5
b = int(input())
n = b

a = [[0 for i in range(n)] for j in range(n)]
num = 1

i = 0
j = 0

while num <= b*b:
    m = i
    while m < n:
        a[i][m] = num
        num += 1
        m += 1
    i += 1

    k = i
    m = n - 1
    while k < n:
        a[k][m] = num
        num += 1
        k += 1
    n -= 1

    k = n
    m = i + 1
    while m < (n + 2):
        a[k][-m] = num
        num += 1
        m += 1

    k = i + 1
    while k < (n + 1):
        a[-k][j] = num
        num += 1
        k += 1
    j += 1

for i in range(b):
    for j in range(b):
        print(a[i][j], end=' ')
    print()