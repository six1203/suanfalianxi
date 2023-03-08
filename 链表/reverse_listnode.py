from base import LinkedList

"""
反转单链表

给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。

输入：head = [1,2,3,4,5]
输出：[5,4,3,2,1]

输入：head = [1,2]
输出：[2,1]

https://leetcode.cn/problems/reverse-linked-list/
"""


def reverseListNode(head: LinkedList) -> LinkedList:

    # 初始化三个指针，分别指向当前节点（cur）、当前节点的前驱节点（prev）和当前节点的后继节点（next）。
    # 将当前节点的后继节点保存到 next 中。
    # 将当前节点的后继节点指向 prev。
    # 将 prev 指针指向当前节点。
    # 将 cur 指针指向 next。
    # 重复步骤 2-5 直到 cur 指向链表末尾。
    prev, curr = None, head

    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    return prev


"""
################################################################################################################
进阶

给你单链表的头指针 head 和两个整数 left 和 right ，其中 left <= right 。请你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表 。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/reverse-linked-list-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

################################################################################################################
"""


def reverseBetween(head: LinkedList, left: int, right: int) -> LinkedList:
    """
    创建一个 dummy 节点，令其 next 指向 head，令 pre 指向 dummy。
    将 pre 移动到第 left - 1 个节点，cur 移动到第 left 个节点。
    从 left 开始，按照反转链表的方式进行操作，直到 right 结束。
    将 pre 的 next 指向反转后链表的头节点，反转后链表的尾节点的 next 指向 cur。
    :param head:
    :param left:
    :param right:
    :return:
    """



    if not head or not head.next:
        return head
    dummy = LinkedList(0)
    dummy.next = head
    pre = dummy
    for i in range(left - 1):
        pre = pre.next
    cur = pre.next
    for i in range(right - left):
        next = cur.next
        cur.next = next.next
        next.next = pre.next
        pre.next = next
    return dummy.next


if __name__ == "__main__":
    a = LinkedList(1)
    b = LinkedList(2)
    c = LinkedList(3)
    a.next = b
    b.next = c

    print(reverseListNode(a))
