n = int(input())
stack, answer, find, now = [], [], True, 1
for i in range(n):
    num = int(input())
    while num >= now:
        stack.append(now)
        answer.append('+')
        now += 1
    if stack[-1] == num:
        stack.pop()
        answer.append('-')
    else:
        find = False
if not find:
    print("NO")
else:
    for j in answer:
        print(j)