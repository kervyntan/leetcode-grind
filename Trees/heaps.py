# Complete binary tree -> all levels except the last level has NO missing nodes
# In a heap, invariance when adding nodes is must maintain a complete binary tree
# always append nodes to the left and right child of the 2nd last level, to fill up the last level first (bfs)

# Order property (MIN heap)
# For each node, the values in the left and right subtree must be greater than the root value

# implemented using an array
# Start at index 1 i.e. root is placed at index 1
# ^^ to allow formulas (only work because of the complete binary tree property):
# leftChild : 2 * index
# rightChild : 2 * index + 1
# parent : index / 2
class Heap:
    def __init__(self):
        self.heap = [0]

    # min-heap
    def push(self, val):
        # append the new val to the heap first
        self.heap.append(val)

        # obtain index of the newly inserted value
        i = len(self.heap) - 1

        # Percolate up
        # shift it up, while the order property is not satisfied
        # comparing the new value to the parent
        while self.heap[i] < self.heap[i // 2]:
            temp = self.heap[i]

            # put the parent into where the newly inserted value is
            self.heap[i] = self.heap[i // 2]

            # parent is now the newly inserted value
            self.heap[i // 2] = temp

            # go to the new index of the newly inserted value
            i = i // 2
    
    # O(log n) -> height of the heap
    def pop(self):
        if len(self.heap) == 1:
            return None
        if len(self.heap) == 2:
            return self.heap.pop()
        
        res = self.heap[1]

        # move last value to root
        self.heap[1] = self.heap.pop()
        
        # Start percolating down at the first element
        i = 1

        # checks if the current eleemnt has a left child
        # recall that a leftChild is 2 * current index
        while 2 * i < len(self.heap):
            if(
                # if there's a right child
                2 * i + 1 < len(self.heap)
                and
                # if current position of the element
                # right child is LESS than left child
                self.heap[2 * i + 1] < self.heap[2 * i]
                and
                # if current element
                # greater than the right child
                self.heap[i] > self.heap[2 * i + 1]
            ):
                # Then swap the right child
                temp = self.heap[i]
                self.heap[i] = self.heap[2 * i + 1]
                self.heap[2 * i + 1] = temp
                # shift index to where the element got shifted to
                i = 2 * i + 1
            
            # if current element is greater than it's left child
            elif self.heap[i] > self.heap[2 * i]:
                temp = self.heap[i]
                self.heap[i] = self.heap[2 * i]
                self.heap[2 * i] = temp
                i = 2 * i
            else:
                break

        return res
