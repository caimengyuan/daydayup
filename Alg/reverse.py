'''
单链表反转
'''

class Node:
    data = 0
    next = None


def bulid_single_link_list(nodeArr):
    head_node = None
    next_node = None
    for i in nodeArr:
        node = Node()
        node.data = i
        node.next = None
        if head_node is None:
            head_node = node
            head_node = head_node
        else:
            next_node.next = node
            next_node = node
    return head_node


def reverse(head):
    if head is None or head.next is None:
        return head
    cur = head
    pre = None
    pnext = None
    while cur is not None:
        pnext = cur.next
        cur.next = pre
        pre = cur 
        cur = pnext
    return pre
