def myPow(self, x: float, n: int) -> float:
    """
    Implement pow(x, n), which calculates x raised to the power n (i.e. xn).
    Time Complexity: O(log N)
    Space: O(1)
    """
    result = 1
    if n < 0:
        x = 1 / x
        n = -n
    while n:
        if n & 1:
            result *= x
        x *= x
        n >>= 1
    return result


"""
FAST POWER ALGORITHM
Example: 3^9
x = 3, n = 9

1.) Convert n to binary

9 = b1001 (8,4,2,1 are the powers of each bit)

2.) From right to left of the binary number, use those with 1s

3^9 = 3^1 * 3^8
"""