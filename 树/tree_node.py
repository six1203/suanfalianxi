from typing import List


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


a = TreeNode(1)

b = TreeNode(2)

c = TreeNode(3)

d = TreeNode(4)

e = TreeNode(5)

f = TreeNode(6)

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f


# ++++++++++++++++++++++++++++++++++++++++++++++++前序遍历+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# 前序遍历（先序遍历） 根节点->左子树->右子树


def pre_order_traverse(node):
    if node is None:
        return
    print(node.val)
    pre_order_traverse(node.left)
    pre_order_traverse(node.right)


def preOrderTraverse(node):
    if node is None:
        return
    stack = [node]
    while stack:
        node = stack.pop()
        print(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)


# ++++++++++++++++++++++++++++++++++++++++++++++++中序遍历+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# 中序遍历（中根遍历） 左子树->根节点->右子树


def in_order_traverse(node):
    if node is None:
        return
    in_order_traverse(node.left)
    print(node.val)
    in_order_traverse(node.right)


def inOrderTraverse(node):
    if node is None:
        return
    stack = []
    while stack or node:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        print(node.val)
        node = node.right


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack, rst = [root], []
        while stack:
            i = stack.pop()
            if isinstance(i, TreeNode):
                stack.extend([i.right, i.val, i.left])
            elif isinstance(i, int):
                rst.append(i)
        return rst


# ++++++++++++++++++++++++++++++++++++++++++++++++后序遍历+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# 后序遍历（后根遍历） 左子树->右子树->根节点


def post_order_traverse(node):
    if node is None:
        return
    post_order_traverse(node.left)
    post_order_traverse(node.right)
    print(node.val)


def postOrderTraverse(node):
    if node is None:
        return
    stack = [node]
    stack2 = []
    while stack:
        node = stack.pop()
        stack2.append(node)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    while stack2:
        print(stack2.pop().val)


# ++++++++++++++++++++++++++++++++++++++++++++++++层次遍历+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


def level_order_traverse(node):
    if node is None:
        return
    queue = [node]
    while queue:
        node = queue.pop(0)
        print(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


# ++++++++++++++++++++++++++++++++++++++++++++++++深度优先遍历+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


def depth_first_traverse(node):
    if node is None:
        return
    stack = [node]
    while stack:
        node = stack.pop()
        print(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)


# ++++++++++++++++++++++++++++++++++++++++++++++++广度优先遍历+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


def breadth_first_traverse(node):
    if node is None:
        return
    queue = [node]
    while queue:
        node = queue.pop(0)
        print(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


if __name__ == "__main__":
    # pre_order_traverse(a)
    # preOrderTraverse(a)

    # in_order_traverse(a)
    # inOrderTraverse(a)

    # post_order_traverse(a)
    # postOrderTraverse(a)

    # level_order_traverse(a)

    # depth_first_traverse(a)

    # breadth_first_traverse(a)

    print(Solution().inorderTraversal(a))
