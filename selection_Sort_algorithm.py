### Using Selection sort Algorithm, sort the given array in ascending order
# arr = [70, 56, 23, 19, 25, 37, 48]



# Method Definition

def selectionSort(arr):
    n = len(arr)

    # Traverse the Elements
    for i in range(n):
        
        # Find min_value
        min_idx = i

        # Traverse again to find next min_value in unsorted array
        for j in range(i+1, n):

            # Compare the elements
            if arr[j] < arr[min_idx]:

                # Update the min_value 
                min_idx = j
        ## Swap the element 
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

## Driver code
arr = [70, 56, 23, 19, 25, 37, 48]
result = selectionSort(arr)
print("Sorted array after applying selection sort:", result)


# Time complexity: O(n^2)