# Backtracking
# Determine if a path exists from the root of the tree to a leaf node. It may not contain any zeroes*

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def leaf_path(root, path):
    # path cannot contain 0s
    # if hit null, then just return False
    if not root or root.val == 0:
        return False

    path.append(root.val)

    # check if currently checked out node is a leaf node
    if not root.left and not root.right:
        return True
    
    # recursively check the left subtree of the current root
    # if it returns True overall, it means a path exists
    if leaf_path(root.left, path):
        return True
    
    if leaf_path(root.right, path):
        return True
    
    path.pop()
    return False


first_node = TreeNode(2)
second_node = TreeNode(1)
third_node = TreeNode(3)
fourth_node = TreeNode(4)

first_node.left = second_node
first_node.right = third_node

third_node.right = fourth_node

# path from root to the leaf node
path = []

leaf_path(first_node, path)
print(path)