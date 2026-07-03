class Solution:
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