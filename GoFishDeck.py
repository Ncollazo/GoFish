 
#N,Collazo
#
#GoFishDeck.py
# making the cats and Flerken card to make a Flerken deck 
 
import random
from GoFishCard import GoFishCard

#creates a deck of 57 Flerken cards 
class GoFishDeck: 
  
  # Two cards should be created and added to the deck for each breed/color combinationcreating 56 cards. 
  # single Flerken card should be created and added to the deck with a random color
  def __init__ (self):
    #emidy list 
    self._deck = []

    # card suits 
    suits = ["spades","hearts","diamonds","clubs"]

    #card numder   
    numder = ["one","two","three","four", "five","six","seven","eight","nine","ten","jack", "queen"," king"]
    
    for suit in suits:
      for num in numder:
       #making deck 52 cards
        card = GoFishCard(suit,num)
        self._deck.append(card)
   
    
  
  #shuffles the deck of cards in random ordering
  #@return shuffles the deck of cards in random ordering
  def shuffle(self): 
    random.shuffle(self._deck) 
    
  
  #Removes the card from the top of the deck
  #@return removes the card from the top of the deck
  def deal(self):
    return self._deck.pop(len(self._deck)-1)
  
  #boolean indicating whether or not the deck is empty
  #@return whether or not deck is empty
  def isEmpty(self):
    if len(self._deck) == 0:
      return True
    else:
      return False
    
  
  # get the len of number of cards in the deck
  # @returns the current number of cards in the deck.
  def len(self):
    return len(self._deck)
  
  # string representation of the deck surrounded by [ ]. 
  #@return deck 
  def __repr__(self):
    deckstr = "["
    for i in range(len(self._deck)):
        if (i != len(self._deck) - 1):
            deckstr += str(self._deck[i]) + ", "
        else:
            deckstr += str(self._deck[i]) + "]"
    return deckstr
    