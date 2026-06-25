def tri_bulle(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


print(tri_bulle([54, 78, 9, 42, 23, 180, 30, 74, 2, 73]))
