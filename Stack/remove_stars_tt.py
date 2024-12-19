"""
Interview question that looks like it uses string manipulation
But stack is much more elegant
"""

"""
Problem Statement:
Given a string, remove all occurrences of it's stars and left-most character.

Example 1:
Input: "leet**cod*e"
Output "lecoe"

From left to right, after 't', we meet a '*'. Thus we remove 't' from the string
Subsequently, we meet another '*' right after, thus we also remove 'e' from the string

Example 2:
Input: "erase*****"
Output: ""
"""


# Time complexity: O(n), where n = len(s). 
# Space complexity: O(n), where n = len(s).
# Pop (from end) and append have Amortized O(1)
def remove_stars(s):
    # Optimal solution
    # Using the List as a Stack, rather than just naively looping and checking all chars' neighbours
    res = []
    for char in s:
        if char == "*":
            res.pop()
            continue

        res.append(char)

    return "".join(res)


print(remove_stars("leet**cod*e"))  # lecoe
print(remove_stars("erase*****"))  # ""
