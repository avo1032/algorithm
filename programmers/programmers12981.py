def solution(n, words):
    answer = []
    words_list = []
    target_i = -1
    for i, word in enumerate(words):
        if i == 0:
            words_list.append(word)
            continue
        if not word[0] == words[i-1][::-1][0]:
            target_i = i
            break
        if word in words_list:
            target_i = i
            break
        words_list.append(word)
    a = 0
    b = 0
    if not target_i == -1:
        a = (target_i % n) + 1
        b = (target_i // n) + 1
        answer = [a, b]
    else:
        answer = [0, 0]
    return answer


print(
    solution(
        2, 	["hello", "one", "even", "never", "now", "world", "draw"]
    )
)