class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """

    def encode(self, strs):
        return ''.join(map(lambda s: f"{len(s)}#{s}", strs))

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """

    def decode(self, str):
        res = []
        i = 0

        while i < len(str):
            j = i
            while str[j] != '#':
                j += 1
            length = int(str[i:j])
            k = j + 1
            l = k + length
            res.append(str[k:l])
            i = l

        return res


print(Solution().encode(["lint", "code", "love", "you"]))
print(Solution().decode("4#lint4#code4#love3#you"))
