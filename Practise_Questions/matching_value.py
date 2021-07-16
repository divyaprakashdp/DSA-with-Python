'''
Given two sorted arrays, find the number of elements in common. The arrays are the same length
and each has all distinct elements.
Ex:
A: 13 27 ->35 ->40 49 ->55 59
B: 17 ->35 39 ->40 ->55 58 60
'''


def find_matching(array1, array2):
    count = 0
    for i in range(len(array1)):
        if array1[i] in array2:
            count = count+1
    print(count)


find_matching([13,27,35,40,49,55,59], [17,35,39,40,55,58,60])

