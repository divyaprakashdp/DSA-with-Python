def quicksort(listToSort):
    if len(listToSort) <= 1:
        return listToSort
    pivot = listToSort[0]
    less_than_pivot = []
    greater_than_pivot = []

    for value in listToSort[1:]:
        if value <= pivot:
            less_than_pivot.append(value)
        else:
            greater_than_pivot.append(value)
    return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)


aList = [2, 87, 34, 69, 0, 2, 12, 45, 78]
print(quicksort(aList))