"""
判断两个链表是否相交，如果相交，返回相交的节点，否则返回None
"""


# 算法思路：

# 两个指针p1和p2分别指向两个链表的头节点，然后同时向后移动，
# 当p1到达链表1的尾节点时，将p1指向链表2的头节点，当p2到达链表2的尾节点时，将p2指向链表1的头节点，这样两个指针就可以同时移动，当两个指针相遇时，就是两个链表的交点。


class Node:
	def __init__(self, value):
		self.value = value
		self.next = None


def is_intersect(head1, head2):
	p1 = head1

	p2 = head2

	while p1 != p2:
		if p1 is None:
			p1 = head2
		else:
			p1 = p1.next

		if p2 is None:
			p2 = head1
		else:
			p2 = p2.next

	return p1


if __name__ == '__main__':
	head1 = Node(1)
	head1.next = Node(2)
	head1.next.next = Node(3)
	head1.next.next.next = Node(4)
	head1.next.next.next.next = Node(5)

	head2 = Node(6)
	head2.next = Node(7)
	head2.next.next = Node(8)
	head2.next.next.next = head1.next.next

	print(is_intersect(head1, head2).value)
