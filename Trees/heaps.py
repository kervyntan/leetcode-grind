# Complete binary tree -> all levels except the last level has NO missing nodes
# In a heap, invariance when adding nodes is must maintain a complete binary tree
# always append nodes to the left and right child of the 2nd last level, to fill up the last level first (bfs)

# Order property (MIN heap)
# For each node, the values in the left and right subtree must be greater than the root value