''' 2.3 Цикл for '''

# task 1
a = int(input())
b = int(input())
c = int(input())
d = int(input())

for k in range(c, d + 1):
    print('\t', k, end='')
print()

for i in range(a, b + 1):
    print(i, end='\t')
    for j in range(c, d + 1):
        print(i * j, end='\t')

    print()

# task 2
a = int(input())
b = int(input())

mid = 0
count = 0

for i in range(a, b+1):
    if i % 3 == 0:
        mid += i
        count += 1

print(mid/count)