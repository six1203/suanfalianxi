"""
给你一个整数数组 nums ，请你找出数组中乘积最大的非空连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。

测试用例的答案是一个 32-位 整数。

子数组 是数组的连续子序列。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/maximum-product-subarray
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


"""
from typing import List


def maxProduct(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return 0

    max_product = nums[0]
    min_product = nums[0]
    global_max = nums[0]

    for i in range(1, len(nums)):
        if nums[i] < 0:
            # 遇到负的，进行交换，这样最小的负数乘以当前元素就变成最大的了
            max_product, min_product = min_product, max_product

        # nums[i]为正数，那么最大子数组乘积为max(nums[i]*max_product), 其中max_product表示以i-1结尾的最大子数组乘积。
        max_product = max(nums[i], nums[i] * max_product)



        # nums[i]为负数，那么最大子数组乘积为min(nums[i], nums[i]*min_product)，其中min_product表示以i-1结尾的最小子数组乘积
        min_product = min(nums[i], nums[i] * min_product)


        # 同时需要维护全局最大乘积和，即以i结尾的最大子数组乘积和全局最大乘积中的较大值。
        global_max = max(global_max, max_product)



    return global_max


if __name__ == '__main__':
    nums = [2,3,-2,4]

    print(maxProduct(nums))

