def merge_sort(listToSort):
    """
    sorts a list in descending order
    Returns a new sordted list
    """
    if len(listToSort) <= 1:
        return listToSort

    leftHalf, rightHalf = split(listToSort)
    left = merge_sort(leftHalf)
    right = merge_sort(rightHalf)

    return merge(left, right)


def split(listToSplit):
    """
    Divide the unsorted list at midpoint into sublists
    Return two sublists left and right
    """

    mid = len(listToSplit) // 2
    left = listToSplit[:mid]
    right = listToSplit[mid:]

    return left, right


def merge(leftList, rightList):
    """
    Merges two lists(arrays), sorting them in process
    :returns a new merged list
    """
    l = []
    i = 0
    j = 0
    while i < len(leftList) and j < len(rightList):
        if leftList[i] < rightList[j]:
            l.append(leftList[i])
            i += 1
        else:
            l.append(rightList[j])
            j += 1

    while i < len(leftList):
        l.append(leftList[i])
        i += 1
    while j < len(rightList):
        l.append(rightList[j])
        j += 1

    return l


def verify_Sorted(listToTest):
    n = len(listToTest)

    if n == 0 or n == 1:
        return True
    else:
        return listToTest[0] < listToTest[1] and verify_Sorted(listToTest[1:])




aList = [56, 23, 45, 98, 100, 112, 7, 21]
a = merge_sort(aList)
print(a)
print("Is the list sorted:- ", verify_Sorted(a))
