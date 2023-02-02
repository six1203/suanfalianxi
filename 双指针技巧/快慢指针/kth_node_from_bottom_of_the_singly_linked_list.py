"""
单链表的倒数第k个节点
"""
from typing import Optional


# 算法思路：

# 链表有n个节点，第一个指针先走k步，然后两个指针开始一起走，当第一个指针走到链表尾部时，走了n-k步，第二个指针也走了n-k步，停留在n-k+1个节点上, 即恰好停链表的倒数第 k 个节点上


class ListNode:
    def __init__(self, x, next=None):
        self.data = x
        self.next = next


def last_kth_node(head: Optional[ListNode], k):
    p1 = p2 = head

    for i in range(k):
        if not p1:
            return None
        # 先走k步
        p1 = p1.next

    while p1:
        # 一起走剩下的n-k步
        p1 = p1.next
        p2 = p2.next

    # 返回节点
    return p2
    # 返回节点的值
    # return p2.data


if __name__ == "__main__":
    head = ListNode(
        1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7))))))
    )
    print(last_kth_node(head, 2).data)
