"""
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from base import TreeNode

from typing import Optional


# 找到二叉树中两个节点的最近公共祖先
def lowest_common_ancestor(root, p, q):
    # 如果树为空，直接返回 None
    if not root:
        return None

    # 如果当前节点等于其中一个节点，直接返回当前节点
    if root == p or root == q:
        return root

    # 在左子树中查找 p 和 q 的最近公共祖先
    left = lowest_common_ancestor(root.left, p, q)
    # 在右子树中查找 p 和 q 的最近公共祖先
    right = lowest_common_ancestor(root.right, p, q)

    # 如果 p 和 q 分别在左右子树中，返回当前节点
    if left and right:
        return root

    # 如果只有左子树中存在 p 或 q，返回左子树中的最近公共祖先
    if left:
        return left

    # 如果只有右子树中存在 p 或 q，返回右子树中的最近公共祖先
    if right:
        return right


# 构造二叉树
A = TreeNode(3)
B = TreeNode(5)
C = TreeNode(1)
D = TreeNode(6)
E = TreeNode(2)
F = TreeNode(0)
G = TreeNode(8)
H = TreeNode(7)
J = TreeNode(4)

A.left = B
A.right = C
B.left = D
B.right = E
C.left = F
C.right = G
E.left = H
E.right = J






def bfs(root: Optional[TreeNode]):
    if not root:
        return

    queue = [root]
    ans = []
    while queue:
        q = queue.pop(0)
        if q.left:
            queue.append(q.left)

        if q.right:
            queue.append(q.right)

        ans.append(q.val)

    return ans

if __name__ == "__main__":
    print(lowest_common_ancestor(A, p=5, q=1))

    # print(bfs(A))
