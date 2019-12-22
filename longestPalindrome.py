def spread(s, left, right):
    i, j = left, right
    while i >= 0 and j < len(s) and s[i] == s[j]:
        i -= 1
        j += 1
    return s[i+1:j]


def longestPalindrome(s):
    # if len(s) <= 1:
    #     return s
    # dp = [[False for i in range(len(s))] for j in range(len(s))]
    # dp[0][0] = True
    # result = s[0]
    # for right in range(1, len(s)):
    #     for left in range(right):
    #         if s[left] == s[right] and (right - left <= 2 or dp[left + 1][right - 1]):
    #             dp[left][right] = True
    #             if right - left + 1 > len(result):
    #                 result = s[left:right+1]
    # print(result)
    # return result

    if len(s) <= 1:
        return s
    result = s[0]
    for i in range(len(s)):
        s_odd = spread(s, i, i)
        s_even = spread(s, i, i+1)
        max_length_s = s_odd if len(s_odd) > len(s_even) else s_even
        if len(max_length_s) > len(result):
            result = max_length_s
    print(result)
    return result

if __name__ == "__main__":
    s = 'babaq'
    longestPalindrome(s)
