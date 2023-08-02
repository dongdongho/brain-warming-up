# https://leetcode.com/problems/move-zeroes/submissions/?envType=study-plan-v2&envId=leetcode-75
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        except_0 = [f for f in nums if f != 0]
        zeros = [0 for _ in range(len(nums)-len(except_0))]
        result = except_0 + zeros
        for i, _ in enumerate(nums):
            nums[i] = result[i]
        return nums
