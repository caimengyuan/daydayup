def binary_search(sorted_array, val):
    if not sorted_array:
        return -1 
    
    beg = 0
    end = len(sorted_array)-1

    while beg <= end:
        mid = int((end - beg) / 2)
        if sorted_array[mid] < val:
            beg = mid + 1
        elif sorted_array[mid] > val:
            end = mid - 1
        else:
            return mid
    return -1 

def binary_search_recursive(sorted_array, beg, end, val):
    if beg >= end:
        return -1 
    mid = int((end - beg) / 2)
    if sorted_array[mid] == val:
        return mid
    elif sorted_array[mid] > val:
        return binary_search_recursive(sorted_array, beg, mid, val)
    else:
        return binary_search_recursive(sorted_array, beg, mid+1, val)

def test_binary_search():
    ll = list(range(10))
    print(ll)
    print(binary_search(ll, 5))

test_binary_search()