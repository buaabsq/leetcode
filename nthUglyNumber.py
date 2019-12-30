def nthUglyNumber(n):
    """
    任何一个合数都可以被质因数分解，因此若只含有2,3,5，应该可以在反复除的过程中得到商1
    以上为对某个数的判断，对于第n个数，可以从反向思考
    任何一个丑数均是由之前的丑数乘2/3/5得到的（否则会引入其他的质因数），
    因此最简单的方法就是对之前的丑数依次乘，直到大于第n-1个为止
    实际上并不需要这么多的次数，使用乘2,3,5得到n-1的下标a,b,c即可
    但乘以2,3,5时可能使顺序打乱，因此需要保持顺序，按a<b<c，判断5a,3b,2c的关系（min)
    """
    if n == 0 or n == 1:
        return n
    else:
        a, b,c = 0, 0, 0
        dp_ugly = [0 for i in range(n)]
        dp_ugly[0] = 1
        for i in range(1, n):
            dp_ugly[i] = min(dp_ugly[a] * 5, dp_ugly[b]
                                * 3, dp_ugly[c] * 2)
            # 更新3指针的位置
            if dp_ugly[a] * 5 <= dp_ugly[i]:
                a += 1
            if dp_ugly[b] * 3 <= dp_ugly[i]:
                b += 1
            if dp_ugly[c] * 2 <= dp_ugly[i]:
                c += 1
        return dp_ugly[-1]


if __name__ == "__main__":
    print(nthUglyNumber(10))
