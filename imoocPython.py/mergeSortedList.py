'''
合并两个有序数组，要求a[n], a[m], a[n+m]
'''
def merge_sorted_list(sorted_a, sorted_b):
    length_a, length_b = len(sorted_a), len(sorted_b)
    a = b = 0
    new_sorted_seq = []
    
    while a < length_a and b < length_b:
        if sorted_a[a] < sorted_b[b]:
            new_sorted_seq.append(sorted_a[a])
            a += 1
        else:
            new_sorted_seq.append(sorted_b[b])
            b += 1
    if a < length_a:
        new_sorted_seq.extend(sorted_a[a:])   # 注意列表后面接列表需要用extend
    if b < length_b:
        new_sorted_seq.extend(sorted_b[b:])
    return new_sorted_seq


def test_merge_sorted_list():
    a = [1, 2, 5]
    b = [0, 3, 4, 8]
    print(merge_sorted_list(a, b))

test_merge_sorted_list()
