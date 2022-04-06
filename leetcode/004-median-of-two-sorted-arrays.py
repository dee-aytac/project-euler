# class Solution(object):
#     def findMedianSortedArrays(self, nums1, nums2):
#         """
#         :type nums1: List[int]
#         :type nums2: List[int]
#         :rtype: float
#         """
#         length = len(nums1) + len(nums2)
#         new_list = []
#         index_1 = 0
#         index_2 = 0
#         while index_1 < len(nums1) and index_2 < len(nums2):
#             if nums1[index_1] < nums2[index_2]:
#                 new_list.append(nums1[index_1])
#                 index_1 += 1
#             else:
#                 new_list.append(nums2[index_2])
#                 index_2 += 1

#         while index_1 < len(nums1):
#             new_list.append(nums1[index_1])
#             index_1 += 1

#         while index_2 < len(nums2):
#             new_list.append(nums2[index_2])
#             index_2 += 1

#         if length % 2 == 0:
#             return (new_list[length // 2] + new_list[(length // 2) - 1]) / 2
#         else:
#             print(new_list, length // 2)
#             return new_list[length // 2]


solution = Solution()
print(solution.findMedianSortedArrays([1, 2], [3, 4]))