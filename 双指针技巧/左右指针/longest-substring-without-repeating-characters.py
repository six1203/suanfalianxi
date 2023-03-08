"""
无重复最长子串

https://leetcode.cn/problems/longest-substring-without-repeating-characters/



具体来说，我们可以使用一个哈希集合来记录当前窗口中出现过的字符，
同时使用一个变量来记录窗口的起始位置。
初始时，左指针和右指针都指向字符串的第一个字符，窗口中只包含该字符。
然后我们向右移动右指针，如果右指针指向的字符在哈希集合中已经出现过，
则向右移动左指针直到窗口中不包含该字符为止。
在每次移动右指针的过程中，我们需要更新窗口的长度并记录最长的无重复字符子串的长度和起始位置。
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)

        char_set = set()

        max_len, l, r = 0, 0, 0

        while l < n and r < n:
            if s[r] not in char_set:
                char_set.add(s[r])
                r += 1
                max_len = max(max_len, r - l)
            else:
                char_set.remove(s[l])
                l += 1
        return max_len
