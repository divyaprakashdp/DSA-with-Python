'''
Given an array of distinct integer values, count the number of pairs of integers that
have difference k. For example, given the array {1, 7, 5, 9, 2, 12, 3} and the difference
k = 2, there are four pairs with difference 2: (1, 3), (3, 5), (5, 7), (7, 9)
'''

def pair_finder(input_array):
    dict = {}
    for i in range(len(input_array)):
        dict.__setitem__(i,input_array[i])
    print(dict)
    x = 2
    output = []
    for item in dict.values():
        if item-x in dict.values():
            output.append({item-x, item})
    print(output)

pair_finder([1, 7, 5, 9, 2, 12, 3])