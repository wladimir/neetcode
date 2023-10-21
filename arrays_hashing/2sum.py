from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = {}
        for i, num in enumerate(nums):  # 0, 2; 1, 7
            v = target - num  # 9 - 2 = 7; 2
            if v in complements:
                return [complements[v], i]
            complements[num] = i  # {7: 0}; {2: 1}

        return []


# nums = [2,7,11,15], target = 9
# output = [0, 1]
print(Solution().twoSum([2, 7, 11, 15], 9))
