 
#N,Collazo
#
#GoFishDeck.py
# 
 
import random
from GoFishCard import GoFishCard

class GoFishDeck: 
  
    def __init__ (self):
        self._deck = []
        num_to_int = {
            "One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6,
            "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 11, "Queen": 12, "King": 13
        }
        
        suits = ["Spades", "Hearts", "Diamonds", "Clubs"] 

        for suit in suits:
            for num, val in num_to_int.items():
                card = GoFishCard(suit, num)
                self._deck.append(card)
       
    def shuffle(self): 
        random.shuffle(self._deck) 

    def deal(self):
        return self._deck.pop(len(self._deck) - 1)
    
    def isEmpty(self):
        return len(self._deck) == 0
    
    def len(self):
        return len(self._deck)
    
    def __repr__(self):
        deckstr = "["
        for i in range(len(self._deck)):
            if (i != len(self._deck) - 1):
                deckstr += str(self._deck[i]) + ", "
            else:
                deckstr += str(self._deck[i]) + "]"
        return deckstr

    