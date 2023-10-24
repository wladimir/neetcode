from collections import defaultdict


class Solution:
    def characterReplacement(self, s, k):
        # Initialize variables to keep track of the maximum substring length and character counts.
        max_length = 0
        max_count = 0
        start = 0  # Start of the sliding window.

        # Create a dictionary to store the count of each character in the window.
        char_count = {}

        for end in range(len(s)):
            # Update the count of the current character in the window.
            char = s[end]
            char_count[char] = char_count.get(char, 0) + 1

            # Update max_count with the maximum count of any character in the window.
            max_count = max(max_count, char_count[char])

            # Calculate the number of replacements needed to make the window valid.
            replacements_needed = (end - start + 1) - max_count

            # If the number of replacements needed is greater than k, we need to shrink the window.
            if replacements_needed > k:
                # Move the window's starting position.
                char_count[s[start]] -= 1
                start += 1

            # Update the maximum substring length.
            max_length = max(max_length, end - start + 1)

        return max_length

    def characterReplacement2(self, s: str, k: int) -> int:
        if not s:
            return 0

        left = right = 0
        max_count = 0
        max_len = 0
        count = defaultdict(int)

        while right < len(s):
            count[s[right]] += 1

            # max count is the count of the most frequent character in the current window
            max_count = max(max_count, count[s[right]])
            # if length of substring - max_count > k, then we need to shrink the window
            if right - left + 1 - max_count > k:
                count[s[left]] -= 1
                left += 1
            max_len = max(max_len, right - left + 1)
            right += 1
        return max_len


s = "ABAB"
k = 2
print(Solution().characterReplacement(s, k))  # Output: 4
print(Solution().characterReplacement(s, k))  # Output: 4
