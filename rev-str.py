"""
Reverse a String

Given a string, write a function that reverses the string.

Example:
"Hello world!" => "!dlrow olleH"

"""


def rev_str(s):

    for i in range(len(s)/2):
        save = s[i]
        s[i] = s[-(i+1)]
        s[-(i+1)] = save

    return s
