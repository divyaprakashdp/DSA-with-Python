def linear_Search(listToCheck, target):
    """Returns the position in the list if found, else return None"""
    print("Linear Search: Searching", target, "...")
    for i in range(0, len(listToCheck)):
        if listToCheck[i] == target:
            return i

    return None
