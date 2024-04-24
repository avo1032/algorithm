n = int(input())

result = 0
a = 1
now = 0
while True:
    if n <= (result * 6) + a:
        result += 1
        break
    else:
        a = a + (result * 6)
        result += 1

print(result)
