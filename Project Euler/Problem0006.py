## Project Euler Problem 6
##
## The sum of the squares of the first ten natural numbers is:
##
## 1^2 + 2^2 + 3^2... = 385
##
## The square of the sum of the first ten natural numbers is:
##
## (1 + 2 + 3... )^2 = 55^2 = 3025
##
## Hence the difference between the sum of the squares and the square of the
## sums is 3025 - 385 = 2640.
##
## Find the difference between the sum of the squares of the first one
## hundred natural numbers and the square of the sum.
##
## Answer: 25164150

def Problem6():
    squareofsums = 0
    sumofsquares = 0

    for everyNum in range(1,101):
        sumofsquares += everyNum**2
        squareofsums += everyNum

    squareofsums = squareofsums**2

    return(squareofsums - sumofsquares)
