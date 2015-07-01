## Project Euler Problem 1
##
## If we list all the natural numbers below 10 that are multiples of 3 or 5,
## we get 3, 5, 6 and 9. The sum of these multiples is 23.
##
## Find the sum of all the multiples of 3 or 5 below 1000.
##
##
## Answer: 233168

def Problem1():
    ## Initialize total
    total = 0

    ## Iterate from 1 to 999.  If number is evenly divisable by 3 or 5,
    ## add the value to to total.  Once complete, return the total.
    for everyInt in range(1,1000):
        if (everyInt % 3 == 0) or (everyInt % 5 == 0):
            total = total + everyInt

    return(total)

        
