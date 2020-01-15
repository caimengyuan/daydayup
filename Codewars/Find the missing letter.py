'''
You will always get an valid array. And it will be always exactly one letter be missing. The length of the array will always be at least 2.
The array will always contain letters in only one case.

Example:

['a','b','c','d','f'] -> 'e' ['O','Q','R','S'] -> 'P'
'''

# Python3 打印26个英文字母
# 1. list(map(chr, range(ord('a'), ord('z') + 1)))
# 2. [chr(x) for x in range(ord('a'), ord('z') + 1)] 




# Does my number look big in this?
def narcissistic( value ):
    # Code away
    n, sum = 0,0
    num, res = value, value
    while num != 0:
        n += 1
        num = num // 10
    flag = n
    print(n)
    while n > 0:
        sum += (value % 10) ** flag
        value = value // 10
        n -= 1
    print(sum)
    if sum == res:
        return True
    else:
        return False


def narcissistic(value):
    return value == sum(int(x) ** len(str(value)) for x in str(value))



'''
排序：
    对列表中的奇数排序 偶数不动
'''
def sort_array(arr):
  odds = sorted((x for x in arr if x%2 != 0), reverse=True)
  return [x if x%2==0 else odds.pop() for x in arr]

sort_array([5, 3, 2, 8, 1, 4])
