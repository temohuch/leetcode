class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        dict = {}
        i = 0
        while i < len(strs):
            word = strs[i]
            for count in range(len(word)):
                if count in dict and word[count] == dict[count][-1]:
                    dict[count] += word[count]
                elif count not in dict:
                    dict[count] = word[count]
                count += 1
            i += 1
        print(dict)
        result = ""
        for key, value in dict.items():
            if len(value) == len(strs):
                result += value[0]
            else:
                break

        return result

s = Solution()
print(s.longestCommonPrefix(["cri","crcdi","crifs","ck"]))


