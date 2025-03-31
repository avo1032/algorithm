from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums);
        return [num for num, freq in count.most_common(k)];

if __name__ == "__main__":
    # 예제 입력
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    solution = Solution()
    result = solution.topKFrequent(nums, k)
    print(result)