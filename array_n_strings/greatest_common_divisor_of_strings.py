import re
class Solution:
    # Solution
    def gcdOfStrings1(self, str1: str, str2: str) -> str:
        long_str, short_str = (str2, str1) if len(str1) < len(str2) else (str1, str2)
        for i in range(len(long_str)):
            part_str = short_str[:i+1]
            if len(short_str) != sum(len(s) for s in re.findall(part_str, short_str)):
                continue
            if len(long_str) == sum(len(s) for s in re.findall(part_str, long_str)):
                result = part_str
        return result
    # Good Solution.
    # def gcdOfStrings(self, str1: str, str2: str) -> str:
    #     # Check if concatenated strings are equal or not, if not return ""
    #     if str1 + str2 != str2 + str1:
    #         return ""
    #     # If strings are equal than return the substring from 0 to gcd of size(str1), size(str2)
    #     from math import gcd
    #     return str1[:gcd(len(str1), len(str2))]

str1 = "ABABAB"
str2 = "ABAB"
print(Solution().gcdOfStrings2(str1, str2))
str1 = "TAUXXTAUXXTAUXXTAUXXTAUXX"
str2 = "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"
print(Solution().gcdOfStrings2(str1, str2))