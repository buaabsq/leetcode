def uniquePaths(m, n):
    path_dp = [[0 for i in range(m)] for j in range(n)]
    for row in range(n):
        for col in range(m):
            if row == 0 or col == 0:
                path_dp[row][col] = 1
            else:
                path_dp[row][col] = path_dp[row - 1][col] + path_dp[row][col-1]
    
    return path_dp[n-1][m-1]


if __name__ == "__main__":
    print(uniquePaths(7, 3))