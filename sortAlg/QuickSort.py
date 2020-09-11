'''
快速排序
'''

def quickSort_01(array):
    # 递归出口
    if len(array) < 2:
        return array
    else:
        index = 0
        privot = array[index]
        less_part = [i for i in array[index+1:] if i <= privot]
        great_part = [i for i in array[index+1:] if i > privot]
        return quickSort_01(less_part) + [privot] + quickSort_01(great_part)


def quickSort_02(array, start, end):
    # 递归出口
    if start >= end:
        return
    low = start 
    high = end 
    value = array[start] 
    while low < high: 
        while low < high and array[high] >= value:
            high -= 1 
        array[low] = array[high]
        print('array28:{}'.format(array))

        while low < high and array[low] <= value:
            low += 1 
        array[high] = array[low]
        print('array32:{}'.format(array))

    print('array33:{}'.format(array))
    mid = low
    array[low] = value
    quickSort_02(array, start, mid-1)
    quickSort_02(array, mid+1, end)

def test_quicksort():
    import random
    ll = list(range(10))
    random.shuffle(ll)
    print(ll)
    print(quickSort_02(ll, 0, len(ll)-1))

test_quicksort()
