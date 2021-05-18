def recursive_Binary_Search(list, target):
    print("Recursive Binary Search: Searching ", target, "...")
    if len(list) == 0:
        return False
    else:
        midpoint = (len(list))//2

        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                return recursive_Binary_Search(list[midpoint+1:], target)
            else:
                return recursive_Binary_Search(list[:midpoint], target)
