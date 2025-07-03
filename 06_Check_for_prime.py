def check_prime(num):
    if num==0 or num==1:
        return False
    if num==2 or num==3:
        return True
    if num % 2 == 0 or num%3==0:
        return False
    i = 5
    while i*i<=num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True
# ### Driver Code
if __name__ == "__main__":
    num = int(input("Enter a number: "))
    if check_prime(num):
        print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")