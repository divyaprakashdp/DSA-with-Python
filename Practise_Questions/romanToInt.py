def romanToInt(s):
    if len(s) >= 1 or len(s) <= 15:
        output = 0
        master = {'I': 1,
                  'V': 5,
                  'X': 10,
                  'L': 50,
                  'C': 100,
                  'D': 500,
                  'M': 1000
                  }

        new_roman = list(s)
        for i in range(len(new_roman)):
            if new_roman[i] in (master.keys()):
                output = output + master[new_roman[i]]
                if i == len(new_roman) - 1:
                    break
                elif new_roman[i] == 'I' and (new_roman[i + 1] == 'V' or new_roman[i + 1] == 'X'):
                    output = output - 2
                elif new_roman[i] == 'X' and (new_roman[i + 1] == 'L' or new_roman[i + 1] == 'C'):
                    output = output - 20
                elif new_roman[i] == 'C' and (new_roman[i + 1] == 'D' or new_roman[i + 1] == 'M'):
                    output = output - 200
    else:
        return -1
    print(output)
    return output

def romanToInt_Faster(s):
    if len(s) >= 1 or len(s) <= 15:
        output = 0
        master = {'I': 1,
                  'V': 5,
                  'X': 10,
                  'L': 50,
                  'C': 100,
                  'D': 500,
                  'M': 1000
                  }

        new_roman = list(s)
        for i in range(len(new_roman)):
            currentNode = master[new_roman[i]]
            output = output + currentNode

            if i == len(new_roman) - 1:
                break

            nextNode = master[new_roman[i+1]]

            if currentNode >= nextNode:
                pass
            else:
                output = output - currentNode*2

    else:
        return -1
    print(output)



romanToInt_Faster('MCMXCIV')
"""
"III"
"IV"
"IX"
"LVIII"
"MCMXCIV"
"""
