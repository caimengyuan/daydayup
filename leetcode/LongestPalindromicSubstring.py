'''
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
'''
# 方案一：动态规划
# 画出动态规划矩阵，大小是字符串s的长度，矩阵中的每个值初始值为False
# 状态：dp[i][j]表示字符串s中从i到j是否为回文子串
# 初始化：dp[i][i] = True 
# 状态转移方程：dp[i][j] = (s[i]==s[j]) and dp[i+1][j-1]
class Solution(object):
    def longestPalindrome(self, s):
        size = len(s)
        if size < 2:
            return s
        
        dp = [[False for _ in range(size)] for _ in range(size)]     # 状态初始化定义
        start = 0
        max_len = 1

        for i in range(size):
            dp[i][i] = True       # 减少运算时间
        
        for j in range(1, size):
            for i in range(0, j):
                if s[i] == s[j]:        # 状态转移
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = False
                
                if dp[i][j]:
                    cur_len = j-i+1
                    if cur_len > max_len:
                        max_len = cur_len
                        start = i
        return s[start:start+max_len]

x = input("Please input a string:\n")
s = Solution()
print(s.longestPalindrome(x))
