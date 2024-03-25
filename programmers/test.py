from collections import deque

def solution(N, K):
    queue = deque(range(1, N + 1))

    while len(queue) > 1:
        for _ in range(K - 1):
            queue.append(queue.popleft())
            queue.popleft()
    return queue[0]

print(solution(5, 2))


dic = { }
participant = ["leo", "kiki", "eden"]

dic["leo"] = 1
dic["kiki"] = 1
print(dic)
dic["leo"] = 1
print(dic.get("af"))