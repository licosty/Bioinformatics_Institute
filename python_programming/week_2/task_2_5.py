''' 2.5 Списки '''

# task 1
print(sum(int(i) for i in input().split()))

# task 2
listNum = [int(i) for i in input().split()]

if len(listNum) == 1:
    print(listNum[0])
else:
    for i in range(len(listNum)):
        print(listNum[i-1] + listNum[(i+1) % len(listNum)], end=' ')


# task 3
listNum = [i for i in input().split()]
listNum.sort()

i = 0
while i < len(listNum):
    if listNum.count(listNum[i]) > 1:
        print(listNum[i], end=' ')
        i += listNum.count(listNum[i])
    else:
        i += 1