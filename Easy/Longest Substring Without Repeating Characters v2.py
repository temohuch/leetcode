class Solution(object):
    def lengthOfLongestSubstring(self, s):
        result = 0
        left = 0
        special_letter = set()

        for right, right_letter in enumerate(s):
            while right_letter in special_letter:
                special_letter.remove(s[left])
                left += 1

            special_letter.add(right_letter)
            result = max(result, right - left + 1)

        return result

s = Solution()
print(s.lengthOfLongestSubstring(s = "abcabcbb"))