'''
快速排序，分治法，三步走

'''

def quickSort_01(array):
    # 递归出口
    if len(array) < 2:
        return array

    else:
        index = 0   # 第一个元素作为pivot
        pivot = array[index]
        less_part = [
            i for i in array[index+1:] if i <= pivot
        ]
        great_part = [
            i for i in array[index+1:] if i > pivot
        ]
        return quickSort_01(less_part) + [pivot] + quickSort_01(great_part)


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
    random.shuffle(ll)  # 打乱数组
    print(ll)
    print(quickSort_02(ll, 0, len(ll)-1))
    assert quickSort_01(ll) == sorted(ll)

test_quicksort()
