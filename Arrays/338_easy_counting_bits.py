"""
Time complexity: O(n^2)
Runtime: 204ms
Memory: 15.24MB
"""

class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """ 

        """
        Given an integer 5, return an array of length 6 such that for each i <= 5,  
        ans[i] = number of 1's in the binary representation of i
        """

        """
        Binary representation of a number -> weights of 2
        """

        ans = []
        if n == 0:
            ans.append(0)
            return ans
        else:
            i = 0
            while i <= n:
                self.binaryCount(ans, i)
                i+=1
            
            return ans
                
    def binaryCount(self, list, index):
        # if index is 1, then it'll be 0001 (4-bit)
        # if index is 2, then it'll be 0010 (4-bit)
        # if index is 3, then it'll be 0011 (4-bit)
        # if index is 4, then it'll be 0100 (4-bit)

        # how to convert decimal to binary (mathematical way)
        # repeated division by 2
        # remainder from division is representation in binary
        # MSB begins from the last remainder

        val = index
        remainder = 0
        no_of_ones = 0

        while val != 0:
            remainder = val % 2
            if int(remainder) == 1:
                no_of_ones += 1
            val = val / 2
        
        list.append(no_of_ones)

