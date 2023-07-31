# https://leetcode.com/problems/reverse-words-in-a-string/submissions/?envType=study-plan-v2&envId=leetcode-75
class Solution:
    def reverseWords(self, s: str) -> str:
        word_list = [f for f in s.split(" ") if f != ""][]
        i, j = 0, len(word_list) - 1
        while i<j:
            temp = word_list[i]
            word_list[i] = word_list[j]
            word_list[j] = temp
            i += 1
            j -= 1
        return " ".join(word_list)
    
# Solution using list indexing
# class Solution:
#     def reverseWords(self, s: str) -> str:
#         word_list = [f for f in s.split(" ") if f != ""][::-1]
#         return " ".join(word_list)