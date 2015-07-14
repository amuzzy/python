## Project Euler Problem 16
##
## 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
##
## What is the sum of the digits of the number 2^1000?
##
## Answer: 1366

def Problem16():
    x = 2 ** 1000
    total = 0

    ## Treat the value as a string, read the characters from it and
    ## add them up.
    
    for everyChar in str(x):
        total += int(everyChar)

    return(total)
    
