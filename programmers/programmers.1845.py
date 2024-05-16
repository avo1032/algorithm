def solution(nums):
    answer = 0
    set_nums = set(nums)
    max_answer = len(nums) // 2
    if len(set_nums) > max_answer:
        return max_answer
    else:
        return len(set_nums)

print(solution([3,1,2,3]))

# nums = [3,1,2,3]