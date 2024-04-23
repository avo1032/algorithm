import sys


[n, k] = list(map(int, input().split()))

nums_list = [int(sys.stdin.readline()) for i in range(n)]
start = 1
end = max(nums_list)

while start <= end:
    mid = (start + end) // 2
    LANS = 0
    for j in nums_list:
        LANS += j // mid

    if LANS >= k:
        start = mid + 1
    else:
        end = mid - 1
print(end)
