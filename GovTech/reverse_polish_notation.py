# aka postfix expression
# example input 
# using a stack to store values

def reverse_polish_notation(str):
    # stack to store values/digits in the string
    # limitation: if you put in a 2 digit number, it doesn't work
    # need to optimise for that
    stack = []

    operators = ['+', '-', '*', '/']
    for char in str:
        if char not in operators:
            stack.append(int(char))
        else:
            # pop the values off of the stack
            # say stack has [2,9] (max will only have 2 values)
            x = stack.pop(0)
            y = stack.pop()

            if char == '+':
                stack.append(x + y)
            elif char == '-':
                stack.append(x - y)
            elif char == '*':
                stack.append(x * y)
            else:
                stack.append(int(x / y))

    return stack[0]


print(reverse_polish_notation('83-2*'))
    