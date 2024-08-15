numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for d in numbers:
    if d > 1:
        for i in range(2, d):
            if(d % i) == 0:
                not_primes.append(d)
                break
        else:
            primes.append(d)
print("Список простых чисел: ", primes)
print("Список не простых чисел: ", not_primes)