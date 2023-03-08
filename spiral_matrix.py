"""
螺旋矩阵

给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。

输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]

输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]
"""
from typing import List


def spiralOrder(matrix: List[List[int]]):
    left = 0
    right = len(matrix[0]) - 1
    top = 0
    bottom = len(matrix) - 1

    res = []
    while left <= right and top <= bottom:

        # 从左到右遍历上边界
        for i in range(left, right + 1):
            res.append(matrix[top][i])

        # 当前上边界已经遍历过了 记作+1
        top += 1

        # 从上到下遍历右边界
        for i in range(top, bottom + 1):
            res.append(matrix[i][right])
        # 当前右边界已经遍历过了，记作-1
        right -= 1

        # 从右到左遍历下边界
        if top <= bottom:
            for i in range(right, left - 1, -1):
                res.append(matrix[bottom][i])
        bottom -= 1

        # 从下到上遍历左边界
        if left <= right:
            for i in range(bottom, top - 1, -1):
                res.append(matrix[i][left])

        left += 1

    return res


if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(spiralOrder(matrix))
