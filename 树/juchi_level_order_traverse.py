"""
二叉树锯齿形层序遍历
"""




from collections import deque
from dataclasses import dataclass
from typing import Optional, List


@dataclass
class TreeNode:
    value: int | str
    left: Optional[int] = None
    right: Optional[int] = None


def juchi_level_order_traverse(root: Optional[TreeNode]) -> List[List[int | str]]:
    if root is None:
        return

    ans: List[List[int | str]] = []

    d = deque([root])

    is_order_left = True
    while d:

        node_values: List[int | str] = []
        for i in range(len(d)):
            node = d.popleft()

            if node.left:
                d.append(node.left)

            if node.right:
                d.append(node.right)

            node_values.append(node.value)

        ans.append(node_values if is_order_left else node_values[::-1])

        is_order_left = not is_order_left

    return ans
