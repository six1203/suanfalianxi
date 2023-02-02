"""
最长回文串

给你一个字符串 s，找到 s 中最长的回文子串。

如果字符串的反序与原始字符串相同，则该字符串称为回文字符串。

输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。

输入：s = "cbbd"
输出："bb"

"""


# 算法思路
# 左右指针，从中心向两端扩散

# 具体思路是，构建一个【从中心往两边扩散】的函数——扩散的条件是，不超出边界且扩散的两边的元素相等，函数返回【回文字符串】。基于构建的函数，以此判断s中所有的位置，用一个res保留最长的结果。
# 大白话是，每个位置都判断下，以该位置为中心的回文串最长为多少，遍历一遍，保留最长的那个。
# 其中有一个细节，中心元素需要区分1个或者2个的情况（回文串中元素个数为奇数/偶数）


def longestPalindrome(s: str) -> str:
    res = ""
    for i in range(len(s)):
        s1 = expandAroundCenter(s, i, i)
        s2 = expandAroundCenter(s, i, i + 1)
        if len(s1) > len(res):
            res = s1
        if len(s2) > len(res):
            res = s2
    return res


def expandAroundCenter(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left + 1 : right]


if __name__ == "__main__":
    s = "babad"
    print(longestPalindrome(s))
