''' 2.2 Операторы break, continue '''

# task 1
while 1:
    i = int(input())
    if i < 10:
        continue
    elif i > 100:
        break
    print(i)