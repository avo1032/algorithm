from collections import deque

[N, K] = list(map(int, input().split()))

queue = deque(range(1, N+1))
result = "<"
while len(queue) > 0:
    queue.rotate(-(K-1))
    pop = queue.popleft()
    if result == "<":
        result += str(pop)
    else:
        result += f", {pop}"
result += ">"
print(result)