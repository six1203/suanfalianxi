"""
给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。

请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

你必须设计并实现时间复杂度为 O(n) 的算法解决此问题。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/kth-largest-element-in-an-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。




这道题的解法比较多，可以使用快速排序、堆排序、快速选择等算法

"""



import random

from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pivot = random.choice(nums)

        nums1 = [num for num in nums if num > pivot]

        nums2 = [num for num in nums if num < pivot]

        if k <= len(nums1):
            return self.findKthLargest(nums1, k)

        elif k > len(nums) - len(nums2):
            return self.findKthLargest(nums2, k - (len(nums) - len(nums2)))

        else:
            return pivot
