"""
单链表的中点

给定一个头结点为 head 的非空单链表，返回链表的中间结点。

如果有两个中间结点，则返回第二个中间结点。

"""

# 算法思路
# 1. 快慢指针
# 2. 快指针每次走两步，慢指针每次走一步
# 3. 当快指针走到链表尾部时，慢指针正好走到链表中间



class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None


def find_mid_node(head):
	slow = fast = head

	while fast and fast.next:
		slow = slow.next
		fast = fast.next.next

	return slow


if __name__ == '__main__':
	head = ListNode(1)
	head.next = ListNode(2)
	head.next.next = ListNode(3)
	head.next.next.next = ListNode(4)
	head.next.next.next.next = ListNode(5)
	head.next.next.next.next.next = ListNode(6)

	print(find_mid_node(head).val)
