"""
计数排序(Counting Sort)是一种不比较数据大小的排序算法，是一种牺牲空间换取时间的排序算法。

计数排序适合数据量大且数据范围小的数据排序，如对人的年龄进行排序，对考试成绩进行排序等


1. 找到待排序列表中的最大值k，申请一个长度为k+1的计数列表，计数列表的初始值都是0
2. 遍历待排序列表，如果遍历的到元素是i，则计数列表中索引i的值加1。遍历完待排序列表，则计数列表中索引i的值j表示有j个i
3. 创建一个新列表，遍历计数列表，依次在新列表中添加j个i，新列表就是排好序的列表


时间复杂度：数据取值范围是常数 k，待排序元素个数是 n，总的时间复杂度是 O(n+k)

空间复杂度：计数排序只需要额外的空间复杂度为O(k)，所以计数排序的空间复杂度为O(k)。

稳定性：计数排序不会改变相等元素的相对位置，所以计数排序是稳定的。
"""


from typing import List


def countingSort(arr: List):

    max_num = max(arr)

    count_arr = [0] * (max_num + 1)

    for num in arr:
        count_arr[num] += 1

    ret = []
    for i in range(len(count_arr)):
        for _ in range(count_arr[i]):
            ret.append(i)

    return ret


array = [5, 1, 3, 67, 2]


if __name__ == "__main__":
    print(countingSort(arr=array))
