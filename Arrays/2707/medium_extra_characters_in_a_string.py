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
            if word_start_index != -1:
                sentence = sentence.replace(word, "")

        return len(sentence)


execute = Solution()
execute.minExtraChar("leetscode", ["leet", "code", "leetcode"])