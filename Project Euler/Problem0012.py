## Project Euler Problem 12
##
## The sequence of triangle numbers is generated by adding the natural
## numbers.  So the 7th triangle number would be 1+2+3+4+5+6+7 = 28.
## The first ten terms would be:
##  1,3,6,10,15,21,28,26,45,55...
##
## Let us list the factors of the first seven triangle numbers:
##
## 1: 1
## 3: 1,3
## 6: 1,2,3,6
## 10: 1,2,5,10
## 15: 1,2,5,15
## 21: 1,3,7,21
## 28: 1,2,4,7,14,28
##
## We can see that 28 is the first triangle number to have over
## five divisors.  What is the value of the first triangle number
## to have over five hundred divisors?
##
## Answer:

## First of all, what is a Triangle Number?  It is the number of objects
## needed to form an equalateral triangle when stacked.
##  T1  T2=3  T3=6
##  0   0      0
##     0 0    0 0
##           0 0 0 .... and so on.
##
## The formula is as described in the instructions.  Do a while loop, and
## generate a total based on the current iteration.
##
## Secondly is how to find the factors/divisors.  An iterating loop looking
## for modulus zero ought to do it.

def Problem12():

    TriangleNumber = 2
    DivisorList = []
    
    while len(DivisorList) < 500:
        DivisorList = []
        ## Generate a total based on triangle number
        TriNumTotal = 0
        for eachDigit in range(0,TriangleNumber+1):
            TriNumTotal += eachDigit

        for eachDivisor in range(1,TriNumTotal+1):
            if TriNumTotal % eachDivisor == 0:
                DivisorList.append(eachDivisor)
        print(TriangleNumber)
        TriangleNumber += 1

    #print(DivisorList)
    #print(TriNumTotal)
    return(TriangleNumber-1)

                

        

        
