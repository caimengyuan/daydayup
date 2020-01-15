'''
给定两个单词 word1 和 word2，找到使得 word1 和 word2 相同所需的最小步数，每步可以删除任意一个字符串中的一个字符。

示例 1:

输入: "sea", "eat"
输出: 2
解释: 第一步将"sea"变为"ea"，第二步将"eat"变为"ea"

解析：
    动态规划问题：
    状态：dp[i][j] 表示word1[:i]和word2[:j]的最长公共子序列
    初始化：dp[i][0]=dp[0][j]=0
    状态转移方程：dp[i][j] = dp[i-1][j-1] + 1 if word1[i-1] == word2[j-1] else max(dp[i-1][j], dp[i][j-1])
'''
class Solution:
    def opration(self, word1, word2):
        # m,n = len(word1), len(word2)
        # dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
        # for i in range(1, m-1):
        #     for j in range(1, n-1):
        #         if word1[i] == word2[j]:
        #             dp[i][j] = dp[i-1][j-1] + 1
        #         else:
        #             dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        # return m+n - 2*dp[m-1][n-1]

        n, m = len(word1), len(word2)
        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, m+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        return n+m-2*dp[n][m]



class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        word1,word2=' '+word1,' '+word2
        m,n=len(word1),len(word2)
        d=[[0]*n,[0]*n]
        t=0
        for i in range(1,m):
            for j in range(1,n):
                if word1[i]==word2[j]:
                    d[t][j]=d[1-t][j-1]+1
                else:
                    d[t][j]=max(d[1-t][j],d[t][j-1])
            t=1-t
        return m+n-d[1-t][-1]*2-2
