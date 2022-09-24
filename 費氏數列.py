# Part I
# A1 = 1
# An = 2 * A(n-1) + 7
# Recursive Algorithm = Call a function inside the function itself
# Call Stack
def recursiveSequence(n):
    print(n)
    if n == 1:
        return 1
    else:
        return 2 * recursiveSequence(n - 1) + 7


# Part II


def fab(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fab(n - 1) + fab(n - 2)


print(fab(10))
