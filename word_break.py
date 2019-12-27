def wordBreak(s, wordDict):
    if len(s) == 1:
        return s in wordDict
    else:
        """
        dp_is_word[i]表示到s[:i]位置的字符串可以被分割
        对于字符串s[:i]来说，给定一个分割位置j,若s(0,j),s(j+1,i)都能在字典中，则s[:i]能够被分割
        （注：第一次的想法忽略了aaaa|aaa这种情况，分割可能并不止一种，应当寻找不同）
        对于长度为0的字符串，空集必然属于任何集合
        """
        dp_is_word = [False for i in range(len(s) + 1)]
        dp_is_word[0] = True
        # 从第一个位置开始找
        for i in range(1, len(s) + 1):
            # 分割到i之前的所有字符串
            for j in range(i):
                if dp_is_word[j] and s[j: i] in wordDict:
                    dp_is_word[i] = True
                    break
                
        print(dp_is_word)
        return dp_is_word[-1]


if __name__ == "__main__":
    s = "aaaaaaa"
    wordDict = ["aaaa", "aaa"]
    print(wordBreak(s, wordDict))
