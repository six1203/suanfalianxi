"""
两数之和
"""

# 算法思路
# 类似二分查找，通过调节左右指针来调整sum的大小


def two_sum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    left, right = 0, len(nums) - 1
    while left < right:
        sum = nums[left] + nums[right]
        if sum == target:
            return [nums[left], nums[right]]
        elif sum < target:
            left += 1
        else:
            right -= 1
    return []
