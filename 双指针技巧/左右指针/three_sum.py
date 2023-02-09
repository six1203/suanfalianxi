"""

给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请

你返回所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。


示例 1：

输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
解释：
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0 。
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0 。
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0 。
不同的三元组是 [-1,0,1] 和 [-1,-1,2] 。
注意，输出的顺序和三元组的顺序并不重要。
示例 2：

输入：nums = [0,1,1]
输出：[]
解释：唯一可能的三元组和不为 0 。
示例 3：

输入：nums = [0,0,0]
输出：[[0,0,0]]
解释：唯一可能的三元组和为 0 。
 

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/3sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


"""



from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        空间复杂度 O(1) 时间复杂度: O(n^2) ==>
        数组排序 O（nlogn） 遍历数组O（n） 双指针遍历 O（n），总体 O(nlogn) + O(n)*O(n), O(n^2)
        :param nums:
        :return:
        """

        n = len(nums)

        # 如果数组为null 或者长度小于3返回[]
        if not nums or n < 3:
            return []

        # 排序
        nums.sort()

        res = []

        # 遍历排序后的数组
        for i in range(n):

            # 排序后是从小到大，如果元素大于0，则三数之和不可能等于0，返回[]
            if nums[i] > 0:
                return res

            # 去重，当起始的值等于前一个元素，那么得到的结果将会和前一次相同
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # 左右指针
            L = i + 1
            R = n - 1


            while L < R:
                _sum = nums[i] + nums[L] + nums[R]

                if _sum == 0:

                    # 等于0，将三数的结果集加入到结果集中
                    res.append([nums[i], nums[L], nums[R]])

                    # 判断左指针和右指针 是否和下一位置重复，去除重复解
                    while L < R and nums[L] == nums[L + 1]:
                        L = L + 1


                    while L < R and nums[R] == nums[R - 1]:
                        R = R - 1


                    # 将L，R 移到下一位置，寻找新的解
                    L = L + 1
                    R = R - 1


                # 和大于0，右指针左移
                elif _sum > 0:
                    R = R - 1

                # 和小于0，左指针左移
                else:
                    L = L + 1
        return res


if __name__ == "__main__":
    print(Solution().threeSum(nums=[0, 0, 0]))
