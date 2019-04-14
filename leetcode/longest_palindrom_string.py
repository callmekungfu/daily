# Naive (Will not work since exceeds time limit)
def isPalindrome(s):
    return list(s) == list(reversed(s))
    s = s.casefold()

def longestPalindrome(s):
    if len(s) <= 1:
        return s
    longest = ""

    for i in range(0, len(s) - 1):
        count = ""
        j = i + 1
        while j < len(s):
            if isPalindrome(s[i:j+1]):
                count = s[i:j+1]
            j = j + 1
        # print(longest, count)
        if (len(count) > len(longest)):
            longest = count
    return longest

hello = input()
while hello != 'bye':
    print(longestPalindrome(hello))
    hello = input()
