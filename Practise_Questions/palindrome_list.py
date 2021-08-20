"""
Palindrome: Implement a function to check if a linked list is a palindrome.
"""
import collections
def palindrome_list(list1):
    deque = collections.deque(list1)
    isPalindrome = False
    for i in range(len(deque)//2):
        last = deque.pop()
        first = deque.popleft()
        if last==first:
            isPalindrome = True
            pass
        else:
            isPalindrome = False
            break
    if isPalindrome:
        print("palindrome")
    else:
        print("not palindrome")
    # print(deque)

palindrome_list(['a','b','c','o','o','c','b','a'])
