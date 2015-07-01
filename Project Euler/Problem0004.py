## Project Euler Problem 4
##
## A palindromic number reads the same both ways.  The largest
## palindrome made from the product of two 2-digit numbers is
## 9009 = 91 * 99.
##
## Find the largest palindrome made from the product of two 3-
## digit numbers.
##
## Answer: 906609

## Start with 999 x 999 and iterate second number down until it
## is equal with the first number, then iterate first number down.
## If the result of multiplying those numbers is a palindrome, return it.

def Problem4():
    answer = 0
    firstNum = 999
    while firstNum > 99:
        secondNum = 999
        while secondNum >= firstNum:
            numUnderTest = firstNum * secondNum
            if numUnderTest > answer and str(numUnderTest) == (str(numUnderTest)[::-1]):
                answer = numUnderTest
                print(firstNum, secondNum)
            secondNum = secondNum - 1
        firstNum = firstNum - 1
    return(answer)
