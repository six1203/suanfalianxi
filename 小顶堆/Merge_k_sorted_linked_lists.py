"""
合并k个有序链表
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


from typing import List


# =================================================================分治法=================================================================
# 算法流程如下：
# 1. 如果链表为空或者只包含一个链表,直接返回
# 2. 将链表数组平均分为两部分,分别对左右两部分分别调用递归函数进行合并
# 3. 将左右两部分合并的结果进行合并
# 4. 返回合并后的链表


def mergeKLists(lists: List[ListNode]):
    if not lists:
        return None
    if len(lists) == 1:
        return lists[0]

    mid = len(lists) // 2

    left = mergeKLists(lists[:mid])

    right = mergeKLists(lists[mid:])

    return mergeTwoLists(left, right)


def mergeTwoLists(l1: ListNode, l2: ListNode):
    if not l1:
        return l2

    if not l2:
        return l1

    if l1.val < l2.val:
        l1.next = mergeTwoLists(l1.next, l2)
        return l1
    else:
        l2.next = mergeTwoLists(l1, l2.next)
        return l2


# ==================================================================小顶堆==================================================================
# 算法流程如下：
# 1. 将所有的链表的首节点放入小顶堆中
# 2. 从小顶堆中取出最小的节点,并将它的next指针指向链表的末尾
# 3. 如果当前节点有next指针,则将next指针放入小顶堆中

# 这种方法的时间复杂度为 O(n log k)，其中 n 是所有链表中节点的总数，k 是链表的数量。

# 堆这个优先级队列元素个数最大是k，pop或者push的时间复杂度是logk，一共有n个链表节点，所以总的时间复杂度是O(nlogk)。


from heapq import heapify, heappop, heappush


def merge_k_lists(lists: List[ListNode]):
    # 将所有链表的首节点放入小顶堆中
    heap = [(node.val, node) for node in lists if node]
    heapify(heap)

    # 初始化结果链表的头节点
    dummy = ListNode(None)

    cur = dummy

    while heap:
        # 取出最小的节点
        val, node = heappop(heap)

        # 将当前节点加入结果链表
        cur.next = node

        cur = cur.next

        # 如果当前节点有 next 指针，将 next 节点加入小顶堆
        if node:
            heappush(heap, (node.val, node))

    # 返回结果链表的头节点的 next 指针，即真正的链表头
    return dummy.next


if __name__ == "__main__":
    a = ListNode(1)
    b = ListNode(4)
    c = ListNode(5)
    a.next = b
    b.next = c

    d = ListNode(1)
    e = ListNode(3)
    f = ListNode(4)
    d.next = e
    e.next = f

    g = ListNode(2)
    h = ListNode(6)
    g.next = h

    lists = [a, d, g]

    res = mergeKLists(lists)

    while res:
        print(res.val)
        res = res.next
