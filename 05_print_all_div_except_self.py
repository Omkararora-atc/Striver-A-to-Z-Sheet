def print_all_div(n):
    res=[]
    for i in range(1,n):
        if n%i==0:
            res.append(i)
    return res
# ### Driver Code
if __name__ == "__main__":
    n = int(input("Enter a number: "))
    if n <= 0:
        print("Please enter a positive integer.")
    else:
        divisors = print_all_div(n)
        if divisors:
            print(f"The divisors of {n} are: {divisors}")
        else:
            print(f"{n} has no divisors other than itself.")
