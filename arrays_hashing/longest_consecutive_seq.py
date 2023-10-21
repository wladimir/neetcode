from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0

        for num in nums:
            if num - 1 not in nums:  # start of sequence
                curr = num
                sequence = 1

                while curr + 1 in nums:
                    curr += 1
                    sequence += 1

                res = max(res, sequence)
                # time complexity: O(n) because we only visit each number once
                # space complexity: O(n) because we store all numbers in a set

        return res
