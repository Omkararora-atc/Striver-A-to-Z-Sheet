def four_sum(arr):
    arr.sort()
    n=len(arr)
    res=[]
    for i in range(0,n-3):
        if i>0 and arr[i]==arr[i-1]:
            continue
        for j in range(i+1,n-2):
            if j>i+1 and arr[j]==arr[j-1]:
                continue
            l=j+1
            r=n-1
            while l<r:
                total=arr[l]+arr[r]+arr[i]+arr[j]
                if total==0:
                    res.append([arr[i],arr[j],arr[l],arr[r]])
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
    arr = [1, 0, -1, 0, -2, 2]
    quadruplets = four_sum(arr)
    print("Quadruplets that sum to zero:", quadruplets)