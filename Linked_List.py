class Node:
    """
    An object for storing a single node of a linked list.
    Models two attributes - data and the link to the next node in the list.
    """
    data = None
    next_Node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "<Node data : %s>" % self.data


class Linked_List:
    """Singly LInked List"""

    def __init__(self):
        self.head = None

    def __repr__(self):
        """
        Return a string representation of the list.
        Takes O(n) time.
        """
        nodes = []
        current = self.head
        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_Node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)
            current = current.next_Node
        return '-> '.join(nodes)

    def is_empty(self):
        return self.head == None

    def size(self):
        """
        Returns the number of nodes in the list.
        Takes O(n) time
        """
        current = self.head
        count = 0

        while current:
            count = count + 1
            current = current.next_Node
        return count

    def add(self, data):
        """
        Add a new node with data at head of the list
        Takes O(1) time
        """
        new_node = Node(data)
        new_node.next_Node = self.head
        self.head = new_node
