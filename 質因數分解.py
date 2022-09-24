def primeFactor(n):
    answer = str(n) + " = "  # 1200 =
    p = 2
    while (p <= n):
        if (n % p == 0):
            answer += str(p) + " x "
            n /= p  # n = n / p
        else:
            p += 1
    print(answer[:len(answer) - 3])


primeFactor(1200)
primeFactor(91)  # 91 = 7 x 13
primeFactor(1001)

# 1200 = 2 x 2 x 2 x 2 x 3 x 5 x 5
# 1200 / 2 = 600
# 600 / 2 = 300
# 300 / 2 = 150
# 150 / 2 = 75
# 75 / 3 = 25
# 25 / 5 = 5
# 5 / 5 = 1
