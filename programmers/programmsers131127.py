def solution(want, number, discounts):
    answer = 0
    doc = { }
    target = { }
    for index, want in enumerate(want):
        target[want] = number[index]
    lastQueue = []

    for i, discount in enumerate(discounts):
        if i < 9:
            if doc.get(discount) == None:
                doc[discount] = 1
            else:
                doc[discount] += 1
        elif i == 9:
            if doc.get(discount) == None:
                doc[discount] = 1
            else:
                doc[discount] += 1
            if doc == target:
                answer += 1
        else:
            deleted = discounts[i-10]
            if doc[deleted] > 1:
                doc[deleted] -= 1
            else:
                del doc[deleted]

            if doc.get(discount) == None:
                doc[discount] = 1
            else:
                doc[discount] += 1
            
            if doc == target:
                answer += 1
            # print(doc)
    print(answer)
    return answer

solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1], ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"])

# target = { "banana" : 1, "apple": 1 }
# target2 = { "banana" : 1, "apple": 2 }
# print(target == target2)