class Solution:
    def romanToInt(self, s: str) -> int:
        same = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000, "IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
        number = list(str(s))
        sum = 0
        i = 0
        while i < len(number):
            if i+1 < len(number):
                if (number[i+1] == "V" or number[i+1] == "X") and number[i] == "I":
                    number[i] = number[i] + number[i+1]
                    del number[i+1]
                elif (number[i+1] == "L" or number[i+1] == "C") and number[i] == "X":
                    number[i] = number[i] + number[i+1]
                    del number[i+1]
                elif (number[i+1] == "D" or number[i+1] == "M") and number[i] == "C":
                    number[i] = number[i] + number[i+1]
                    del number[i+1]
            sum += same[number[i]]
            i += 1
        return sum

s = Solution()
print(s.romanToInt("LVIII"))
