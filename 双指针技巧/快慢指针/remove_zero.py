"""
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

请注意 ，必须在不复制数组的情况下原地对数组进行操作。
"""


def move_zeroes(nums):
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] == 0:
            nums.pop(i)
            nums.append(0)

    return nums


def moveZeroes(nums):
    slow = fast = 0

    while fast < len(nums):
        if nums[fast] != 0:
            nums[slow] = nums[fast]
            slow += 1
        fast += 1

    while slow < len(nums):
        nums[slow] = 0
        slow += 1

    return nums
