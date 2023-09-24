# Given [A, B, C], create a function that returns "A says hi to B and C. B says hi to A and C. C says hi to A and B"

# loop through the list 
# pop the top of the list, and then it'll say hi to the other 2

array = ['A', 'B', 'C']
result_strings = []

def say_hi(greeter, recipient_one, recipient_two):
    result_strings.append(greeter)
    result_strings.append(" says hi to ")
    result_strings.append(recipient_one)
    result_strings.append(" and ")
    result_strings.append(recipient_two)
    result_strings.append(". ")

str = say_hi(array[0], array[1], array[2])
str = say_hi(array[1], array[0], array[2])
str = say_hi(array[2], array[0], array[1])

print("".join(result_strings))

# Overall Time Complexity: O(n) for the join
# Unlike the concatenation operators,
# .join() doesn’t create new intermediate strings in each iteration.

# loop through string
# use python.count to check how many times this char exists in the string
# compare both the count of the same char
# in both of the strings
# if they are more than equals to 
def appear_n(str1, str2, n):
    res = []
    counter_first = 0
    counter_second = 0

    for char in str1:
        # look at the first character
        counter_first = str1.count(char)
        counter_second = str2.count(char)

        if (counter_first >= n and counter_second >= n):
            if (char not in res):
                res.append(char)

    return res

print(appear_n("aaabbcde", "aababde", 1))