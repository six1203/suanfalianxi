"""
桶排序(Bucket sort)是一种通过分桶和合并实现的排序算法，又被称为箱排序。其主要思想是：将待排序集合中处于同一个值域的元素存入同一个桶中，
也就是根据元素值特性将集合拆分为多个区域，则拆分后形成的多个桶，从值域上看是处于有序状态的。对每个桶中元素进行排序，则所有桶中元素构成的集合是已排序的。

桶排序是计数排序的扩展版本，计数排序可以看成每个桶只存储相同元素，
而桶排序每个桶存储一定范围的元素。桶排序需要尽量保证元素分散均匀，否则当所有数据集中在同一个桶中时，桶排序失效。


桶排序先将数据分到有限数量的桶里，然后对每一个桶内的数据进行排序(桶内排序可以使用任何一种排序算法，如快速排序)，最后将所有排好序的桶合并成一个有序序列，列表排序完成。

桶排序需要占用很多额外的空间，对桶内数据进行排序，选择哪种排序算法对于性能的影响至关重要。桶排序适用的场景并不多，用得多一点的是基于桶排序思想的计数排序和基数排序。


1. 求出待排序列表中的最大值和最小值，得到数据的范围。

2. 根据数据的范围，选择一个适合的值构建有限数量的桶，确定每个桶的数据范围。如数据范围是[0,100)，将数据分成10个桶，第一个桶为[0,10)，第二个桶为[10,20)，以此类推。

3. 将待排序列表中的数据分配到对应的桶中。

4. 对每一个桶内的数据进行排序，这里可以采用任意一种排序算法，建议采用时间复杂度小的排序算法。

5. 将所有桶中的数据依次取出，添加到一个新的有序序列中，列表排序完成。


时间复杂度： 平均为O(n)，最坏为O（n^2)

空间复杂度： 桶排序过程中需要创建k个桶的额外空间，以及n个元素的额外空间，所以桶排序的空间复杂度为 O(n+k)。

稳定性：桶排序的稳定性取决于桶内排序使用的算法，如果是队列，可以保证相同的元素取出和放回的相对位置不变，即排序是稳定的，
而如果用栈来实现，则排序一定是不稳定的。由于桶排序可以做到稳定，所以桶排序是稳定的排序算法。

"""


from typing import List


def bucket_sort(array: List):
    min_num, max_num = min(array), max(array)

    # 3为每个桶存放的元素个数，可以任意调整
    bucket_num = (max_num - min_num) // 3 + 1


    buckets = [[] for _ in range(int(bucket_num))]


    for num in array:
        buckets[int((num - min_num) // 3)].append(num)

    new_array = list()

    for i in buckets:
        # 桶内排序，建议采用复杂度小的算法
        for j in sorted(i):
            new_array.append(j)

    return new_array


if __name__ == "__main__":
    array = [5, 1, 3, 67, 2]
    print(bucket_sort(array))
