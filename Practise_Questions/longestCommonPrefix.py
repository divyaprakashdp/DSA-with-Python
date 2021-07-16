def longestCommonPrefix(strs) -> str:
    if not strs:
        return ""

    for i, letter_group in enumerate(zip(*strs)):
        if len(set(letter_group)) > 1:
            return strs[0][:i]
    else:
        return min(strs)

input = ["amber","flow","flight"]
# ["flower", "flow", "flight", "fl", "float", "abra"]
print(longestCommonPrefix(input))
