import sys


def normal_round(num):
    if num - int(num) >= 0.5:
        return int(num) + 1
    return int(num)

n = int(sys.stdin.readline())
nums = []
sum_num = 0
if n == 0:
    print(0)
    exit(0)
for i in range(n):
    num = int(sys.stdin.readline())
    nums.append(num)
    sum_num += num

avg_num = normal_round(n * 0.15)
sorted_nums = sorted(nums)
if avg_num > 0:
    nums = sorted_nums[avg_num:-avg_num]

print(normal_round(sum(nums) / len(nums)))


# 제외할 수 계산
# 정렬 후 제외
# 평균계산
