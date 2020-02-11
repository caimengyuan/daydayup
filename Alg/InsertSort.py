'''
    插入排序
'''

def insertSort(array):
    if len(array) < 2:
        return array
    for i in range(1, len(array)):
        value = array[i]
        j = i
        while j > 0 and value < array[j-1]:
            array[j] = array[j-1]
            j = j-1
        array[j] = value
    return array

def test_insertSort():
    import random
    ll = list(range(10))
    random.shuffle(ll)
    print(ll)
    print(insertSort(ll))

test_insertSort()