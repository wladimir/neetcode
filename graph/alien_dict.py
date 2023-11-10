from typing import (
    List,
)


class Solution:
    def alien_order(self, words: List[str]) -> str:
        adj = {c: set() for word in words for c in word}

        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]

            min_len = min(len(word1), len(word2))
            if len(word1) > len(word2) and word1[:min_len] == word2[:min_len]:
                return ""

            for j in range(min_len):
                if word1[j] != word2[j]:
                    adj[word1[j]].add(word2[j])
                    break

        seen = {}
        output = []

        def dfs(node):
            if node in seen:
                return seen[node]

            seen[node] = True
            for nei in adj[node]:
                if dfs(nei):
                    return True

            seen[node] = False
            output.append(node)

        for char in adj:
            if dfs(char):
                return ""

        output.reverse()
        return "".join(output)
