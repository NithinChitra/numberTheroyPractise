#In this technique we are iterating all elements but for every iteration we are 
# we are performing swapping once in an iteration

def selection_sort(arr):
    n = len(arr)
    for i in range(0,n-1):
        min = i
        for j in range(i,n):
            if arr[j] < arr[min]:
                min = j
        # Performing swapping outside inner loop
        arr[i], arr[min] = arr[min], arr[i]
    return arr
arr = [5,7,4,8,2]
print(selection_sort(arr))