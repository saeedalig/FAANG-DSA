
# Using Bubble Sort Algorithm sort the given array 
## arr = [90, 10,29,15,17,5]

def bubbleSort(arr):
    n = len(arr)
    # Traverse through all elements
    for i in range(n):
        # Last i element is already in place (n-1)
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                # Swap the element
                arr[j], arr[j+1] = arr[j+1] , arr[j]
    return arr


# Driver code
arr = [90, 10,29,15,17,5]
result = bubbleSort(arr)
print(result)





