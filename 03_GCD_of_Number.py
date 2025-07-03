def gcd(a,b):
    if b==0:
        return a
    return gcd(b, a % b)
### Driver Code
if __name__ == "__main__":
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    result = gcd(a, b)
    print(f"The GCD of {a} and {b} is {result}")
