#   This is solutions of tasks from codewars.com
#   by Georgi Kazakov
#   https://www.codewars.com/users/KazakovGeorge


# DESCRIPTION (8 kyu):
# Convert number to reversed array of digits
# Given a random non-negative number, you have to return the digits of this number within an array in reverse order.
#
# Example(Input => Output):
# 35231 => [1,3,2,5,3]
# 0 => [0]

def digitize(n):
    arr = []
    nStr = str(n)

    for i in range(len(nStr) - 1, -1, -1):
        arr.append(int(nStr[i]))

    return arr


# DESCRIPTION (7 kyu):
# Implement a function that adds two numbers together and returns their sum in binary.
# The conversion can be done before, or after the addition.
# The binary number returned should be a string.
#
# Examples:(Input1, Input2 --> Output (explanation)))
# 1, 1 --> "10" (1 + 1 = 2 in decimal or 10 in binary)
# 5, 9 --> "1110" (5 + 9 = 14 in decimal or 1110 in binary)

def add_binary(a, b):
    sum = a + b
    result = []

    while (sum >= 1):
        if ((sum % 2) == 1):
            result.append('1')
        else:
            result.append('0')
        sum = sum // 2

    return ''.join(result[::-1])


# DESCRIPTION (6 kyu):
# In this kata you are required to, given a string, replace every letter with its position in the alphabet.
# If anything in the text isn't a letter, ignore it and don't return it.
# "a" = 1, "b" = 2, etc.
#
# Example
# alphabet_position("The sunset sets at twelve o' clock.")
# Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" ( as a string )

def alphabet_position(text):
    text = text.lower()
    result = ''
    letters = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4,
        'e': 5,
        'f': 6,
        'g': 7,
        'h': 8,
        'i': 9,
        'j': 10,
        'k': 11,
        'l': 12,
        'm': 13,
        'n': 14,
        'o': 15,
        'p': 16,
        'q': 17,
        'r': 18,
        's': 19,
        't': 20,
        'u': 21,
        'v': 22,
        'w': 23,
        'x': 24,
        'y': 25,
        'z': 26,
    }

    for ltr in text:
        if ltr in letters:
            result = result + str(letters[ltr]) + ' '

    return result.rstrip()


# DESCRIPTION (6 kyu):
# Write a function that accepts an array of 10 integers (between 0 and 9),
# that returns a string of those numbers in the form of a phone number.
#
# Example
# create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
# The returned format must be correct in order to complete this challenge.
#
# Don't forget the space after the closing parentheses!

def create_phone_number(n):
    return ("(%s%s%s) %s%s%s-%s%s%s%s" % (n[0],n[1],n[2],n[3],n[4],n[5],n[6],n[7],n[8],n[9]))


# DESCRIPTION ( kyu):
# Create a method each_cons that accepts a list and a number n,
# and returns cascading subsets of the list of size n, like so:

# each_cons([1,2,3,4], 2)
#   #=> [[1,2], [2,3], [3,4]]
# each_cons([1,2,3,4], 3)
#   #=> [[1,2,3],[2,3,4]]
#
# As you can see, the lists are cascading; ie, they overlap, but never out of order.

def each_cons(lst, n):
    # your solution here
    print(lst, n)
    result = []
    tmp = []
    i = 0

    if ((lst != []) and (n <= len(lst))):
        while (i != len(lst) - n + 1):
            for j in range(i, i + n, 1):
                tmp.append(lst[j])
            result.append(tmp)
            tmp = []

            i += 1
    return result


# DESCRIPTION (8 kyu):
# This code does not execute properly. Try to figure out why.

def multiply(a, b):
    return a * b


