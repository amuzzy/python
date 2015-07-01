## Project Euler Problem 9
##
## A Pythagorean triplet is a set of three natural numbers,
## a < b < c, for which,
##
## a^2 + b^2 = c^2
## For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
##
## There exists exactly one Pythagorean triplet for which
## a + b + c = 1000.
##
## Find the product abc.
##
## Answer: 31875000

## Start with 1,2,3 in a list.  Iterate the values within the list
## until the product of the three is greater than 1,000.
##
## Iterate the 3rd number, until limit is reached, then iterate the
## 2nd number, etc.
##
## Square the values and determine if their product is 1,000.
## If not, continue the iteration.

def Problem9():

    ## create nested loops to iterate.
    for FirstNums in range (1,1000):        
        for SecondNums in range (1,1000-FirstNums):            
            LastNum = 1000 - SecondNums - FirstNums
            ## Numbers must always total to 1000
            
            if FirstNums**2 + SecondNums**2 == LastNum**2:
                return(FirstNums * SecondNums * LastNum)

    return("solution not found")
