"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes < 1:
        raise ValueError("Number smaller than 0")
    list = []
    i = 2
    con = True
    while con:
        list.append(i)
        for j in range(2,i):
            if i % j == 0:
                list.remove(i)
                break
        i += 1
        if len(list) == number_of_primes:
            con = False
    return list
