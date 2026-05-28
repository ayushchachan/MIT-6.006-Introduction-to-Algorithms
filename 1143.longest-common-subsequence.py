#
# @lc app=leetcode id=1143 lang=python3
#
# [1143] Longest Common Subsequence
#

# @lc code=start

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        lcs_length = [[None for _ in range(n)] for _ in range(m)]
        
        if text1[0] == text2[0]:
            lcs_length[0][0] = 1
        else:
            lcs_length[0][0] = 0
            
        for j in range(1, n):
            if text1[0] == text2[j]:
                lcs_length[0][j] = 1
            else:
                lcs_length[0][j] = lcs_length[0][j - 1]
        
        for i in range(1, m):
            if text1[i] == text2[0]:
                lcs_length[i][0] = 1
            else:
                lcs_length[i][0] = lcs_length[i - 1][0]
            
            for j in range(1, n):
                if text1[i] == text2[j]:
                    lcs_length[i][j] = 1 + lcs_length[i - 1][j - 1]
                else:
                    lcs_length[i][j] = max(
                        lcs_length[i][j - 1], 
                        lcs_length[i - 1][j])
        
        
        
        print(lcs_length)
        return lcs_length[m - 1][n - 1]





# @lc code=end

