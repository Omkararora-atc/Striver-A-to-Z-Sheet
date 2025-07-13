def palindrome(s):
    s="".join(ch.lower() for ch in s if ch.isalnum())
    if s==" ":
        return True
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
# ### Example usage:
if __name__ == "__main__":
    s = "A jbucshf,vsyidjpjf,shcujbA"
    is_palindrome = palindrome(s)
    print("Is the string a palindrome?", is_palindrome)
    s="a plan, a canal, panama"
    is_palindrome = palindrome(s)
    print("Is the string a palindrome?", is_palindrome)