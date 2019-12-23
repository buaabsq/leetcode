def numDecodings(s):
    # 首位是0不能解码
    if s[0] == '0':
        return 0
    # dp[i] = dp[i-1]+dp[i-2]，即认为在前i-1或i-2个字符后面接一个或两个，类似于上楼梯
    # 增加一项，使得第一项为0
    dp = [0 for i in range(len(s) + 1)]
    # 1指字符串第一项
    dp[0] = 1
    dp[1] = 1
    # 从字符串第二项开始
    for i in range(2, len(s) + 1):
        """
        判断0的情况，0必须与前一项组合，因此
            i-2大于2或等于0时，0将无法被解析，直接返回0
            若可以组合，则只能为前i-2个字符的组合方式
        若非0，则应当判断是否能进行组合：
            若前两项组合起来大于26，说明i-2这一项无法组合，应当等于前i-1个字符的组合方式
            若前一项为0，也说明不能与i-2进行组合
        在这里，i-1是字符串的序号，即当前在判断的一项
        """
        if s[i - 1] == '0':
            if int(s[i - 2]) > 2 or s[i-2] == '0':
                return 0
            else:
                dp[i] = dp[i-2]
        else:
            dp[i] = dp[i-1] if s[i-2] == '0' or int(s[i - 2: i]) > 26 else dp[i-1]+dp[i-2]

    print(dp)
    return dp[-1]

if __name__ == "__main__":
    s = '101'
    print(numDecodings(s))
