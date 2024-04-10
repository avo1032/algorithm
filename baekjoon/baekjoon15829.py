n = int(input())
words = input()

answer = 0
num = 0
for i in words:
    addNum = (ord(i) - 96) * (31 ** num)
    answer += addNum
    num += 1

print(answer)