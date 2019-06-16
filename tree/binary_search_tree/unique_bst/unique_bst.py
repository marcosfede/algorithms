def num_trees(n):
    """
    :type n: int
    :rtype: int
    """
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n + 1):
        for j in range(i + 1):
            dp[i] += dp[i - j] * dp[j - 1]
    return dp[-1]
