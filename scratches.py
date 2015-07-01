import random

def roll():
    ## Dice roller.
    ##
    ## To Do:
    ##  1: Exploding dice.  i.e. 1d6x
    ##  2: Fudge dice.  i.e. fate or f
    ##  3: Multi dice roll.  i.e. 1d6x 1d8x
    
    x = 0
    while x != 1:
        dietype = input("Die Type: ")

        ## Make d20 the default
        if dietype == '':
            dietype = 20
            print("d%s = %d" % (dietype, random.randint(1,int(dietype))))

        ## Check for Fate Dice
        elif dietype == "f":
            total = []
            fate = ""
            for eachDie in range(0,4):
                dieresult = random.randint(1,3)

                if dieresult == 1:
                    total.append("-")
                elif dieresult == 2:
                    total.append(" ")
                else:
                    total.append("+")
            print(fate.join(total))
        

        ## Check for Exploding Dice
        #elif dietype.find('x') > 0:
            
        ## Check to see if input is a multi-roll            
        elif dietype.find('d') > 0:
            ## Break string into parts before and after 'd'
            dicenum = dietype[:dietype.find('d')]
            dietype = dietype[dietype.find('d')+1:]
            total = 0
            
            for eachDie in range(0,int(dicenum)):
                total += (random.randint(1,int(dietype)))

            print (dicenum,"d%s = %d" % (dietype, total))
            
        ## Normal Roll   
        else:
            print("d%s = %d" % (dietype, random.randint(1,int(dietype))))
        
