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
    for everyChar in str(x):
        total += int(everyChar)

    print(total)
    
