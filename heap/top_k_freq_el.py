from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int):
        freq = {}
        rev = [[] for _ in range(len(nums))]
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)

        for n, c in freq.items():
            rev[c].append(n)

        res = []
        for i in range(len(rev) - 1, 0, -1):
            for n in rev[i]:
                res.append(n)
                if (len(res)) == k:
                    return res


print(Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2))
