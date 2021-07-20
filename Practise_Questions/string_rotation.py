"""
String Rotation: Assume you have a method i5Substring which checks ifone word is a substring
of another. Given two strings, 51 and 52, write code to check if 52 is a rotation of 51 using only one
call to isSubstring (e.g., waterbottle is a rotation of erbottlewat ).
"""

def string_rotation(s1, s2):
    length = len(s1)
    if length == len(s2) and length>0:
        s1s1 = s1+s1
        return isSubstring(s1s1, s2)
    return False

def isSubstring(str1, str2):
    if str2 in str1:
        return True
    return False

print(string_rotation("waterbottle", "erbottlewat"))