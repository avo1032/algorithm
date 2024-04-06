import sys


while True:
    data = sys.stdin.readline().rstrip()
    stack = ["1"]
    answer = "yes"
    if data == ".":
        break
    for i in data:
        if i == "[" or i == "(":
            stack.append(i)
        if i == "]":
            if stack[-1] == "[":
                stack.pop()
            else:
                answer = "no"
                break
        if i == ")":
            if stack[-1] == "(":
                stack.pop()
            else:
                answer = "no"
                break
    if len(stack) > 1:
        answer = "no"
    print(answer)