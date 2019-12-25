def minimumTotal(triangle):
    if len(triangle) == 0:
        return 0
    elif len(triangle) == 1:
        return triangle[0][0]
    else:
        dp_min = [0 for i in range(sum(range(1, len(triangle) + 1)))]
        dp_min[0] = triangle[0][0]
        '''
        对于每行而言，每个数的最小值等于其正上方和两侧数字的最短路
        到点i,j为止的最短路就是min[(i-1,j),(i,j),(i-1,j+1)]+(i,j)，需要考虑一些边界情况
        设last_sum为本行数的起始点
        则(i,j)=last_sum+j,(i-1,j)为last_sum-i+j
        注：此题居然右侧不算相邻，另外直接原地tp修改即可
        '''
        last_sum = 0
        for i in range(1, len(triangle)):
            last_sum += i
            # 行数序号+1的数字
            for j in range(i+1):
                '''
                第一个位置，没有左侧项，只有正上方+右侧，
                右侧在第二行时无效
                与上一行最后一个平齐的位置，只有上侧和左侧
                左侧在第二行无效
                '''
                if j == 0:
                    dp_min[last_sum + j] = dp_min[last_sum-i+j] + \
                        triangle[i][j]

                elif j == i-1:
                    dp_min[last_sum + j] = min(dp_min[last_sum-i+j],
                                               dp_min[last_sum-i+j-1]) + triangle[i][j]
                elif j == i:
                    dp_min[last_sum + j] = dp_min[last_sum-i+j-1] + \
                        triangle[i][j]
                else:
                    dp_min[last_sum + j] = min(dp_min[last_sum-i+j],
                                               dp_min[last_sum-i+j-1]) + triangle[i][j]
        print(dp_min)
        return min(dp_min[last_sum:])


if __name__ == "__main__":
    triangle = [
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ]
    print(minimumTotal(triangle))
