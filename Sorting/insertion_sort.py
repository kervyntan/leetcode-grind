# Invariance:
# Assume that elements before the pointer element are already in sorted order.
# WIth each swap, the sub array of length n - 1, where n is the index of the current pointer, is already sorted

def insertion_sort(array):
    # Loop through the array
    # Start with a pointer that is 1 before the current loop's index
    # Compare the pointer element with current index's element
    # if the current index's element is smaller than the pointer, then swap the elements
    # repeat until the currnt index's element is bigger than the pointer, or when pointer goes out of bounds

    # use range loop to start from index 1, and get index for each element
    for index in range(1, len(array)):
        # pointer is right before the current index to compare values
        # Only need pointer to be initialized to right before
        # since the invariance states that all elements in the subarray before current index is already sorted
        pointer = index - 1 

        # while loop here, so you can keep performing swaps if the element is smaller than all the elements 
        # in the sorted subarray before it
        while (pointer >= 0 and array[pointer + 1] <= array[pointer]):
            temp = array[pointer]
            array[pointer] = array[pointer + 1]
            array[pointer + 1] = temp
            # decrement pointer to compare values with the previous values in subarray 
            pointer -= 1
        
    return array

print(insertion_sort([1,3, 8, 2, 9,4,6]))

# 2nd time writing this algorithm on my own
def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # insertion sort
        # algorithm:
        # compare the elements
        # if smaller, then replace
        if (len(nums) == 0 or len(nums) == 1):
            return nums
        
        for i in range(0, len(nums) - 1): 
            j = i
            while j >= 0 and nums[j + 1] < nums[j]:
                temp = nums[j]
                nums[j] = nums[j + 1]
                nums[j + 1] = temp
                j -= 1
        return nums
        