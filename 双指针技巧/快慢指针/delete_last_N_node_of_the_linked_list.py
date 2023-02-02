"""
删除链表的倒数第 N 个结点

给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
"""

# 算法思路
# 使用双指针p1和p2, p1先走n步, 然后p1和p2一起走, 当p1走到链表末尾时, p2就是倒数第n个节点
# 移除p2.next节点即可




class ListNode:
    def __init__(self, x=0, next=None):
        self.data = x
        self.next = next


def delete_last_n_node(head, n):

    p1 = p2 = dummy = ListNode(next=head)

    for _ in range(n):
        if not p1:
            return None
        p1 = p1.next

    while p1:
        p1 = p1.next
        p2 = p2.next

    # 移除倒数第n个节点
    p2.next = p2.next.next

    # 返回头节点
    return dummy.next
