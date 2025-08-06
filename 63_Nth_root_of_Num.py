def NthRoot( n, m):
    left, right = 0, m
    while left <= right:
        mid = (left + right) // 2
        new = helper(mid,n,m)
        if new == 0:
            return mid
        elif new == 2:
            right = mid - 1
        else:
            left = mid + 1
    return -1


def helper(mid, n, m):
    result = 1
    for _ in range(n):
        result *= mid
        if result > m:
            return 2
    if result == m:
        return 0
    return 1
# ### Example usage:
if __name__ == "__main__":
    n = 3  # The root to find
    m = 27  # The number to find the nth root of
    result = NthRoot(n, m)
    print(f"The {n}th root of {m} is: {result}")

    n = 4
    m = 16
    result = NthRoot(n, m)
    print(f"The {n}th root of {m} is: {result}")

    n = 5
    m = 32
    result = NthRoot(n, m)
    print(f"The {n}th root of {m} is: {result}")