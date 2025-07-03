def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
# ### Driver Code
if __name__ == "__main__":
    n = int(input("Enter a number: "))
    if n < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        result = fact(n)
        print(f"The factorial of {n} is: {result}")