def armstrong(n):
    orig=n
    digit=len(str(n))
    res=0
    while n>0:
        res += (n % 10) ** digit
        n //= 10
    return res==orig
### Driver Code
if __name__ == "__main__":
    n = int(input("Enter a number: "))
    if armstrong(n):
        print(f"{n} is an Armstrong number")
    else:
        print(f"{n} is not an Armstrong number")
