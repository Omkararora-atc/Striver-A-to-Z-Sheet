def square_root(n):
    if n==0 or n==1:
        return n
    left,right=1,n
    while left<=right:
        mid=(left+right)//2
        if mid*mid==n:
            return mid
        elif mid*mid<n:
            left=mid+1
        else:
            right=mid-1
    return right
# ### Example usage:
if __name__ == "__main__":
    n = 17
    result = square_root(n)
    print(f"Square root of {n} is: {result}")

    n = 20
    result = square_root(n)
    print(f"Square root of {n} is: {result}")

    n = 0
    result = square_root(n)
    print(f"Square root of {n} is: {result}")