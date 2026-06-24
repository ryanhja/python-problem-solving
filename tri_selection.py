def tri_selection(arr):
    n = len(arr)
    for i in range(n - 1):
        _min = i
        for j in range(i + 1, n):
            if arr[j] < arr[_min]:
                _min = j
        arr[i], arr[_min] = arr[_min], arr[i]
    return arr


print(tri_selection([54, 78, 9, 42, 23, 180, 30, 74, 2, 73]))