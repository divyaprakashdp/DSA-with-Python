"""
Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.
"""

def check_permutation(strs):
    sorted_strs = []
    for i in range(len(strs)):
        list_Chars = list(strs[i])
        list_Chars.sort()
        sorted_strs.append("".join(list_Chars))
    print(sorted_strs)
    strs_set = set(sorted_strs)
    if len(strs_set) > 1:
        return False
    return True



strs = ['adx', 'azd']
    #['abc', 'acb', 'bac', 'bca', 'gab', 'cba']
print(check_permutation(strs))