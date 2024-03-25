def solution(participant, completion):
    answer = ''
    doc = {}
    for i in completion:
        if doc.get(i):
            doc[i] += 1
        else:
            doc[i] = 1
    for j in participant:
        if doc.get(j) and doc.get(j) > 0:
            doc[j] -= 1
        else:
            answer = j
            break

    print(answer)
    return answer

solution(["leo", "kiki", "eden"], ["eden", "kiki"])