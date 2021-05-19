new_List = [1,2,3,4]
result = new_List[0]
print(result)

if 1 in new_List:
    print(True)


for i in new_List:
    if new_List[i]==2:
        print(True)
        break


new_List.append(6)
print(new_List)

new_List.extend([7,8,'dog'])
print(new_List)

