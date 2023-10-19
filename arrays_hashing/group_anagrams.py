from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for s in strs:
            sortedWord = ''.join(sorted(s))
            if sortedWord in anagrams:
                anagrams[sortedWord].append(s)
            else:
                anagrams[sortedWord] = [s]
        print(anagrams)
        return list(anagrams.values())


solution = Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
print(solution)
