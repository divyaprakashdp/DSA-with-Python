"""
Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome.
A palindrome is a word or phrase that is the same forwards and backwards. A permutation
is a rea rrangement of letters. The palindrome does not need to be limited to just dictionary words.
EXAMPLE
Input: Tact Coa
Output: True (permutations: "taco cat" "atco cta" etc.)
"""

def palindrome_permutation(str):
    space_index = str.index(" ")
    str_without_space = str.replace(" ", "").lower()
    len_str_without_space  = len(str_without_space)


    dict = {}
    for i in range(len_str_without_space):
        count = 0
        if str_without_space[i] in dict.keys():
            dict.update({str_without_space[i]:dict[str_without_space[i]]+1})
        else:
            dict.update({str_without_space[i]:1})

    count_unique_char = 0
    count_odd_char = 0
    for key, value in dict.items():
        if value==1:
            count_unique_char = count_unique_char+1
        elif value%2 > 0:
            count_odd_char = count_odd_char+1
    if (count_unique_char==1 or count_odd_char == 1):
        print("palindrome")
    else:
        print("not palindrome")

str = 'Taaaact Coa'
palindrome_permutation(str)