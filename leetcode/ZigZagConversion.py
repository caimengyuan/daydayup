'''
将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：

L   C   I   R
E T O E S I I G
E   D   H   N
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。
'''
# 假设当前的numRows=4，设置一个列表res储存输出的字符串，如果numRows为4，则需要4个地址来存储Z字形的字符串
# res[i]为第i行的输出的字符串
# 从左往右遍历输入字符串时，可以观察到，每当遍历到numRows-1次时，都需要进行拐弯
# 重点：设置一个flag值，初始为-1
'''
按顺序遍历字符串 s；
res[i] += c： 把每个字符 c 填入对应行;
i += flag： 更新当前字符 c 对应的行索引；
flag = - flag： 在达到 ZZ 字形转折点时，执行反向。
'''
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows < 2:
            return s
        res = ["" for _ in range(numRows)]
        i = 0         # 标志的哪一行
        flag = -1        # 标志位，标志是否转行
        for a in s:
            res[i] += a
            if i == 0 or i == numRows-1:
                flag = -flag         # 需要进行转行，则转换标志位，增加行或者减少行
            i += flag
        return "".join(res)


