def bubble_sort(arr, n):
    for i in range(n - 1):
        for j in range(n - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


arr = [5, 6, 1, 4, 2, 8, 9, 3]
print(bubble_sort(arr, len(arr)))
