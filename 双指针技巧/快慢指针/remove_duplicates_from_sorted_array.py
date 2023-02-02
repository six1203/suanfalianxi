"""
删除有序数组中的重复项
"""
# 算法思路
# 1. 用快慢指针，快指针遍历数组，慢指针记录不重复元素的位置


from typing import List


def remove_duplicates(nums: List[int]) -> int:
    slow, fast = 0, 1
    while fast < len(nums):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
        fast += 1
    return slow + 1
