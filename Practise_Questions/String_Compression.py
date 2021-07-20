"""
String Compression: Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become a2b1c5a3. If the
"compressed" string would not become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase
"""

def string_compression(strIP):
    count = 0
    strlist = list(strIP)
    newstrlist = []
    while len(strlist) > 0 :
        if len(strlist) == 1:
            count=count+1
            newstrlist.append(strlist[0]+str(count))
        elif strlist[0]==strlist[1]:
            count=count+1
        else:
            count=count+1
            newstrlist.append(strlist[0]+str(count))
            count=0
        strlist.pop(0)
    print("".join(newstrlist))

string_compression("aabcccggccaaaa")