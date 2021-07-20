"""
One Away: There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to check if they are
one edit (or zero edits) away.
EXAMPLE
pale, ple -> true
pales, pale -> true
pale, bale -> true
pale, bake -> false
"""


def isDifferent(str1, str2):
    count = 0
    if len(str1) >= len(str2):
        len_range = len(str2)
    else:
        len_range = len(str1)
    isDiff = False
    for i in range(len_range):
        if i > len_range:
            break
        elif str1[i] == str2[i]:
            isDiff = True
            if str1[i + 1] == str2[i]:
                isDiff = True
            else:
                isDiff = False
        else:
            if str1[i+1] == str2[i+1]:
                isDiff = True
            else:
                isDiff = False
    return isDiff


def one_away(str1, str2):
    if str1 == str2:
        print("it's same")
    else:
        if not isDifferent(str1, str2):
            print("one away")
        else:
            print("Different")


one_away("pale", "pales")
