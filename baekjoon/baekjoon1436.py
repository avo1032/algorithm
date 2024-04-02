n = int(input())

result = 0

while True:
    if '666' in str(result):
        n -= 1
    if n == 0:
        break
    result += 1

print(result)