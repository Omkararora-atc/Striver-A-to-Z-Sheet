def majority(arr):
    count={}
    n=len(arr)
    for i in arr:
        if i in count:
            count[i]+=1
        else:
            count[i]=1
        if count[i]>n//2:
            return i
    return None
# ### Example usage:
if __name__ == "__main__":
    arr = [3, 2, 3]
    majority_element = majority(arr)
    if majority_element is not None:
        print("The majority element is:", majority_element)
    else:
        print("No majority element found.")