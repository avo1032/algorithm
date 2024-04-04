import sys


n = int(input())

for i in range(n):
    data = sys.stdin.readline().rstrip()
    answer = 'NO'
    stack = []
    for j in data:
        if j == ")":
            if not stack:
                break
            elif stack[-1] == "(":
                stack.pop()
            else:
                break
        if j == "(":
            stack.append(j)
    else:
        if not stack:
            answer = 'YES'
    print(answer)