def reverse_num(x):
    rev=0
    sign=1
    posi=False
    if x < 0:
        x = -x
        sign = -1
        posi=True
    while x>0:
        rev = rev * 10 + x % 10
        x //= 10
    if posi:
        return rev * sign
    else:
        return rev
