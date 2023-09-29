from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def bfs(root):
    # initialise the queue
    queue = deque()

    if root:
        queue.append(root)
    
    level_of_tree = 0
    # while there are nodes to be processed
    while len(queue) > 0:
        print("Level: ", level_of_tree)
        
        # loop through elements in the queue
        # len(queue) here acts as a 'constant'
        # doesn't change even though we append elements to it within the loop
        for i in range(len(queue)):
            # FIFO
            # ensure we visit the nodes from left to right
            curr = queue.popleft()
            print(curr.val)

            if curr.left:
                # if node has a left child
                queue.append(curr.left)
            if curr.right:
                # if node has a right child
                queue.append(curr.right)
        level_of_tree += 1



first_node = TreeNode(2)
second_node = TreeNode(1)
third_node = TreeNode(3)
fourth_node = TreeNode(4)

first_node.left = second_node
first_node.right = third_node

third_node.right = fourth_node

bfs(first_node)