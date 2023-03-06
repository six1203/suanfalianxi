"""

这个实现的思路是将原数组拆分成一个元素和其余部分，然后对于剩余部分进行全排列，
将结果和当前元素拼接起来，得到最终结果。递归的终止条件是当数组为空时，返回一个空数组。
"""


def permutations(nums):
    if len(nums) == 0:
        return [[]]
    result = []
    for i in range(len(nums)):
        rest = nums[:i] + nums[i + 1 :]
        for p in permutations(rest):
            result.append([nums[i]] + p)

    return result


if __name__ == "__main__":

    # 测试代码
    nums = [1, 2]
    print(permutations(nums))
