'''
快速排序
'''
def quickSort(array):
    # 递归出口
    if len(array) < 2:
        return array
    else:
        privot_index = 0
        privot = array[privot_index]
        less_part = [i for i in array[privot_index+1:] if i <= privot]
        great_part = [i for i in array[privot_index+1:] if i > privot]
        return quickSort(less_part)+ [privot] + quickSort(great_part)

def test_quicksort():
    import random
    ll = list(range(10))
    random.shuffle(ll)
    print(ll)
    assert quickSort(ll) == sorted(ll)

test_quicksort()
