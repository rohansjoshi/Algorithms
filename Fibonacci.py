
"""
Textbook example of recursion. The recursion tree is unbalanced. The rightmost path
has n/2 levels and the leftmost has n levels. So the first n/2 levels of the tree are full,
but the full n levels are not. So there are between O((sqrt 2)^n) = O(1.4^n) and O(2^n)
levels, which is the time complexity of the algorithm. 
"""

def recursive_fib(n):
    if n == 0 or n == 1:
        return n
    return recursive_fib(n-1)+recursive_fib(n-1)

# Finally, some linear time algorithms

# This one uses O(n) storage
def dp_fib(n):
    dp = [0]*(n+1)
    dp[1] = 1
    if n == 0 or n == 1:
        return dp[n]
    def helper(n):
        if n > 1 and dp[n] == 0:
            helper(n-1)
            helper(n-2)
            dp[n] = dp[n-1]+dp[n-2]
    helper(n)
    return dp[n]

def iter_fib(n):
    if n == 0 or n == 1:
        return n
    a, b = 0, 1
    for _ in range(n-1):
        a, b = b, a+b
    return b


# This one proves you can have a O(n) solution that is recursive

def addseq(n, a, b):
    if n == 0:
        return a
    elif n == 1:
        return b
    return addseq(n-1, b, a+b)

fib = lambda n: addseq(n, 0, 1)
