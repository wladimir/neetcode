from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        pCount, sCount = {}, {}
        res = []

        for i in range(len(p)):
            pCount[p[i]] = 1 + pCount.get(p[i], 0)
            sCount[s[i]] = 1 + sCount.get(s[i], 0)

        if pCount == sCount:
            res = [0]

        left = 0
        for right in range(len(p), len(s)):
            sCount[s[right]] = 1 + sCount.get(s[right], 0)
            sCount[s[left]] -= 1

            if sCount[s[left]] == 0:
                del sCount[s[left]]

            left += 1

            if pCount == sCount:
                res.append(left)

        print(res)
        return res


Solution().findAnagrams("ab", "ba")
