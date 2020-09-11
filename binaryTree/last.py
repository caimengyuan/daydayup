class treeNode(object):
    def __init__(self, x):
        self.value = x
        self.left = None        # 左子树
        self.right = None       # 右子树

# 递归-后序遍历
def last_normal(root):
    if root == None:
        return None
    last_normal(root.left)
    last_normal(root.right)
    print(root.value)

# 非递归-后序遍历
def last_cycle(root):
    if root == None:
        return None
    stack = []
    tempNode = root
    while tempNode or stack:
        while tempNode:
            stack.append(tempNode)
            tempNode = tempNode.left
        
        node = stack[-1]
        tempNode = node.right
        if node.right == None:
            print(node.value)
            node = stack.pop()
            while stack and node == stack[-1].right:
                node = stack.pop()
                print(node.value)


if __name__ == "__main__":
    # 构造一棵二叉树
    # 后序遍历的结果：4 5 2 5 6 7 3 1
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

    print("递归-后序遍历：")
    last_normal(t1)
    print("非递归-后序遍历")
    last_cycle(t1)