 
#N,Collazo
#
#GoFishDeck.py
# making the cats and Flerken card to make a Flerken deck 
 
import random
from GoFishCard import GoFishCard

class GoFishDeck: 
  
    def __init__ (self):
        self._deck = []
        suits = ["spades","hearts","diamonds","clubs"]
        num_to_int = {
            "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6,
            "seven": 7, "eight": 8, "nine": 9, "ten": 10, "jack": 11, "queen": 12, "king": 13
        }  

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

    