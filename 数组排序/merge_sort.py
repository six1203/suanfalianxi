"""
归并排序

合并排序是一种排序算法，它使用分而治之的方法对列表进行排序。
它的工作原理是将列表分成更小的子列表，对这些子列表进行排序，然后将它们合并回一起形成一个排序列表。

其运行时间总是 O（n logn）
"""


def merge_sort(arr):
    # Base case: if the input array has length 1, it is already sorted
    if len(arr) == 1:
        return arr

    # Recursive case: split the input array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort the two halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the sorted halves and return the result
    return merge(left_half, right_half)


def merge(left, right):
    # Initialize an empty result list
    result = []

    # While there are elements in both lists
    while left and right:
        # Append the smaller element to the result list
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    # Append the remaining elements, if any, to the result list
    result.extend(left)
    result.extend(right)
    return result


if __name__ == "__main__":
    unsorted_list = [5, 2, 4, 1, 3]
    sorted_list = merge_sort(unsorted_list)
    print(sorted_list)  # prints [1, 2, 3, 4, 5]
