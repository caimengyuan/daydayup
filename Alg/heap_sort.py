'''
借助堆来实现的选择排序，思想同简单的选择排序，以下以大顶堆为例。注意：如果想升序排序就使用大顶堆，反之使用小顶堆：

1. 如何由一个无序序列建成一个堆？

2. 如何在输出堆顶元素之后，调整剩余元素成为一个新的堆？

堆（二叉堆）可以视为一棵完全的二叉树，完全二叉树的一个“优秀”的性质是，除了最底层之外，每一层都是满的，这使得堆可以利用数组来表示（普通的一般的二叉树通常用链表作为基本容器表示），每一个结点对应数组中的一个元素。


对于给定的某个结点的下标i，可以很容易的计算出这个结点的父结点、孩子结点的下标：

Parent(i) = floor(i/2)，i 的父节点下标

Left(i) = 2i，i 的左子节点下标

Right(i) = 2i + 1，i 的右子节点下标


堆排序（Heap-Sort）是堆排序的接口算法，Heap-Sort先调用Build-Max-Heap将数组改造为最大堆，然后将堆顶和堆底元素交换，之后将底部上升，最后重新调用Max-Heapify保持最大堆性质。
'''

# 调整根和左右子女的值
def max_head(mylist, headsize, root_index):

    # mylist: 待排序列表
    # headsize: 排序的数目
    # root_index: 开始比较的根节点
    left = root_index*2+1
    right =root_index*2+2
    large_index = root_index

    # 左右子树下标不超过待排序列表长度的前提下，比根节点值大的情况下，找出最大的下标
    if left < headsize and mylist[left] > mylist[large_index]:
        large_index = left
    if right < headsize and mylist[right] > mylist[large_index]:
        large_index =right

    if large_index != root_index:
        mylist[large_index], mylist[root_index] =mylist[root_index], mylist[large_index]
        max_head(mylist, headsize, large_index)


# 建大顶堆
def create_head(mylist):
    length = len(mylist)
    # 从上往下 从左往右 最后一个根节点
    max_child_index = (length - 2)//2
    for i in range(max_child_index, -1, -1):
        max_head(mylist, length, i)


def sort_head(mylist):
    create_head(mylist)
    print(mylist)
    for i in range(len(mylist)-1,-1,-1):
        mylist[0], mylist[i] = mylist[i], mylist[0]
        max_head(mylist, i, 0)


if __name__== "__main__":
    mylist = [49,38,65,97,76,13,27,49]
    sort_head(mylist)
    print(mylist)
