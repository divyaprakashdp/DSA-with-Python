from Binary_Search import binary_search
from Linear_Search import linear_Search
from Recursive_Binary_Search import recursive_Binary_Search


def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found in the list")


number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = linear_Search(number, 11)
verify(result)

resultNew = binary_search(number, 6)
verify(resultNew)

resultNew1 = recursive_Binary_Search(number,8)
verify(resultNew1)

