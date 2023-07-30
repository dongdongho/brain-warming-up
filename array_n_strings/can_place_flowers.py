# https://leetcode.com/problems/can-place-flowers/description/?envType=study-plan-v2&envId=leetcode-75
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        exp_list = [flowerbed[0]] + flowerbed + [flowerbed[-1]]
        flowerbed_list = ["1" if f or exp_list[idx] or exp_list[idx+2] else "0" for idx, f in enumerate(exp_list[1:-1])]
        flowerbed_list = "".join([f for f in flowerbed_list]).split("1")
        for cur_bed in flowerbed_list:
            num_empty = len([f for f in cur_bed])
            if num_empty % 2 == 0:
                n -= num_empty//2
            else:
                n -= (num_empty+1)//2
            if n <= 0:
                return True
        return False

## Simple solution
# class Solution:
#     def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
#         if n == 0:
#             return True
#         for i in range(len(flowerbed)):
#             if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed)-1 or flowerbed[i+1] == 0):
#                 flowerbed[i] = 1
#                 n -= 1
#                 if n == 0:
#                     return True
#         return False