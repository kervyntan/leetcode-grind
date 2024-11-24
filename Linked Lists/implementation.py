class Node:
    # Create Node class, and use the class method
    # Since there are many methods in LinkedList class that need node creation
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        # Create a node, initializes new LinkedList
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
        
    # def append(self, value):
        # Create new Node, add Node to end
        
    # def prepend(self, value):
    #     # Create new Node, add Node to start
        
    
    # def insert(self, value):
        # Create new Node, insert at position
        
linked_list = LinkedList(4)
print(linked_list.head.value)