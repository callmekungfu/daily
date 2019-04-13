from enum import Enum

def value(s):
    if s == 'I':
        return 1
    if s == 'V':
        return 5
    if s == 'X':
        return 10
    if s == 'L':
        return 50
    if s == 'C':
        return 100
    if s == 'D':
        return 500
    if s == 'M':
        return 1000
    return -1

class Roman(Enum):
    I = 1
    IV = 4
    V = 5
    IX = 9
    X = 10
    XL = 40
    L = 50
    XC = 90
    C = 100
    CD = 400
    D = 500
    CM = 900
    M = 1000


def romanToInt(s):
    sum = 0
    i = 0
    while i < len(s):
        s1 = value(s[i])
        if (i+1 < len(s)):
            s2 = value(s[i+1])
            if (s1 >= s2):
                sum = sum + s1
                i = i + 1
            else:
                sum = sum + s2 - s1
                i = i + 2
        else:
            sum = sum + s1
            i = i + 1
    return sum


print(romanToInt('IV'))