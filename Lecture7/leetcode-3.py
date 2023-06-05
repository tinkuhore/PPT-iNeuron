def lengthOfLongestSubstring(s):
    n = len(s)
    ans = 0
    map = {}  # current index of character
    # try to extend the range [i, j]
    i = 0
    for j in range(n):
        if s[j] in map:
            i = max(map[s[j]], i)
        ans = max(ans, j - i + 1)
        map[s[j]] = j + 1
    return ans

lengthOfLongestSubstring("abcabcd")