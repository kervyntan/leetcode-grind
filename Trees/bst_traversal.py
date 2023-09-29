class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# O(n) -> where n is the number of nodes in the tree
# Produces sorted list of values in the bst
# O(n log n) -> to sort random values using a BST + in-order traversal
def inorder(root):
    # for EVERY node, you traverse the left subtree, then after that the root, then the right subtree
    if not root:
        return False
    
    inorder(root.left)
    print(root.val)
    inorder(root.right)

# preorder -> root, then left subtree, then right subtree
def preorder(root):
    if not root:
        return False
    
    print(root.val)
    preorder(root.left)
    preorder(root.right)

# postorder -> left subtree, right subtree then root
def postorder(root):
    if not root:
        return False
    
    postorder(root.left)
    postorder(root.right)
    print(root.val)

def reverse_order(root):
    if not root:
        return False
    
    reverse_order(root.right)
    print(root.val)
    reverse_order(root.left)

    
first_node = TreeNode(2)
second_node = TreeNode(1)
third_node = TreeNode(3)
fourth_node = TreeNode(4)

first_node.left = second_node
first_node.right = third_node

third_node.right = fourth_node

reverse_order(first_node)