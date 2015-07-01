## Project Euler Problem 10
##
## The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
##
## Find the sum of all the primes below two million.
##
## Answer = 142913828922


from math import sqrt

def Problem10():
    numberUnderTest = 2
    primeNum = 2
    primeList = []
    sumOfPrimes = 0

    while numberUnderTest != 2000000:
        divisibleBy = 0

        max = int(sqrt(numberUnderTest) + 1)

        for denominator in primeList:
            if denominator > max:
                break
            if numberUnderTest % denominator == 0:
                divisibleBy +=1
                break

        if divisibleBy == 0:
            primeNum += 1
            primeList.append(numberUnderTest)
            sumOfPrimes += numberUnderTest
            
        numberUnderTest += 1

    return(sumOfPrimes)
