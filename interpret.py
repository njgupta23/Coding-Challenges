# interpret


# Write a simple interpreter which understands "+", "-", and "*" operations. 
# Apply the operations in order using command/arg pairs starting with the initial 
# value of `value`. If you encounter an unknown command, return -1.


# interpret(1, ["+"], [1]) → 2
# interpret(4, ["-"], [2]) → 2
# interpret(1, ["+", "*"], [1, 3]) → 6


def interpret(val, com, arg):
    result = val

    for i in range(len(com)):
        if com[i] == '+':
            result += arg[i]
        elif com[i] == '-':
            result -= arg[i]
        elif com[i] == '*':
            result *= arg[i]
        else:
            return -1

    return result
