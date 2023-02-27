
class Node:

    def __init__(self, t):
        # 树阶
        self.t = t
        # 关键字列表
        self.keys = []
        # 子节点列表
        self.children = []
        # 是否为叶子节点
        self.leaf = True
