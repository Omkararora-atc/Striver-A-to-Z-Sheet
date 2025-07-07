def missing(arr):
    n=len(arr)
    sum_n=n*(n+1)//2
    return sum_n-sum(arr)
### Example usage:
if __name__ == "__main__":
    arr = [0, 1, 2, 3, 5]
    missing_number = missing(arr)
    print("The missing number is:", missing_number)