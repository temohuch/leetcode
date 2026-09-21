class Solution:
    def mergeTwoLists(self, list1: list, list2: list) -> list:
        count_1 = 0
        count_2 = 0
        result = []

        while count_1 < len(list1) and count_2 < len(list2):
            if list1[count_1] < list2[count_2]:
                result.append(list1[count_1])
                count_1 += 1
            else:
                result.append(list2[count_2])
                count_2 += 1
        result.extend(list1[count_1:])
        result.extend(list2[count_2:])

        return result


s = Solution()
print(s.mergeTwoLists(list1 = [1,2,4,5,6,7], list2 = [1,3,4]))
