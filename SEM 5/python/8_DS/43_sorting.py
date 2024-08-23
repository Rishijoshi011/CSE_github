
def swapping(num, num2):
    temp = num 
    num = num2
    num2 = temp
    
    return num, num2

# ! Selection sort

def selection_sort(arr):
    arr_len = len(arr)
    
    for i in range(arr_len):
        min_index = i
        for j in range(i + 1, arr_len):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = swapping(arr[i], arr[min_index])
    
    return arr

# ! Merge sort
def merge(arr, low, mid, high):
    left_half = arr[low:mid + 1]
    right_half = arr[mid + 1:high + 1]

    i = j = 0  
    k = low    
    
    while i < len(left_half) and j < len(right_half):
        if left_half[i] <= right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1
    
    while i < len(left_half):
        arr[k] = left_half[i]
        i += 1
        k += 1
    
    while j < len(right_half):
        arr[k] = right_half[j]
        j += 1
        k += 1

def merge_sort(arr, low, high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(arr, low, mid)
        merge_sort(arr, mid + 1, high)
        merge(arr, low, mid, high)


# ! tim sort

def tim_sort(arr):
    # * Python's built in function uses timsort
    return sorted(arr)


arr = [64, 25, 12, 22, 11]
sorted_arr = selection_sort(arr)
print("Selection Sorted array:", sorted_arr)

merge_sort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)

sorted_arr = tim_sort(arr)
print("Timsorted array:", sorted_arr)