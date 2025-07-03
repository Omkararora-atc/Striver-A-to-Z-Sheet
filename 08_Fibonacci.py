def fibonacci(n):
    if n==0 or n==1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
# ### Driver Code
if __name__ == "__main__":
    n = int(input("Enter a number: "))
    if n < 0:
        print("Fibonacci is not defined for negative numbers.")
    else:
        result = fibonacci(n)
        print(f"The {n}th Fibonacci number is: {result}")