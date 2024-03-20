def solution(s):
    answer = -1
    stack = []
    for word in s:
        if not stack:
            stack.append(word)
        elif stack[-1] == word:
            stack.pop()
        else:
            stack.append(word)
    else:
        answer = 1 if not stack else 0
    return answer

# 스택이 비어있으면 현재 단어를 채움
# 현재 단어가 스택에 있는 단어와 같으면 스택 pop
# 마지막에 스택이 비어있으면 1, 비어있지 않으면 0