#875


# import math


# class Solution:
#     def minEatingSpeed(self, piles: List[int], h: int) -> int:
#         left = 1
#         right = max(piles)
#         res = right

#         while left <= right:
#             speed = left + (right - left) // 2

#             total_time = 0
#             for pile in piles:
#                 total_time += math.ceil(pile / speed)

#             if total_time <= h:
#                 res = speed
#                 right = speed - 1
#             else:
#                 left = speed + 1

#         return res



#33


# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         left = 0
#         right = len(nums) - 1

#         while left <= right:
#             # mid = (right + left) // 2
#             mid = left + ((right - left) // 2)

#             middle_value = nums[mid]
#             if target == middle_value:
#                 return mid

#             if nums[left] <= middle_value:
#                 if target > middle_value or target < nums[left]:
#                     left = mid + 1
#                 else:
#                     right = mid - 1
#             else:
#                 if target < middle_value or target > nums[right]:
#                     right = mid - 1
#                 else:
#                     left = mid + 1

#         return -1




#704



# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         left = 0
#         right = len(nums) - 1

#         while left <= right:
#             # mid = (left + right) // 2
#             mid = left + ((right - left) // 2)
#             if nums[mid] > target:
#                 right = mid - 1
#             elif nums[mid] < target:
#                 left = mid + 1
#             else:
#                 return mid

#         return -1



#128


# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         nums_set = set(nums)
#         longest = 0

#         for n in nums_set:
#             if (n - 1) not in nums_set:
#                 seq_len = 0
#                 while (n + seq_len) in nums_set:
#                     seq_len += 1
#                 longest = max(longest, seq_len)

#         return longest




#49


# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         nums_set = set(nums)
#         longest = 0

#         for n in nums_set:
#             if (n - 1) not in nums_set:
#                 seq_len = 0
#                 while (n + seq_len) in nums_set:
#                     seq_len += 1
#                 longest = max(longest, seq_len)

#         return longest




#347


# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         result = {}
#         for i in nums:
#             if i not in result:
#                 result[i] = 1
#             else:
#                 result[i] += 1
#         sorted_counts = dict(sorted(result.items(), key=lambda item: item[1], reverse=True))
#         return list(sorted_counts.keys())[:k]