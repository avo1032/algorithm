def is_correct_word(words):
    stack = []
    for word in words:
        if word == "(" or word == "{" or word == "[":
            stack.append(word)
            continue
        else:
            if not stack:
                return False
        
        if word == ")" and stack[-1] == "(":
            stack.pop()
        elif word == "}" and stack[-1] == "{":
            stack.pop()
        elif word == "]" and stack[-1] == "[":
            stack.pop()
    else:
        if not stack:
            return True
        else:
            return False

def swift_word(words):
    return words[1:] + words[0]

def solution(s):
    answer = 0
    for i in range(len(s)):
        if is_correct_word(s):
            answer += 1
        s = swift_word(s)
    return answer
