def stock(arr):
    min_price = float('inf')
    max_profit = 0
    for price in arr:
        if price< min_price:
            min_price = price
        profit= price - min_price
        if profit>max_profit:
            max_profit = profit
    return max_profit
# ### Example usage:
if __name__ == "__main__":
    arr = [7, 1, 5, 3, 6, 4]
    max_profit = stock(arr)
    print("Maximum profit from stock buy and sell is:", max_profit)