def primeFactors(number):
    dato = int(number)
    primo = []
    while copy != 1:
        for num in range (2, int(number) +1):
            while dato % num == 0:
                dato = dato // num
                primes.append(num)
    return primo + dato
    raise NotImplementedError