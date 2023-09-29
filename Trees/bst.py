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
        return TreeNode(val)

    if val < root.val:
        # self.insertIntoBST(root.left, val)
        root.left = self.insertIntoBST(root.left, val)
        # root.left = TreeNode(val)
    elif val > root.val:
        # self.insertIntoBST(root.right, val)
        root.right = self.insertIntoBST(root.right, val)
        # root.right = TreeNode(val)
    return root

def min_value_node(root):
    curr = root

    # find min value in bst
    # if you draw it out, it's the same as traversing a linkedlist
    if curr and curr.left:
        curr = curr.left
    
    return curr

def remove(root, target):
    # 2 cases
    # node to remove has 0/1 child
    # node to remove has 2 children
    if not root:
        return False
    
    # check whether the node is in left/right subtree first (basically a search)
    if target > root.val:
        root.right = remove(root.right, target)
    elif target < root.val:
        root.left = remove(root.left, target)
    else:
        # when you found the target node
        # need to check if it's case 1 - 0/1 child
        # or case 2 - 2 children
        if not root.left:
            # means no left child
            return root.right

        elif not root.right:
            return root.left
        
        else:
            # case for 2 child nodes attached to target node
            
            # first, find the minimum value node attached to it
            # why? because in this case, if you are removing the root, means that you need to replace it
            # with the value of the minimum value node (draw it out to visualise)

            # replace the node to be deleted with the child that has a minimum value
            min_node = min_value_node(root.right)
            root.val = min_node.val
            root.right = remove(root.right, min_node.val)
    
    return root
        


first_node = TreeNode(2)
second_node = TreeNode(1)
third_node = TreeNode(3)
fourth_node = TreeNode(4)

first_node.left = second_node
first_node.right = third_node

third_node.right = fourth_node

# print(search(first_node, 4))
print(insert(first_node, TreeNode(4)))
