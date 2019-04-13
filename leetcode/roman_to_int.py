from enum import Enum

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
        s1 = Roman[s[i]].value
        if (i+1 < len(s)):
            s2 = Roman[s[i + 1]].value
            if (s1 >= s2):
                sum = sum + s1
                i = i + 1
            else:
                sum = sum + s2 - s1
                i + i + 2
        else:
            sum = sum + s1
            i = i + 1
    return sum


print(romanToInt('IV'))