"""
The following code adds two numbers without using the '+' operator.
The code uses bitwise operations to add two numbers.

Input: 2 3
Output: 5
"""
try:
    raw_input          # Python 2
except NameError:
    raw_input = input  # Python 3


def addWithoutOperator(x, y):
    while y != 0:
        carry = x & y
        x = x ^ y
        y = carry << 1
    print(x)


def main():
    x, y = map(int, raw_input().split())
    addWithoutOperator(x, y)


if __name__ == '__main__':
    main()
