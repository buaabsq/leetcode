def maximalSquare(matrix):
    if len(matrix) == 0:
        return 0
    elif len(matrix) == 1:
        return int(max(matrix[0]))
    else:
        """
        dp_matrix[i][j]表示以(i,j)为右下角的正方形的边数，为1时，画图可知：
        左侧[i][j-1]，上侧[i-1][j]的最小值决定了以(i,j)为右下角的正方形的最长边数
        即二者中的最小值+1
        但二者相等时，不能简单的加一，[i-1][j-1]这个对角线上的也有决定权，画图可知，
        该数若比上侧和左侧小1，则左上角有一个点是0，因此应当选择[i-1][j-1]的值加一，或等于二个边
        """
        m = len(matrix)
        n = len(matrix[0])
        dp_matrix = [[0 for j in range(n)] for i in range(m)]
        # 填写第一行&第一列
        for i in range(m):
            dp_matrix[i][0] = int(matrix[i][0])
        for j in range(n):
            dp_matrix[0][j] = int(matrix[0][j])

        # 从(1,1)找起
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == '0':
                    dp_matrix[i][j] = 0
                else:
                    dp_matrix[i][j] = min(
                        dp_matrix[i-1][j], dp_matrix[i][j-1], dp_matrix[i-1][j-1]) + 1
        
        # 寻找最大值
        max_square = 0
        for i in range(m):
            max_square = max(dp_matrix[i]) if max_square < max(dp_matrix[i]) else max_square

        return max_square**2


if __name__ == "__main__":
    matrix = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"]
    ]

    print(maximalSquare(matrix))
