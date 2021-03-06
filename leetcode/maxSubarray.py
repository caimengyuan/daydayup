'''
返回最大连续子序列的和

最大连续子序列的特点：
    1.第一个值不为负数
    2.前面的值累计加上当前的值后比当前值小，说明当前值不能加进去；如果累计值加上当前值比当前值大或者等于，那就可以加入累计值当中

    步骤：
    1、定义两个变量，一个用来存储之前的累加值，一个用来存储当前的最大和。遍历数组中的每个元素，假设遍历到第i个数时：
　　    ①如果前面的累加值为负数或者等于0，那对累加值清0重新累加，把当前的第i个数的值赋给累加值。
　　    ②如果前面的累加值为整数，那么继续累加，即之前的累加值加上当前第i个数的值作为新的累加值。
    2、判断累加值是否大于最大值：如果大于最大值，则最大和更新；否则，继续保留之前的最大和。
'''

class Solution:
    def findGreatestSumOfSubarray(self, array):
        sum = array[0]
        presum = 0
        for i in array:
            if presum < 0:
                presum = i
            else:
                presum += i
            sum = max(presum, sum)
        return sum
