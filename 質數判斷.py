def isPrime(n):
    if (n == 1):
        return False

    s = 2
    while (s < n):
        if (n % s == 0):
            return False
        s += 1
    return True


print(isPrime(91))  # False
print(isPrime(21))  # False
print(isPrime(6252))  # False
print(isPrime(101))  # True
