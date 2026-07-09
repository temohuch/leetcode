class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        length_default = len(nums)
        final_array = [ '_' for _ in range(length_default) ]
        count = 0
        for index, num in enumerate(nums):
            if index == 0:
                final_array[index] = num
                count = index + 1
            elif num == final_array[count-1]:

                continue
            else:
                final_array[count] = num
                count += 1

        nums[:] = final_array[:count]
        return count

s = Solution()
print(s.removeDuplicates([1,1,2]))