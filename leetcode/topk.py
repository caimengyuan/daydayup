import heapq
class Topk:
    '''
    1.先将前k个元素建立一个最小堆
    2.读取后面的数和根结点比较，比根节点大，则替换根，调整堆
    '''
    def __init__(self, iterable, k):
        self.minheap = []
        self.capacity = k
        self.iterable = iterable
    
    def push(self, val):
        if len(self.minheap) >= self.capacity:
            min_val = self.minheap[0]
            if val < min_val:
                pass
            else:
                heapq.heapreplace(self.minheap, val)
        else:
            heapq.heappush(self.minheap, val)

    def get_topk(self):
        for val in self.iterable:
            self.push(val)
        return self.minheap