from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        letters = {}
        for char in s:
            letters[char] = letters.get(char, 0) + 1

        print(letters)

        for char in t:
            if char not in letters:
                return False
            letters[char] -= 1
            if letters[char] == 0:
                del letters[char]

        print(letters)

        return len(letters) == 0


print(Solution().isAnagram("anagram", "nagaram"))
