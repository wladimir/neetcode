from typing import List


class Solution:
    def topKFrequent1(self, nums: List[int], k: int):
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        res = []
        for item in freq[:k]:
            res.append(item[0])
        return res

    def topKFrequent2(self, nums: List[int], k: int):
        res = [[] for _ in range(len(nums) + 1)]

        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        for key, val in freq.items():
            res[val].append(key)

        val = []
        for i in range(len(res) - 1, 0, -1):
            if len(res[i]) > 0:
                for r in res[i]:
                    val.append(r)
                    if len(val) == k:
                        return val


print(Solution().topKFrequent2([1, 1, 1, 2, 2, 3], 2))
