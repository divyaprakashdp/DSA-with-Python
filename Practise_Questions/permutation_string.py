"""
Given a smaller string 5 and a bigger string b, design an algorithm to find all permutations
of the shorter string within the longer one. Print the location of each permutation
s: abbc
b: cbabadebbabbebabaabcebabe
"""

def find_permutation(str1,str2):
    list_str1 = list(str1)
    list_str2 = list(str2)
    print(list_str1)
    print(list_str2)
    len_list_str2 = len(list_str2)
    for i in range(len_list_str2):
        temp = list_str1.copy()
        if i == len_list_str2-3:
            break
        elif list_str2[i] == 'd':
            pass
        elif list_str2[i] in temp:
            temp.remove(list_str2[i])
            if list_str2[i+1] in temp:
                 temp.remove(list_str2[i+1])
                 if list_str2[i+2] in temp:
                     temp.remove(list_str2[i+2])
                     if list_str2[i+3] in temp:
                        temp.remove(list_str2[i+3])
                        print("Location: ",i)

find_permutation('abbc','cbabadcbbabbcbabaabccbabc')