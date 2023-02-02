"""
冒泡排序

1.比较相邻的元素,如果第一个比第二个大,就交换他们的位置
2.对每一对相邻元素做同样的工作，从开始第一队到结尾的最后一对
3.重复以上步骤，除了最后一个元素
"""
from typing import List


def bubbleSort(arr: List[int]):
    """
    冒泡排序(Bubble sort)
    :param arr: 待排序的List,此处限制了排序类型为int
    :return: 冒泡排序是就地排序(in-place)
    """
    length = len(arr)
    if length <= 1:
        return

    for i in range(length):
        is_made_swap = False  ## 设置标志位，若本身已经有序，则直接break


        for j in range(length - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                is_made_swap = True
        if not is_made_swap:
            break

    return arr


if __name__ == "__main__":
    print(bubbleSort(arr=[5, 1, 3, 67, 2]))




