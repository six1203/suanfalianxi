"""
无重复最长子串

https://leetcode.cn/problems/longest-substring-without-repeating-characters/
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
