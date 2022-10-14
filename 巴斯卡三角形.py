def Pascal(n):
    f = [1]
    m = []  # middle
    i = 1
    while (i <= n):
        f = [1] + m + [1]
        m = []
        for j in range(0, len(f) - 1):
            m.append(f[j] + f[j + 1])
        i += 1
    return f


print(Pascal(0))
print(Pascal(1))
print(Pascal(2))
print(Pascal(6))
# Pascal(0) [1]
# Pascal(1) [1, 1]
# Pascal(2) [1, 2, 1]
