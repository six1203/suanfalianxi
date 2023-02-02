"""
给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度

不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。

元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
"""


# 算法思路

# 1. 双指针技巧，快慢指针

# 2. 快指针遍历数组，慢指针记录不等于val的元素

# 3. 快指针遍历完毕后，慢指针指向的位置即为新数组的长度

# +++++++++++++++++++++++++++++++++++++++++++++快慢指针实现+++++++++++++++++++++++++++++++++++++++++++++++

# 算法实现
def remove_element(nums, val):
    slow = fast = 0

    while fast < len(nums):
        if nums[fast] != val:
            nums[slow] = nums[fast]
            slow += 1
        fast += 1

    return slow


# +++++++++++++++++++++++++++++++++++++++++++++倒序遍历实现+++++++++++++++++++++++++++++++++++++++++++++++
def removeElement(nums, val):
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] == val:
            nums.pop(i)

    return len(nums)


# +++++++++++++++++++++++++++++++++++++++++++++while循环实现+++++++++++++++++++++++++++++++++++++++++++++++
def removeElement2(nums, val):
    while val in nums:
        nums.remove(val)
