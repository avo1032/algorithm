bar = input()

stack = []
answer = 0

for i in range(len(bar)):
    if bar[i] == '(':
        stack.append('(')
    else:
        stack.pop()
        if bar[i-1] == '(':  # 레이저일 때
            answer += len(stack)
        else:  # 막대기의 끝일 때
            answer += 1

print(answer)