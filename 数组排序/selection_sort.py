"""
选择排序 时间复杂度O(n^2)
"""


def find_smallest(array):
    small_index = 0

    for i in range(1, len(array)):
        if array[i] < array[small_index]:
            small_index = i
    return small_index


def selection_sort(array):
    new_array = []
    for i in range(len(array)):
        small_index = find_smallest(array)
        new_array.append(array.pop(small_index))

    return new_array


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def selectionSort(array):
    for i in range(len(array) - 1):
        min_index = i

        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j

        if min_index != i:
            array[i], array[min_index] = array[min_index], array[i]

    return array


# 虽然时间复杂度都是O(n^2)，但是第二种方法的效率要比第一种方法高，第二种空间复杂度是O(1)，第一种是O(n)




if __name__ == "__main__":
    array = [5, 3, 6, 2, 10]
    # print(selection_sort(array))
    print(selection_sort(array))
