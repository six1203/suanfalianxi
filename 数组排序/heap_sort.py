"""
堆排序


堆排序(Heap Sort)是利用堆这种数据结构而设计的一种排序算法，是一种选择排序。

堆排序思路为: 将一个无序序列调整为一个堆，就能找出序列中的最大值（或最小值），然后将找出的这个元素与末尾元素交换，
这样有序序列元素就增加一个，无序序列元素就减少一个，对新的无序序列重复操作，从而实现排序。

"""


from typing import List


# heap_sort 代码实现


def build(arr: List[int], root, end):
    while True:
        child = 2 * root + 1  # 左子节点的位置
        if child > end:  # 若左子节点超过了最后一个节点，则终止循环
            break
        if (child + 1 <= end) and (
            arr[child + 1] > arr[child]
        ):  # 若右子节点在最后一个节点之前，并且右子节点比左子节点大，则我们的孩子指针移到右子节点上
            child += 1
        if arr[child] > arr[root]:  # 若最大的孩子节点大于根节点，则交换两者顺序，并且将根节点指针，移到这个孩子节点上
            arr[child], arr[root] = arr[root], arr[child]
            root = child
        else:
            break


def heap_sort(arr: List[int]):
    n = len(arr)
    first_root = n // 2 - 1  # 确认最深最后的那个根节点的位置
    for root in range(first_root, -1, -1):  # 由后向前遍历所有的根节点，建堆并进行调整
        build(arr, root, n - 1)

    for end in range(
        n - 1, 0, -1
    ):  # 调整完成后，将堆顶的根节点与堆内最后一个元素调换位置，此时为数组中最大的元素，然后重新调整堆，将最大的元素冒到堆顶。依次重复上述操作
        arr[0], arr[end] = arr[end], arr[0]
        build(arr, 0, end - 1)


def heapSort02(array: List):
    from heapq import heapify, heappop

    heapify(array)

    new_array = []

    for i in range(len(array)):
        new_array.append(heappop(array))

    return new_array


if __name__ == "__main__":
    array = [5, 1, 3, 67, 2]

    print(array)
