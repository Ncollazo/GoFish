
#N.Collazo
#
#GoFishCard.py
# 
#

import random
#
class GoFishCard: 
    
    def __init__(self, cardSuits, cardNum):
        num_to_int = {
            "One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6,
            "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 11, "Queen": 12, "King": 13
        }
        
        suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
        assert cardSuits.capitalize() in suits, "Error: Suit should be one of the four types."
        
        assert cardNum.capitalize() in num_to_int.keys(), "Error: Card number should be one of the thirteen types."
        
        self._num_to_int = num_to_int[cardNum.capitalize()]
        self._suits = cardSuits.capitalize()
        self._int_to_num = {v: k for k, v in num_to_int.items()}

    def getKeyFromValue(self, value):
        return self._int_to_num.get(value)
    
    def getNum(self):
        return self._num_to_int

    def getSuits(self):
        return self._suits
    
    def __eq__(self, other):
        return self._num_to_int == other.getNum()
    
    def __repr__(self):
        card_suits = self._suits
        card_num = self.getKeyFromValue(self._num_to_int)
        return card_suits + ":" + card_num


        