# https://leetcode.com/problems/merge-strings-alternately/?envType=study-plan-v2&envId=leetcode-75


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:        
        char_list = ["" for f in range(max(len(word1), len(word2))*2)]
        word1_idx = 0
        word2_idx = 0
        for i, _ in enumerate(char_list):
            try:
                if i % 2 == 0:
                    char_list[i] = word1[word1_idx]
                    word1_idx += 1
                elif i % 2 == 1:
                    char_list[i] = word2[word2_idx]
                    word2_idx += 1
            except IndexError as e:
                continue

        return "".join(char_list)
    
word1 = "ab"
word2 = "pqrs"
print(Solution().mergeAlternately(word1, word2))