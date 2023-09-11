"""
Time Complexity: O(n + n) = O(2n) = O(n)

Concept: 
Convert the given integer into a binary representation, and then into a string
Loop through the string, check each index and see if its a 1
"""

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        str_binary_version = str(bin(n))
        i = 0
        no_of_ones = 0
        while (i < len(str_binary_version)):
            if (str_binary_version[i] == "1"):
                no_of_ones += 1
            i+=1
        return no_of_ones