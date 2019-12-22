def uniquePathsWithObstacles(obstacleGrid):
    n = len(obstacleGrid)
    m = len(obstacleGrid[0])
    if m == 0 or n == 0:
        return 0
    path_dp = [[0 for i in range(m)] for j in range(n)]
    # 先处理第一列和第一行
    for row in range(1, n):
        if obstacleGrid[row][0] == 1:
            path_dp[row][0] = 0
        else:
            path_dp[row][0] = path_dp[row-1][0]
    for col in range(1, m):
        if obstacleGrid[0][col] == 1:
            path_dp[0][col] = 0
        else:
            path_dp[0][col] = path_dp[0][col-1]

    # 从1,1开始处理
    for row in range(1,n):
        for col in range(1,m):
            if obstacleGrid[row][col] == 1:
                path_dp[row][col] = 0
            else:
                path_dp[row][col] = path_dp[row - 1][col] + path_dp[row][col-1]
    print(path_dp)
    return path_dp[-1][-1]


if __name__ == "__main__":
    grid = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    print(uniquePathsWithObstacles(grid))
