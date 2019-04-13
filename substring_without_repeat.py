# Naive
def lengthOfLongestSubstring(s):
    longest = 0
    if (len(s) == 1):
        return 1
    for i in range(0, len(s) - 1):
        j = i
        length = 1
        sub = s[i]
        while (j + 1) < len(s) and not s[j+1] in sub:
            sub += s[j + 1]
            j += 1
            length += 1
        if (length > longest):
            longest = length
    return(longest)
while True:
    print(lengthOfLongestSubstring(input('N test: ')))