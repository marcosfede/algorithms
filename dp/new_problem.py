# New Dynamic Programming Problem: "Fibonacci Sequence"
# Problem Statement:
# Calculate the n-th Fibonacci number using dynamic programming.
# The Fibonacci sequence is defined as follows:
# F(0) = 0, F(1) = 1
# F(n) = F(n-1) + F(n-2) for n > 1
#
# Implement a function `fibonacci(n)` that returns the n-th Fibonacci number.
#
# Example:
# fibonacci(0) -> 0
# fibonacci(1) -> 1
# fibonacci(5) -> 5
# fibonacci(10) -> 55
#
# Constraints:
# 0 <= n <= 100

def fibonacci(n):
    if n <= 1:
        return n
    fib = [0] * (n + 1)
    fib[1] = 1
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib[n]

# Test the function
if __name__ == "__main__":
    print(fibonacci(0))  # Should print 0
    print(fibonacci(1))  # Should print 1
    print(fibonacci(5))  # Should print 5
    print(fibonacci(10))  # Should print 55
