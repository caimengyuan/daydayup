'''
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
'''
# 滑动窗口的方法

class Solution(object):
    def LengthOfLongestSubstring(self, s):
        if not s:
            return 0
        left = 0       # 创建在原字符串的左窗口边界的索引
        cur_len = 0    # 窗口的当前长度
        max_len = 0        # 存储最终的结果
        find_s = set()          # 建立的窗口（list也可以用，但是list的功能强大，效率低）
        for i in s:    
            cur_len += 1
            while i in find_s:
                find_s.remove(s[left])    
                # 窗口中将要出现第一个重复元素时，删除原来字符串的左窗口的值，直到窗口中将不会出现重复元素，也就是说删除将要出现的字符第一次出现及前面所有的值
                left += 1       # 窗口左移
                cur_len -= 1         # 窗口大小变化
            if max_len < cur_len:
                max_len = cur_len
            find_s.add(i)
        return max_len

x = input("Please input a string:\n")
s = Solution()
print(s.LengthOfLongestSubstring(x))