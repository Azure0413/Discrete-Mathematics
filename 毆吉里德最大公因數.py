def gcd(a, b):
    while (b != 0):
        r = a % b
        a = b
        b = r
    return a


print(gcd(420, 66))  # 6
print(gcd(101, 43))  # 1