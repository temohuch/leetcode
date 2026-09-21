class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        print(nums)
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (right + left) // 2
            guess = nums[mid]
            if guess == target:
                return mid
            elif guess > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1

s = Solution()
print(s.search(nums = [-1,0,3,5,9,12], target = 4))
print(s.search(nums= [-5,-8,0,3,1,8,4,5], target = 5))
