class Solution:
    def findIntersectionValues(self, nums1: list[int], nums2: list[int]) -> list[int]:
       	p1 = 0
        p2 = 0
        result = []

        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] > nums2[p2]:
                p2 += 1
            elif nums1[p1] < nums2[p2]:
                p1 += 1
            result.append(nums1[p1])
            p1 += 1
            p2 += 1
        return result

s = Solution()
print(s.findIntersectionValues(nums1 = [1,2,2,3], nums2 = [1,2,3,3]))
