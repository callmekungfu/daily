"""
    Name: Run-length Encoding
    Source: Daily Coding Problem 
    Description:
        This problem was asked by Amazon.
        Run-length encoding is a fast and simple method of encoding strings. 
        The basic idea is to represent repeated successive characters as a single count and character. 
        For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".
"""

def runEncode(word: str) -> str:
    encoded = ''
    prev = word[0]
    counter = 1
    for i in range(1, len(word)):
        if (word[i] == prev and i != len(word) - 1):
            counter += 1
        elif (word[i] == prev and i == len(word) - 1):
            counter += 1
            encoded += str(counter) + word[i - 1]
        else:
            encoded += str(counter) + word[i - 1]
            counter = 1
        prev = word[i]
    return encoded
userIn = input()
while userIn != 'exit':
    print(runEncode(userIn))
    userIn = input()