def tri_insertion(arr):
    for i in range(1, len(arr)):
        cle = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > cle:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = cle
    return arr


print(tri_insertion([54, 78, 9, 42, 23, 180, 30, 74, 2, 73]))
