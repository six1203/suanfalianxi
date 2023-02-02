"""
插入排序

1.从第一个元素开始，该元素可以认为已经被排序；

2.取出下一个元素，在已经排序的元素序列中从后向前扫描；

3.如果该元素（已排序）大于新元素，将该元素移到下一位置；

4.重复步骤 3，直到找到已排序的元素小于或者等于新元素的位置；

5.将新元素插入到该位置后；

6.重复步骤 2~5。


时间复杂度： 平均为O（n^2）, 空间复杂度为O（1）

"""
from typing import List


def insertionSort(array: List):
    if len(array) < 2:
        return array

    for i in range(len(array)):

        value = array[i]

        j = i - 1

        while j >= 0 and array[j] > value:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = value

    return array


array = [5, 1, 3, 67, 2]


if __name__ == "__main__":
    print(insertionSort(array))
