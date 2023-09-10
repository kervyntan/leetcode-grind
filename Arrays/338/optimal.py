# https://leetcode.com/problems/counting-bits/solutions/656849/python-simple-solution-with-clear-explanation/?envType=daily-question&envId=2023-09-01

"""
Time Complexity : O(n)
Space Complexity : O(n)
"""

"""
Explanation:
- All whole numbers can be represented by 2N (even) or 2N + 1 (odd)
- For a given binary number, multiplying by 2 is the same as adding a zero at the end (similar to adding a zero at the end when multiplying by 10 in base 10)

Since multiplying by 2 adds a zero, any number and it's double will have the same number of 1s
Similarly, doubling a number and adding 1 will increase the count exactly by 1

Thus we can see that any number will have the same bit count as half that number, with an extra one if it's an odd number.
"""

class Solution(object):
    def countBits(self, num):
        counter = [0]
        for i in range(1, num+1):
            counter.append(counter[i >> 1] + i % 2)
        return counter
        """
        for i in range(1, num + 1):
            print(i)
            # Does a shift right logical
            print(i >> 1)
        """
    

execute = Solution()
print(execute.countBits(5))