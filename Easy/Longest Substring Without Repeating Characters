"""
a b c a b c b b  -  по сути 2 уникальные строки без повторов
По времени оценка будет O(n) потому что будет одна проходка по строке
По памяти нужно будет создать переменную, которая будет занимать память O(n) - по сути так, потому что в худшем случае мы пройдемся также по всей строке и сохраним ее в доп ячейку памяти

a - specialString = strs[:1] in 1 element -> b if b in specialString -> 

"""

class Solution:
    def lengthOfLongestSubstring(self, s):
        specitalString = ""
        i = 0
        max_count = 0
        for i in range(len(s)):

            if s[i] in specitalString:
                indx = specitalString.index(s[i])
                specitalString = specitalString[indx + 1:] + s[i]
            else:
                specitalString += s[i]
                if len(specitalString) > max_count:
                    max_count = len(specitalString)      

        return max_count

s = Solution()
print(s.lengthOfLongestSubstring(s = "abcabcbb"))