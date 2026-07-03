#Первое решение
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i]+nums[j] == target:
                    return [i, j]

s = Solution()
print(s.twoSum([2,7,11,15], 13))

#Оптимизированное решение
class Solution_hash:
    def twoSumHash(self, nums: list[int], target: int) -> list[int]:
        seem = {}
        for i, num in enumerate(nums):
            x = target - num
            if x in seem:
                return [seem[x], i]
            else:
                seem[num] = i

sh = Solution_hash()
print(sh.twoSumHash([2,7,11,15], 13))