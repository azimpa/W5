def merge(l, r):
    result = []  # This will hold the merged sorted elements
    i, j = 0, 0  # Pointers to keep track of current indices in l and r
    
    while i < len(l) and j < len(r): # Loop through both arrays until one is exhausted
        if l[i] < r[j]: # Compare elements at the current indices of l and r
            result.append(l[i])  # Add the smaller element to the result
            i += 1  # Move to the next element in l
        else:
            result.append(r[j])  # Add the smaller element to the result
            j += 1  # Move to the next element in r
    # At this point, one of the arrays is exhausted # Append any remaining elements from l or r to the result
    result.extend(l[i:])  # Add remaining elements of l (if any)
    result.extend(r[j:])  # Add remaining elements of r (if any)
    return result  # Return the merged sorted array

def merge_sort(arr):  # Function to perform merge sort on an array
    if len(arr) <= 1: # Base case: if the array has 0 or 1 elements, it is already sorted
        return arr
    
    mid = len(arr) // 2   # Find the midpoint to divide the array into two halves
    l = merge_sort(arr[:mid])      # Recursively sort the left half
    r = merge_sort(arr[mid:])      # Recursively sort the right half
    
    return merge(l, r)      # Merge the sorted halves

array = [9, 5, 1, 3, 8, 4, 2, 7, 6]
sorted_array = merge_sort(array)
print(sorted_array)
