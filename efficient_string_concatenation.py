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

