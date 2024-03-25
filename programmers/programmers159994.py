def solution(cards1, cards2, goal):
    answer = 'Yes'
    for target in goal:
        if len(cards1) > 0 and cards1[0] == target:
            cards1.pop(0)
        elif len(cards2) > 0 and cards2[0] == target:
            cards2.pop(0)
        else:
            answer = "No"
    return answer

solution(["i", "water", "drink"], ["want", "to"], ["i", "want", "to", "drink", "water"]	)