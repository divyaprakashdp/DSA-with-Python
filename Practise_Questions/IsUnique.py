"""
Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
cannot use additional data structures?
"""

# with additional data structure set
def is_unique(str):
    setOfChar = set(str)
    if len(setOfChar) < len(str):
        print("Not unique")
    else:
        print("unique")

def is_unique_new(str):
    char_set = []
    for i in range(len(str)):
        if str[i] in char_set:
            return False

        char_set.append(str[i])
    return True




print(is_unique_new("abgsa"))
