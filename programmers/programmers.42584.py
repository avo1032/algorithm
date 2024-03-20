def solution(prices):
    n = len(prices)
    answer = [0] * n

    stack = [0]
    for i in range(1, n):
        while stack and prices[i] < prices[stack[-1]]:
            j = stack.pop()
            answer[j] = i - j
            # print(answer)
        stack.append(i)
        # print(stack)
    print(stack)
    while stack:
        j = stack.pop()
        answer[j] = n - 1 - j
        # print(answer)
    # print(answer)
    return answer


solution([1, 2, 3, 2, 3])

# 최초에는 비교대상이 없으므로 초기값 0을 스택에 푸쉬
# 스택의 값은 prices의 인덱스
