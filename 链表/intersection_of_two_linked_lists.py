"""
相交链表

给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表不存在相交节点，返回 null 。

图示两个链表在节点 c1 开始相交：

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/intersection-of-two-linked-lists
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from base import LinkedList

def getIntersectionNode(headA:LinkedList, headB: LinkedList):


    if headA is None or headB is None:
        return

    ptrA = headA
    ptrB = headB

    while ptrA != ptrB:
        ptrA = headB if ptrA is None else ptrA.next
        ptrB = headA if ptrA is None else ptrB.next


    return ptrA
