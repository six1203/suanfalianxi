from typing import Optional

from dataclasses import dataclass


# Python 表示二叉树
@dataclass
class TreeNode:
    # node 节点上的值
    val: int | str
    # 左子树
    left: Optional["TreeNode"] = None
    # 右子树
    right: Optional["TreeNode"] = None
