## Project Eueler Problem 3
##
## The prime factors of 13195 are 5, 7, 13 and 29.
##
## What is the largest prime factor of the number 600851475143
##
## Answer: 6857



## I don't totally understand how this works, but it gets the list of factors.

def Problem3():
    count = 600851475143
    factors = []
    d = 2
    total = 0

    while count > 1:
        while count % d == 0:
            factors.append(d)
            count /= d
        d = d + 1

## Now that I have a list of primes, return the last value
        
    return(factors[-1])

