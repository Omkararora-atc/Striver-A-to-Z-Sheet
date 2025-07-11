def three_sum(arr):
    n=len(arr)
    arr.sort()
    res=[]
    for i in range(0,n-2):
        if i>0 and arr[i]==arr[i-1]:
            continue
        l=i+1
        r=n-1
        while l<r:
            total=arr[i]+arr[l]+arr[r]
            if total==0:
                res.append([arr[i],arr[l],arr[r]])
                l+=1
                r-=1
                while l<r and arr[l]==arr[l-1]:
                    l+=1
                while l<r and arr[r]==arr[r+1]:
                    r-=1
            elif total<0:
                l+=1
            else:
                r-=1
    return res
# ### Example usage:
if __name__ == "__main__":
    arr = [-1, 0, 1, 2, -1, -4]
    triplets = three_sum(arr)
    print("Triplets that sum to zero:", triplets)