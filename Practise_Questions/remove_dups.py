"""
Remove Dups: Write code to remove duplicates from an unsorted linked list.
"""

def remove_dups(str1):
    list1 = []
    for i in range(len(str1)):
        if str1[i] in list1:
            pass
        else:
            list1.append(str1[i])
    print("".join(list1))

remove_dups("FOLLOW UP")