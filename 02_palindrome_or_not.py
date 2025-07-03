def palindrome(num):
    rev=0
    while num>0:
        rev = rev * 10 + num % 10
        num //= 10
    return rev
### Driver Code
if __name__ == "__main__":
    num = int(input("Enter a number: "))
    rev = palindrome(num)
    if rev == num:
        print(f"{num} is a palindrome")
    else:
        print(f"{num} is not a palindrome")