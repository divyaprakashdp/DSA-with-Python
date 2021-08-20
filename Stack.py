class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        """
        push an item into the stack
        :param item:
        :return:
        """
        self.items.append(item)

    def pop(self):
        """
        Removes the top item in the stack
        :return: top item in the stack
        """
        if self.items:
            return self.items.pop()
        return None

    def peek(self):

        if self.items:
            return self.items[-1]
        return None

    def size(self):
        """

        :return: Size of the stack
        O(1)
        """
        return len(self.items)

    def is_empty(self):
        """

        :return: True if stack is empty
        """
        if self.items:
            return True
        return False



my_stack = Stack()
my_stack.pop()
my_stack.push('apple')
my_stack.push('banana')
print(my_stack.items)
my_stack.pop()
print("After pop: ",my_stack.items)

