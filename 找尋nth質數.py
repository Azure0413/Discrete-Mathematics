def isPrime(n):
    if (n == 1):
        return False

    s = 2
    while (s < n):
        if (n % s == 0):
            return False
        s += 1
    return True


def nthPrime(number):
    primes = [2, 3, 5, 7, 11, 13]
    starter = 17
    while (len(primes) < number):
        primeCheck = True
        for n in primes:
            if (starter % n == 0):
                primeCheck = False
                break
        if (primeCheck):
            primes.append(starter)
        starter += 2
    return primes[number - 1]


print(nthPrime(10))
print(nthPrime(20))
print(nthPrime(30))
print(nthPrime(100))

# n >= 2, n is either a prime or a product of primes
# check if 17 is a prime
# 2, 3, 5, 7, 11, 13
