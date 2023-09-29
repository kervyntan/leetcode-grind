class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
def search(root, target):
    if not root:
        return False

    # check if the value should be in the left or right subtree, for each new root value
    if target < root.val:
        return search(root.left, target)
    
    elif target > root.val:
        return search(root.right, target)
    
    else:
        return True

def insert(root, target_node):
    if not root:
        return False
    
    # check if target value should be put into the left or right subtree
    if target_node.val < root.val:
        insert(root.left, target_node)
        root.left = target_node
    
    elif target_node.val > root.val:
        insert(root.right, target_node)
        root.right = target_node
    
    return root

def min_value_node(root):
    curr = root

    # find min value in bst
    # if you draw it out, it's the same as traversing a linkedlist
    if curr and curr.left:
        curr = curr.left
    
    return curr

first_node = TreeNode(2)
second_node = TreeNode(1)
third_node = TreeNode(3)
fourth_node = TreeNode(4)

first_node.left = second_node
first_node.right = third_node

third_node.right = fourth_node

# print(search(first_node, 4))
print(insert(first_node, TreeNode(5)))
