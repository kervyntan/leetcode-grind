# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

# https://leetcode.com/problems/guess-number-higher-or-lower

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n

        while left <= right:
            
            mid = (left + right) // 2

            if guess(mid) > 0:
                # if my guess is lower, I need to close the range towards the higher values
                left = mid + 1
            elif guess(mid) < 0:
                right = mid - 1
            
            else:
                return mid
        
        return -1