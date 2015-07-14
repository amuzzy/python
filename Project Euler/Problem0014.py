## Problem 14
##
## The following iterative sequence is defined for the set of positive integers:
##
## n → n/2 (n is even)
## n → 3n + 1 (n is odd)
##
## Using the rule above and starting with 13, we generate the following sequence:
##
## 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
## It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
##
## Which starting number, under one million, produces the longest chain?
##
## Answer: 837799

def Problem14():
    ## This solution is not optimized.  I'm sure there is a way to do this
    ## faster.  Probably by skipping numbers it's already calculated.
    
    longestSequence = 0

    for everyNumber in range(1,1000000):
        sequenceLength = 1
        n = everyNumber

        while n > 1:
            ## run the rule
            if n % 2 == 0:
                n = n/2
                sequenceLength += 1

            else:
                n = (3*n) + 1
                sequenceLength += 1
        
        if n == 1:
            ## Check sequence to see if it's the longest
            if sequenceLength >= longestSequence:
                longestSequence = sequenceLength
                print("New record: %d has length %d" % (everyNumber, sequenceLength))
                
            
            
