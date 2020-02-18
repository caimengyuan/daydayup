'''
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
'''
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNum(self, l1, l2):
        re = ListNode(0)
        r = re
        carry = 0
        while(l1 or l2):
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            s = x + y + carry     # 进位 carry位标志位
            carry = s // 10
            r.next = ListNode(s%10)
            r = r.next
            if l1!=None: l1 = l1.next
            if l2!=None: l2 = l2.next
            
        if carry > 0:
            r.next = ListNode(1)
        lst = []
        re = re.next
        while re:
            lst.append(re.val)
            re = re.next
        return lst

x1 = input("Please input a list:\n")
y1 = x1.split()
m = ListNode(0)
l1 = m
for i in y1:
    m.next = ListNode(int(i))
    m = m.next
l1 = l1.next

x2 = input("Please input a list:\n")
y2 = x2.split()
n = ListNode(0)
l2 = n
for i in y2:
    n.next = ListNode(int(i))
    n = n.next
l2 = l2.next

s = Solution()
print(s.addTwoNum(l1, l2))