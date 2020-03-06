'''
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:

输入: 123
输出: 321
'''
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        y = int(str(x)[::-1]) if x>=0 else -int(str(x)[:0:-1])
        return y if -2**31 < y < 2**31-1 else 0
# [a:b:-1] 表示反向输出索引b到a的值