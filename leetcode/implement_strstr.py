"""
    Name: Implement strStr()
    Source: LeetCode - 28
    Link: https://leetcode.com/problems/implement-strstr/
    Description: Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
"""

# Real life implementation
# Runtime: 36 ms
# Memory Usage: 13.4 MB
def strStr_lame(haystack: str, needle: str) -> int:
    return haystack.find(needle)

# Naive implementation
# Runtime: 52 ms, 28.05 percentile
# Memory Usage: 13.3 MB, 5.13 percentile
def strStr(haystack: str, needle: str) -> int:
    struct_len = len(needle)
    for i in range(0, len(haystack)):
        struct = haystack[i:i+struct_len]
        if struct == needle:
            return i
    return -1

print(strStr("mississippi", "issi"))