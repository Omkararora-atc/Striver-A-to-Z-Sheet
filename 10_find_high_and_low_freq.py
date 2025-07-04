def find(arr):
    count={}
    for num in arr:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    high_freq = max(count.values())
    low_freq = min(count.values())
    return high_freq, low_freq
## Driver Code
if __name__ == "__main__":
    arr = [1, 2, 2, 3, 3, 3]
    find(arr)
    print("The highest frequency is:", find(arr)[0])
    print("The lowest frequency is:", find(arr)[1])
    