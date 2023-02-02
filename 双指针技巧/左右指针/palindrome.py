"""
回文串就是正着读和反着读都一样的字符串。

比如说字符串 aba 和 abba 都是回文串，因为它们对称，反过来还是和本身一样；反之，字符串 abac 就不是回文串。


"""


# 算法思路：双指针技巧

# 1. 从字符串的两端开始，分别用两个指针指向字符串的第一个字符和最后一个字符
# 2. 比较两个指针指向的字符是否相等，如果不相等，则不是回文串，如果相等，则继续比较下一个字符


def is_palindrome(s):
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
