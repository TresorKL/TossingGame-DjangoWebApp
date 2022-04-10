import random

 
    
def generateRandom():
    randomValue =random.randint(1,2)
    return randomValue
    
    
def findoutcome( guess, randomValue):
         
    if guess == randomValue:
        strOutcome = "WON"
    else:
        strOutcome ="FAILED"
            
    return strOutcome

def updateScore(guess,Lastsscore,randomValue):
    
    if guess == randomValue:
        newScore = Lastsscore +1
    else:
        newScore =Lastsscore
            
    return newScore

def updateNumberOfTosses(totToss):
    newNumOfTosses = totToss+1;
     
            
    return newNumOfTosses

def determineServerScrore(totalTosses, playerScore):
    
    serverScore = totalTosses-playerScore
    
    return serverScore