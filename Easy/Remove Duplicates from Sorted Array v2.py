class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        pointer_a = 0
        pointer_b = 1
        while pointer_b < len(nums):
            if nums[pointer_b] != nums[pointer_a]:
                pointer_a += 1
                nums[pointer_a] = nums[pointer_b]

            pointer_b += 1

        nums[:] = nums[:pointer_a+1]

        print(nums)
        return pointer_a + 1

s = Solution()
print(s.removeDuplicates([1,1,2,2,3,3,4,5,5]))