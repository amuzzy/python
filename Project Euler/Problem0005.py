## Project Euler Problem 5
##
## 2520 is the smallest number that can be divided by each of the numbers from
## 1 to 10 without any remainder.  What is the smallest positive number that
## is evenly divisible by all of the numbers from 1 to 20.
##
## Answer: 232792560

def Problem5():
    x = 0
    while x != -1:
        ## Answer will always be a multiple of 20, no need to increment
        ## by anything less than 20.
        x+=20 

        ## Numbers 11-20 are divisible by 1-10, so we can skip those.
        if x % 11 != 0:
            continue
        if x % 12 != 0:
            continue
        if x % 13 != 0:
            continue
        if x % 14 != 0:
            continue
        if x % 15 != 0:
            continue
        if x % 16 != 0:
            continue
        if x % 17 != 0:
            continue
        if x % 18 != 0:
            continue
        if x % 19 != 0:
            continue
        if x % 20 != 0:
            continue

        ## If a number has reached this point, then it is divisible by 1-20.
        ## Return the answer and end the while loop.
        return(x)
        x = -1
            
