class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        my_nums = list(set(nums))
        my_nums.sort()

        nums[:] = my_nums

        return len(my_nums)

s = Solution()
print(s.removeDuplicates([1,1,2]))