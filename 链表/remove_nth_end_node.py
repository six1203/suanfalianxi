"""
删除链表的倒数第 N 个结点

给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

输入：head = [1,2,3,4,5], n = 2
输出：[1,2,3,5]

"""


from typing import Optional


class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # [1, 2, 3,,4, 5]

        # 定义快慢指针，初始化为head
        slow, fast = head, head

        # 快指针先移动n个节点
        for i in range(n):
            fast = fast.next

        # 如果快指针到达链表尾部，则说明要移除的是链表的头节点
        if not fast:
            return head.next

        # 同时移动快慢指针
        while fast.next:
            slow = slow.next
            fast = fast.next

        # 此时slow指向要移除的节点的前一个节点，将其next指向下下个节点
        slow.next = slow.next.next

        return head





if __name__ == '__main__':
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    Solution().removeNthFromEnd(head, 5)
