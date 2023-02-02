"""
希尔排序，也称递减增量排序算法，是插入排序的一种更高效的改进版本。但希尔排序是非稳定排序算法。


希尔排序是把记录按下标的一定增量分组，对每组使用直接插入排序算法排序；随着增量逐渐减少，每组包含的关键词越来越多，当增量减至1时，整个文件恰被分成一组，算法便终止。

"""

# shell_sort 代码实现

from typing import List


def shell_sort(arr: List[int]):
    """
    希尔排序
    :param arr: 待排序的List
    :return: 希尔排序是就地排序(in-place)
    """
    length = len(arr)
    dist = length // 2

    while dist > 0:
        for i in range(dist, length):
            temp = arr[i]
            j = i
            while j >= dist and temp < arr[j - dist]:
                arr[j] = arr[j - dist]
                j -= dist
            arr[j] = temp
        dist //= 2


if __name__ == "__main__":
    array = [5, 1, 3, 67, 2]

    shell_sort(array)

    print(array)
