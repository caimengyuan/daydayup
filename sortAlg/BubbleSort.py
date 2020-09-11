'''
    冒泡排序：时间复杂度O(N^2)
'''

def bubbleSort(array):
    if len(array) < 2:
        return array
    length = len(array)
    for i in range(length):
        for j in range(length-i-1):   # attention
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

def test_bubbleSort():
    import random
    ll = list(range(10))
    random.shuffle(ll)
    print(ll)
    print(bubbleSort(ll))

test_bubbleSort()