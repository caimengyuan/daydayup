class treeNode(object):
    def __init__(self, x):
        self.value = x
        self.left = None        # 左子树
        self.right = None       # 右子树

# 递归-中序遍历
def middle_normal(root):
    if root == None:
        return None
    middle_normal(root.left)
    print(root.value)
    middle_normal(root.right)

# 非递归-中序遍历
def middle_cycle(root):
    if root == None:
        return None
    tempNode = root
    stack = []
    while tempNode or stack:
        while tempNode:
            stack.append(tempNode)
            tempNode = tempNode.left
        
        node = stack.pop()
        print(node.value)
        tempNode = node.right


if __name__ == "__main__":
    # 构造一棵二叉树
    # 中序遍历的结果：4 2 5 1 6 3 7
    #         t1
    #     t2      t3
    # t4    t5  t6    t7

    t1 = treeNode(1)
    t2 = treeNode(2)
    t3 = treeNode(3)
    t4 = treeNode(4)
    t5 = treeNode(5)
    t6 = treeNode(6)
    t7 = treeNode(7)

    t1.left = t2
    t1.right = t3
    t2.left = t4
    t2.right = t5
    t3.left = t6
    t3.right = t7
    
    print("递归-中序遍历：")
    middle_normal(t1)
    print("非递归-中序遍历：")
    middle_cycle(t1)