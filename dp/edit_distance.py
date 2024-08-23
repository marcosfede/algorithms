def edit_distance(str1, str2):
    """
    Calculate the minimum number of operations required to convert str1 into str2.
    Operations allowed: insertion, deletion, substitution.
    
    :param str1: First string
    :param str2: Second string
    :return: Minimum number of operations required
    """
    m, n = len(str1), len(str2)
    
    # Create a matrix to store the subproblem solutions
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Initialize the first row and column
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    # Fill the dp matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j],      # deletion
                                   dp[i][j-1],      # insertion
                                   dp[i-1][j-1])    # substitution
    
    return dp[m][n]

# Example usage
if __name__ == "__main__":
    str1 = "kitten"
    str2 = "sitting"
    print(f"Edit distance between '{str1}' and '{str2}': {edit_distance(str1, str2)}")
