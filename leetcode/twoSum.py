'''
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
'''
# 利用python中字典的数据类型，字典的本质是用的哈希表

class Solution(object):
    def towSum(self, nums, target):
        hashmap = {}
        for ind, num in enumerate(nums):
            another_num = target - num
            if another_num in hashmap:
                return [ind, hashmap[another_num]]
            hashmap[num] = ind
        return None

x = input("please input a list:\n")
y = x.split()
nums = []
for i in y:
    nums.append(int(i))

t = input("please input a target\n")
target = int(t)

s = Solution()
print(s.towSum(nums, target))