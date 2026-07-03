class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        sorted_words = sorted(strs)
        print(sorted_words)
        first = sorted_words[0]
        last = sorted_words[-1]
        min_words = min(len(first), len(last))
        result = ""
        for i in range(min_words):
            if first[i] == last[i]:
                result += last[i]
            else:
                break
        return result

s = Solution()
print(s.longestCommonPrefix(["flower","flow","flight"]))