"""
判断链表是否包含环；如果包含环，如何计算环的起点
"""

# 算法思路
# 1. 快慢指针，如果有环，快指针一定会追上慢指针
# 2. 当快慢指针相遇时，将快指针指向头结点，然后快慢指针同时移动，再次相遇点即为环的起点


class ListNode:
    def __init__(self, x, next=None):
        self.data = x
        self.next = next


def has_cycle(head):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


# 如果链表中含有环，如何计算这个环的起点
def find_cycle_start(head):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        # 第一次相遇点
        if slow == fast:
            break

    # 有空指针，说明没有环
    if not fast or not fast.next:
        return None

    # 重新指向头结点
    slow = head

    # 快慢指针同时移动，再次相遇点即为环的起点
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(6)
    head.next.next.next.next.next.next = head.next.next

    print(find_cycle_start(head).data)
