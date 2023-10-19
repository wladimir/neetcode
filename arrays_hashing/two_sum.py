from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, n in enumerate(nums):
            diff = target - n
            print(diff, target, n, seen)
            if diff in seen:
                return [seen[diff], i]
            seen[n] = i
            print(seen)


s = Solution().twoSum([2, 7, 11, 15], 9)
print(s)
