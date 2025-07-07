def sort_colors(arr):
    l,m,h=0,0,len(arr)-1
    while m<=h:
        if arr[m]==0:
            arr[l],arr[m]=arr[m],arr[l]
            l+=1
            m+=1
        elif arr[m]==1:
            m+=1
        else:
            arr[m],arr[h]=arr[h],arr[m]
            h-=1
    return arr
# ### Example usage:
if __name__ == "__main__":
    arr = [2, 0, 2, 1, 1, 0]
    sorted_arr = sort_colors(arr)
    print("Array after sorting colors:", sorted_arr)