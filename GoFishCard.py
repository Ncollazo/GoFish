
#N.Collazo
#
#GoFishCard.py
# 
#

import random
#
class GoFishCard: 
    
    # Creates a single Card with a random suit  and numder
    # @param cardSuits, is the four allowed  
    # @param cardNum, is the 13 allowed  
    def __init__ (self, cardSuits, cardNum):
        
        #card numder   
        numder = ["one","two","three","four", "five","six","seven","eight","nine","ten","jack", "queen"," king"]
        
        # card suits 
        suits = ["spades","hearts","diamonds","clubs"]
        
          
        assert cardSuits.lower() in suits ,"Error: only suits can be only theses 4 types"
        


        assert cardNum.lower() in numder , "Error: only num it can only be theses 13 numders"
        
        self._numder = cardNum
        
        self._suits = cardSuits
      
    # number of the card as a string 
    #@return  the card num as a string in lowercase.
    def getNum(self):
        return self._numder
    
    # suit of the card  as a string 
    #return suits of the card as a string in lowercase
    def getSuits(self):
        return self._suits
    
    
    #  two cards are equivalent (True) or not (False).
    # @param other,is a diffent card
    # @return the card if = to other card    
    def __eq__(self,other): 
        if(self._numder == other.getNum()):
                return True
        return False
    
    #string representation of the card of the form capitalized first letter of color and capitalized breed
    def __repr__(self):
        cardSuits1 = self._suits[0].upper()
        cardNum = self._numder.upper()
        return cardSuits1 + ":" + cardNum
        