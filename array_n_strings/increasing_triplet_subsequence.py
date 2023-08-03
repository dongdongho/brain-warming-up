# https://leetcode.com/problems/increasing-triplet-subsequence/description/
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(set(nums)) < 3:
            return False
        i, j, k = 0, 1, 2
        while i < len(nums)-2:
            if nums[i] >= nums[j]:
                j = j+1
                k = j+1
                if len(nums) == k:
                    i = i+1
                    j = i+1
                    k = i+2
                continue

            if nums[j] >= nums[k]:
                k += 1
                if len(nums) == k:
                    j = j+1
                    k = j+1
                    if len(nums)-1 == j:
                        i = i+1
                        j = i+1
                        k = i+2
                continue
            return True
        return False
# Simple solution
# class Solution:
#     def increasingTriplet(self, nums: List[int]) -> bool:
#         first = second = float('inf') 
#         for n in nums: 
#             if n <= first: 
#                 first = n
#             elif n <= second:
#                 second = n
#             else:
#                 return True
#         return False