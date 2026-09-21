'''class Solution:
    def isPalindrome(self, x: int) -> bool:
         if x < 0:
             return False

         if x % 10 == 0 and x != 0:
             return False

         reverse = 0
         while x > reverse:
             reverse = reverse * 10 + x % 10
             print(f'reverse: {reverse}')
             x = x // 10
             print(f'x: {x}')

         if x == reverse or x == reverse // 10:
             return True
         return False

s = Solution()
print(s.isPalindrome(124))
'''

#Оптимизация по алгоритму два указателя
class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        left = 0
        right = len(s) - 1
        final = False
        while left < right:
            if s[left] == s[right]:
                final = True
            else:
                final = False

        return final

s = Solution()
print(s.isPalindrome(x=121))
