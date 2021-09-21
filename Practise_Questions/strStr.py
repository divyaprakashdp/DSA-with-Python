"""
leetcode - faster than 98%
"""

def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    if needle in haystack:
        return haystack.find(needle)
    else:
        return -1

print(strStr("hello", "ll"))