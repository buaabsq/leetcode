def minPathSum(grid):
    m = len(grid[0])
    n = len(grid)
    if n == 0 or m == 0:
        return 0
    sum_dp = [[0 for i in range(m)] for j in range(n)]
    sum_dp[0][0] = grid[0][0]
    # 先处理第一列和第一行
    for row in range(1, n):
        sum_dp[row][0] = sum_dp[row-1][0] + grid[row][0]

    for col in range(1, m):
        sum_dp[0][col] = sum_dp[0][col-1] + grid[0][col]

    for row in range(1, n):
        for col in range(1, m):
            sum_dp[row][col] = min(sum_dp[row-1][col], sum_dp[row][col-1]) + grid[row][col]

    return sum_dp[-1][-1]

if __name__ == "__main__":
    grid = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    print(minPathSum(grid))
