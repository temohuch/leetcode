class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')': '(', ']': '[', '}': '{'}
        memory = []

        if len(s) % 2 != 0:
            return False

        for symb in s:
            if symb in pairs.keys() and len(memory) > 0 and memory[-1] == pairs[symb]:
                memory = memory[:-1]
            else:
                memory.append(symb)

        if len(memory) == 0:
            return True
        else:
            return False

s = Solution()
print(s.isValid("(]"))