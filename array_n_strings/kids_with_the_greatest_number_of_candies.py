class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        candy_dict = {}
        max_num = max(candies)
        result = [True for _ in candies]

        for idx, candy in enumerate(candies):
            if candy < max_num-extraCandies:
                result[idx] = False
        return result
    