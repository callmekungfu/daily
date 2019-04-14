# naive solution
# runtime: 40ms - 72.98 Percentile
# memeory usage: 13.4mb - 5.1 Percentile
def longestCommonPrefix(self, strs):
    if (len(strs) == 0):
        return ""
    shortest = len(min(strs, key=len))
    iterator = 0
    prefix = ""
    i = 0
    is_prefix = True
    while is_prefix and i < shortest:
        j = 0
        working = strs[j][i]
        while is_prefix and j < len(strs):
            is_prefix = strs[j][i] == working
            j = j + 1
        if (is_prefix):
            prefix += working
        i = i + 1
    return prefix
                