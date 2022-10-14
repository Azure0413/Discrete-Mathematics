def swap(arr, n1, n2):
    arr[n1], arr[n2] = arr[n2], arr[n1]
    # the right side => tuple packing
    # the left side => tuple unpacking


def perm(arr, start):
    if start >= len(arr):
        result.append(arr.copy())
    else:
        for i in range(start, len(arr)):
            swap(arr, start, i)
            perm(arr, start + 1)
            swap(arr, start, i)


result = []
perm(['A', 'B', 'C', 'D', 'E', 'F'], 0)
print(result)
