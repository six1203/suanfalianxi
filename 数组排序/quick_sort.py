"""
快排算法


（1） 选择基准值
（2） 将数组分成两个子数组：小于基准值的元素组成的子数组和大于基准值的元素组成的子数组
（3） 对这两个子数组进行快速排序


平均时间复杂度：O(n logn)，最坏时间复杂度为O(n^2)




快排选取基准值的优化：
    (1) 取第一个或者最后一个：简单但很傻的选择，如果数组本身就是有序的，当输入序列是升序或者降序时，会导致另外一个子数组是空的，这种做法最坏时间复杂度为O(n^2)
    (2) 随机选择: 是比较安全的做法。除非随机数发生器出现错误，并且连续产生劣质分割的概率比较低。但随机数生成开销较大，这样就增加了运行时间。
    (3) 三数中值分割法：




"""
import random
from typing import List


def quick_sort(array: List):

    # 基准条件：为空或只包含一个元素的数组是"有序"的
    if len(array) < 2:
        return array

    # 基准值
    # 注意这里选择的基准值并不是很好，因为数组并没有被分成两半，存在另外一个子数组为空的，导致调用栈非常长
    # 最糟糕情况下栈长为O(n)，最佳情况下栈长为O（logn）
    base = array[0]

    # 将数组分为两个子数组，一个数组放不大于基准值的值，另外一个数组放大于基准值的值
    less = [i for i in array[1:] if i <= base]

    greater = [i for i in array[1:] if i > base]

    return quick_sort(less) + [base] + quick_sort(greater)



def quick_sort_02(array: List):

    # 基准条件：为空或只包含一个元素的数组是"有序"的
    if len(array) < 2:
        return array


    # 基准值优化，采取随机选择，但是会增加运行时间
    base = random.choice(array)

    # 将数组分为两个子数组，一个数组放不大于基准值的值，另外一个数组放大于基准值的值
    less = [i for i in array[1:] if i <= base]

    greater = [i for i in array[1:] if i > base]

    return quick_sort_02(less) + [base] + quick_sort_02(greater)








if __name__ == "__main__":

    print(quick_sort([5, 3, 6, 2, 10]))
