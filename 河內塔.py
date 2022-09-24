def hanoi(n, a, b, c):
    print(a, b, c)
    if n == 1:
        element = a.pop()
        c.append(element)
    else:
        hanoi(n - 1, a, c, b)
        hanoi(1, a, b, c)
        hanoi(n - 1, b, a, c)


arr1 = ["arr1 is ", 5, 4, 3, 2, 1]
arr2 = ["arr2 is "]
arr3 = ["arr3 is "]
hanoi(5, arr1, arr2, arr3)
print("-------------")
print(arr1)
print(arr2)
print(arr3)
