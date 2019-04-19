# Naive (Will not work since exceeds time limit)
def isPalindrome(s):
    return list(s) == list(reversed(s))
    s = s.casefold()

def longestPalindromeNaive(s):
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

# Better Version (From Solution)
def expandAroundCenter(s, left, right):
    L = left
    R = right
    while L >= 0 and R < len(s) and s[L] == s[R]:
        L -= 1
        R += 1
    return R - L - 1

def longestPalindrome(s):
    if len(s) < 1:
        return s
    start = 0
    end = 0
    for i in range(0, len(s)):
        len1 = expandAroundCenter(s, i, i)
        len2 = expandAroundCenter(s, i, i + 1)
        length = max(len1, len2)
        if (length > end - start):
            start = i - (length - 1) // 2
            end = i + length // 2
    return s[start:end+1]


hello = input()
while hello != 'bye':
    print(longestPalindrome(hello))
    hello = input()
