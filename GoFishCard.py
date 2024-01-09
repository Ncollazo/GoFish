
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
    def __init__(self, cardSuits, cardNum):
        num_to_int = {
            "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6,
            "seven": 7, "eight": 8, "nine": 9, "ten": 10, "jack": 11, "queen": 12, "king": 13
        }
        
        suits = ["spades", "hearts", "diamonds", "clubs"]
        assert cardSuits.lower() in suits, "Error: Suit should be one of the four types."
        
        assert cardNum.lower() in num_to_int.keys(), "Error: Card number should be one of the thirteen types."
        
        self._numder = cardNum.lower()
        self._suits = cardSuits.lower()
      
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
        card_suits = self._suits[0].upper()
        card_num = str(self._numder).upper()
        return card_suits + ":" + card_num
        