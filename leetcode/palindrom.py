import math

def isPalindrom(x):
    if (x < 0 or (x % 10 == 0 and x != 0)):
        return False
    
    reverted = 0
    while (x > reverted):
        reverted = reverted * 10 + x % 10
        x = math.floor(x / 10)
    
    return x == reverted or x == math.floor(reverted/10)

print(isPalindrom(11))