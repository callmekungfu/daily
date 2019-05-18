"""
    Name: Implement atoi()
    Source: LeetCode - 8
    Link: https://leetcode.com/problems/string-to-integer-atoi
    Description: Implement atoi which converts a string to an integer.
"""

def myAtoi(word: str) -> int:
    stripped = word.strip().strip('+')
    numerated = ""
    still_number = True
    counter = 0
    if (len(stripped) == 0):
        return 0
    if (len(stripped) > 1 and stripped[0] == '-' and is_number(stripped[1])):
        numerated = '-' + stripped[1]
        counter = 2

    while still_number and counter < len(stripped):
        still_number = is_number(numerated + stripped[counter])
        if (still_number):
            numerated += stripped[counter]
            counter += 1
    if (len(numerated) > 0 and int(numerated) < 2147483647 and int(numerated) > -2147483648):
        return int(numerated)
    elif (len(numerated) > 0 and int(numerated) > 2147483647):
        return 2147483647
    elif (len(numerated) and int(numerated) < -2147483648):
        return -2147483648
    return 0

def is_number(n):
    is_number = True
    try:
        num = int(n)
        # check for "nan" floats
        is_number = num == num   # or use `math.isnan(num)`
    except ValueError:
        is_number = False
    return is_number

print(myAtoi('2+2'))