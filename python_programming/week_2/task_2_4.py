''' 2.4 Строки и символы '''

# task 1
s = input().upper()

result = (s.count('G') + s.count('C')) / len(s) * 100
print(result)

# task 2
s = input()
result = ''
count = 1

if len(s) == 1:
    result = s + '1'
for c in range(len(s)-1):
    if s[c] == s[c+1]:
        count += 1
    else:
        result += s[c] + str(count)
        count = 1

    if c == len(s) - 2:
        result += s[c+1] + str(count)

print(result)