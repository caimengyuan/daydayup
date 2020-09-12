class treeNode(object):
    def __init__(self, x):
        self.value = x
        self.left = None        # 左子树
        self.right = None       # 右子树

def level_normal(root):
    def helper(node, level):
        if not node:
            return
        else:
            sol[level-1].append(node.value)
            if len(sol) == level:      # 遍历到新层时，只有最左边的结点使得等式成立
                sol.append([])
            helper(node.left, level+1)
            helper(node.right, level+1)
    sol = [[]]
    helper(root, 1)
    print(sol[:-1])

def level_cycle(root):
    if not root:
        return []
    sol = []
    curr = root
    queue = [curr]
    while queue:
        curr = queue.pop(0)
        sol.append(curr.value)
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)
    print(sol)

if __name__ == "__main__":
    # 构造一棵二叉树
    # 层次遍历的结果：1 2 3 4 5 6 7
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

    level_normal(t1)
    level_cycle(t1)
