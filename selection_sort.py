def selection_sort(listToSort):
    sortedList = []
    for i in range(0, len(listToSort)):
        index_to_move = index_of_min(listToSort)
        sortedList.append(listToSort.pop(index_to_move))
    return sortedList


def index_of_min(unsortedList):
    min_index = 0
    for i in range(1, len(unsortedList)):
        if unsortedList[i] < unsortedList[min_index]:
            min_index = i
    return min_index


aList = [2, 87, 34, 69, 0, 12, 45, 78]
print(selection_sort(aList))
