def median(a1,a2):
    if len(a1)>len(a2):
        a1,a2=a2,a1
    n1=len(a1)
    n2=len(a2)
    b1,e1=0,n1
    while b1<=e1:
        i1=(b1+e1)//2
        i2=(n1+n2+1)//2-i1

        min1=float('inf') if i1==n1 else a1[i1]
        max1=float('-inf') if i1==0 else a1[i1-1]

        min2=float('inf') if i2==n2 else a2[i2]
        max2=a2[i2-1] if i2>0 else float('-inf')

        if max1<=min2 and max2<=min1:
            if (n1+n2)%2==0:
                return (max(max1,max2)+min(min1,min2))/2
            else:
                return max(max1,max2)
        elif max1>min2:
            e1=i1-1
        else:
            b1=i1+1
# ### Example usage:
if __name__ == "__main__":
    a1 = [1, 3]
    a2 = [2]
    median_value = median(a1, a2)
    print("Median of the two sorted arrays is:", median_value)

    a1 = [1, 2]
    a2 = [3, 4]
    median_value = median(a1, a2)
    print("Median of the two sorted arrays is:", median_value)
    a1=[10,20,30,40,50]
    a2=[5,15,25,35,45,55,65,75,85]
    median_value = median(a1, a2)
    print("Median of the two sorted arrays is:", median_value)
