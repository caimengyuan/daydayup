'''
归并排序
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
        new_sorted_seq.extend(sorted_a[a:])
    else:
        new_sorted_seq.extend(sorted_b[b:])
    return new_sorted_seq

def merge_sort(array):
    # 递归出口
    if len(array) < 2:
        return array
    else:
        mid = int(len(array)/2)
        left_half = merge_sort(array[:mid])
        right_half = merge_sort(array[mid:])
        return merge_sorted_list(left_half, right_half)