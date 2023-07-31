#https://leetcode.com/problems/reverse-vowels-of-a-string/submissions/?envType=study-plan-v2&envId=leetcode-75
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel_list = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        
        result = []
        s_vowels = []
        for ch in [f for f in s]:
            if ch in vowel_list:
                s_vowels.insert(0, ch)
                result.append("")
            else:
                result.append(ch)
        vowel_idx = 0
        for idx, ch in enumerate(result):
            if ch == "":
                result[idx] = s_vowels[vowel_idx]
                vowel_idx += 1
        return "".join(result)

## Solution - Two pointer
# class Solution:
#     def reverseVowels(self, s: str) -> str:
#         lis=['a', 'e', 'i', 'o','u','A','E','I','O','U']
#         i=0
#         j=len(s)-1
#         s=list(s)
#         while(i<j):
#             if s[i] not in lis:
#                 i+=1
#             if s[j] not in lis:
#                 j-=1
#             if s[i] in lis and s[j] in lis:
#                 s[i],s[j]=s[j],s[i]
#                 i+=1
#                 j-=1
#         s="".join(s)
#         return s