"""
栈
"""


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++链栈的实现+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        # 栈顶
        self.head = None

    def push(self, value):
        node = Node(value)
        node.next = self.head
        # 链表的头指针就是栈顶
        self.head = node

    def pop(self):
        node = self.head
        if node is None:
            raise Exception('This is an empty stack')
        self.head = node.text
        return node.value

    def peek(self):
        node = self.head
        if node is None:
            raise Exception('This is an empty stack')
        return node.value

    def is_empty(self):
        # 相当于头指针指向空
        return not self.head

    def size(self):
        node = self.head
        count = 0
        if node is None:
            raise Exception('This is an empty stack')
        while node is not None:
            count += 1
            node = node.next
        return count


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++中缀表达式求值+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# 创建两个栈，一个用于存储操作数，另一个用于存储操作符。
#
# 从左到右遍历表达式的每个元素：
#
# 如果该元素是一个数字，将其压入操作数栈。
# 如果该元素是一个操作符，则将其与操作符栈的顶部元素比较。如果该操作符的优先级高于栈顶元素的优先级，则将该操作符压入栈顶。否则，从操作符栈中取出栈顶元素，并将其作为两个操作数的运算符进行计算，将结果压入操作数栈。
# 当表达式遍历完毕后，操作数栈中仅剩一个数字，即为表达式的结果。

