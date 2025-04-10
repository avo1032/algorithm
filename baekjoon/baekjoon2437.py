n = int(input())
weights = list(map(int, input().split()))
weights.sort()

target = 1  # 만들고자 하는 최소 무게
for weight in weights:
    if target < weight:
        break
    target += weight

print(target)