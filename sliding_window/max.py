import collections
from collections import deque
from typing import List, Type


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []  # indices
        window = collections.deque()

        for i in range(len(nums)):
            left = i - k + 1

            while window and window[0] < left:
                window.popleft()

            while window and nums[window[-1]] < nums[i]:
                window.pop()

            window.append(i)

            if i >= k - 1:
                result.append(nums[window[0]])

        return result


print(Solution().maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
