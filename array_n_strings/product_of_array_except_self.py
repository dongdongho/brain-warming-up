# https://leetcode.com/problems/product-of-array-except-self/submissions/?envType=study-plan-v2&envId=leetcode-75
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_val = 1
        without_0_product_val = 1
        cnt_0 = 0
        for num in nums:
            product_val *= num
            without_0_product_val = without_0_product_val*1 if num == 0 else without_0_product_val*num
            if num == 0:
                cnt_0 += 1
        if cnt_0 > 1:
            without_0_product_val = 0
        result = [int(product_val/f) if f != 0 else without_0_product_val for f in nums]
        return result
        