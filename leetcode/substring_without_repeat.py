# Naive
def lengthOfLongestSubstringNaive(s):
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

"""
public class Solution {
    public int lengthOfLongestSubstring(String s) {
        int n = s.length(), ans = 0;
        Map<Character, Integer> map = new HashMap<>(); // current index of character
        // try to extend the range [i, j]
        for (int j = 0, i = 0; j < n; j++) {
            if (map.containsKey(s.charAt(j))) {
                i = Math.max(map.get(s.charAt(j)), i);
            }
            ans = Math.max(ans, j - i + 1);
            map.put(s.charAt(j), j + 1);
        }
        return ans;
    }
}
"""

def lengthOfLongestSubstringDictionary(s):
    n = len(s)
    longest = 0
    map = {}
    i = 0
    for j in range(0, n):
        if (s[j] in map):
            i = max(map[s[j]], i)
        longest = max(longest, j - i + 1)
        map[s[j]] = j + 1
    return longest

while True:
    print(lengthOfLongestSubstringDictionary(input('N test: ')))