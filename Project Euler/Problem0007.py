## Project Euler Problem 7
##
## By listing the first six prime numbers: 2, 3, 5, 7, 11 and 13, we can see
## that the 6th prime is 13.
##
## What is the 10,001st prime number?
##
## Answer: 104743

## Need square root function
import math

def Problem7():

    ## Create a loop of the primeCount until it reaches 10,001.
    ## Create a number to be tested, and iterate to infinity.
    ## Try to divide that number by a range up to it's square root.
    ## If it's evenly divisible, move on to the next number
    ## else it's prime.  So iterate the prime count.

    primeCount = 0
    currentNumber = 2

    while primeCount != 10001:
        divisor = 2
        while divisor <= int(math.sqrt(currentNumber)):
            if currentNumber % divisor == 0:
                ## Number can't be prime, move to next number
                ## and reset the divisor
                currentNumber += 1
                divisor = 2
            else:
                ## A remainder exists, move to next divisor
                divisor += 1
        ## Number must be prime, iterate the prime number count
        ## and if it's the 10,001st prime, return the value.
        ## Otherwise iterate to the next number and continue.
        primeCount +=1
        if primeCount == 10001:
            return(currentNumber)
        currentNumber += 1

