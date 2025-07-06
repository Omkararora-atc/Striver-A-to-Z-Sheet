def sec(arr):
     if len(arr)<2:
         return None
     first = second = float('-inf')
     for i in range(len(arr)):
         if arr[i]>first:
                second = first
                first = arr[i]
         elif arr[i]>second and arr[i]!=first:
                second = arr[i]
     return second if second != float('-inf') else None
## # ### Driver Code
if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11, -5, 100, 0,1000]
    second_largest = sec(arr)
    print("Second largest element in the array:", second_largest)