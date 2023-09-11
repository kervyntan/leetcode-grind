"""
Time Complexity: 
For loop -> O(n)
sentence.find(word) -> O(n) to find the word
sentence.replace -> O(n)
Each iteration of loop, you're doing O(n + n), which gives rise to O(2n)

Total: O(n * 2n) = O( 2 n^2) = O(n ^ 2) (not v good)
"""

class Solution(object):
    def minExtraChar(self, s, dictionary):
        """
        :type s: str
        :type dictionary: List[str]
        :rtype: int
        """
        
        """
        Using the dictionary, loop through it, see if the word in the dictionary exists in the string
        Using find
        """ 
        sentence = s
        for word in dictionary:
            word_start_index = sentence.find(word)
            # the word exists in the sentence
            if word_start_index != -1:
                sentence = sentence.replace(word, "")

        return len(sentence)


execute = Solution()
execute.minExtraChar("leetscode", ["leet", "code", "leetcode"])