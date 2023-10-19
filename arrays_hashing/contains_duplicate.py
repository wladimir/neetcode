from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = {}

        for n in nums:
            if n in seen.keys():
                return True
            seen[n] = True
        return False


print(Solution().containsDuplicate([1, 2, 3, 3]))
