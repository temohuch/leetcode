class Solution:
    def romanToInt(self, s: str) -> int:
        same = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        sum = 0
        for i in range(len(s)):
            if i + 1 < len(s) and same[s[i]] < same[s[i+1]]:
                sum -= same[s[i]]
            else:
                sum += same[s[i]]

        return sum

s = Solution()
print(s.romanToInt("III"))