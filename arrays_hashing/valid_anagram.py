import string
from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        cs, ct = defaultdict(int), defaultdict(int)
        for i in range(len(s)):
            cs[s[i]] = cs[s[i]] + 1
            ct[t[i]] = ct[t[i]] + 1

        print(cs)
        print(ct)
        return cs == ct

    def isPalindrome(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        j = len(t) - 1
        for i in range(len(s)):
            if s[i] != t[j]:
                return False
            j = j - 1
        return True


valid = Solution().isPalindrome("abc", "cba")
print(valid)
