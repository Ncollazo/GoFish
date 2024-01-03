#N, Collazo
#
# the game of go fish everyone start with 7 cards out of 52 with  4 players max. 
# exta once the cards go into pond deck to be pulled out when the player 
# player will ask bot for a numder of a card igoring suit. 4 of same numder is need. 
# if they do not have that num card then they will pick from the pond.If they do bot will give the card.
# move to next player bot they get to ask other players(bot or main player) a numder at random. 
# untill the person with the empty their hand first wins. 


#import statemt
from GoFishDeck import GoFishDeck
from GoFishCard import GoFishCard
from random import randint

# Initialize hands, bots, and number of bots
# Deal the deck and remove 4 matched cards (book)
# @param hand1 is the human player
# @param bot_hands is a list of bot players' hands
# @param num_bots is the number of bot players (1-6)
# @return the leftover cards (pond) after initialization of the deck
def initializeHands(player_hand, bot_hands):
    deck = GoFishDeck()
    deck.shuffle()

    count = 1
    all_hands = [player_hand] + bot_hands
    while not deck.isEmpty():
        card = deck.deal()
        player_index = count % (len(bot_hands) + 1)
        if not match(card, all_hands[player_index]):
            all_hands[player_index].append(card)
        count += 1

    # Calculate the number of leftover cards in the pond
    pond = len(deck._deck) if hasattr(deck, '_deck') else 0
    return pond


# Match cards in the hand to form books of four cards with the same number
# Group of 4 is a book. Used every round after the main player picks.
# @param hand: The player's hand
# @return books: Books formed in the hand (if any), removed from the hand
def match(hand):
    if not hand:
        return []

    match_dict = {}
    for card in hand:
        if card.getNum() not in match_dict:
            match_dict[card.getNum()] = [card]
        else:
            match_dict[card.getNum()].append(card)
    
    books = []
    for num, cards in match_dict.items():
        if len(cards) == 4:  # If there are 4 cards with the same number, it forms a book
            books.extend(cards)
    
    for book in books:  # Remove the book from the hand
        hand.remove(book)
    
    return books

# Assuming you have initialized the hands for the player and bots

def playerTurn(player_hand, bot_hands, count):
    print("Your Hand: ", player_hand)
    num_to_ask = int(input("Choose a number to ask from 1 to 13: "))

    # Ask a specific bot for the chosen number
    # Loop through each bot's hand
    # If the bot has the requested number, take the cards from the bot's hand and append to the player's hand
    # Break the loop if the cards are found
    found = False
    for bot_hand in bot_hands:
        for card in bot_hand:
            if card.getNum() == num_to_ask:
                player_hand.append(card)
                bot_hand.remove(card)
                found = True
                break
        if found:
            break

## def botTurn(player_hand, bot_hands, count):
    for i, bot_hand in enumerate(bot_hands):
        print(f"Bot {i + 1} Hand: {bot_hand}")

        # Bot asks for a random number
        num_to_ask = randint(1, 13)

        # Similar logic as the player's turn
        # If the player has the requested number, take the cards from the player's hand and append to the bot's hand
        # Break the loop if the cards are found
        found = False
        for card in player_hand:
            if card.getNum() == num_to_ask:
                bot_hand.append(card)
                player_hand.remove(card)
                found = True
                break
        if found:
            break

def checkGameEnd(player_hand, bot_hands):
    if len(player_hand) == 0:
        print("You Won! (=^.^=)")
        print("You’re so tenta-cool!")
        return True
    elif all(len(hand) == 0 for hand in bot_hands):
        print("You Lost... (='-'=)")
        print("Well... Don't trout yourself ")
        return True
    return False

def main():

   # Get the number of bots
    ##num_bots = int(input("Enter the number of bots (1 to 5): "))

   # Initialize player's hand and bot hands as a list
    ##hand1 = []
    ##bot_hands = [[] for _ in range(num_bots)]


    # Split the deck among player and bots
    player_hand = []
    bot_hand1 = []
    bot_hand2 = []
    bot_hand3 = []
    bot_hands = [bot_hand1, bot_hand2, bot_hand3]

    pond = initializeHands(player_hand, bot_hands)
    
    #title of game 
    print("(='.'=)--Go Fish Game--(='.'=)")
    
    # count for loop
    count = 0  

    # a while loop that print out the cards hand 1 and bot hands card as "[]"   

    while len(player_hand) > 0 and any(len(hand) > 0 for hand in bot_hands):

        # Check for matches and remove books
        match(player_hand)

        for bot_hand in bot_hands:
            match(bot_hand) 
     
        #Player's turn
        if count % 2 == 0:
            print("Your Hand: ", player_hand)
            # Implement player's turn logic
            # Example: Ask for a card from a specific bot or handle player input
        
        # Bot turns
        else:
            for i, bot_hand in enumerate(bot_hands):
                print("Bot {i + 1} Hand: {bot_hand}")
                # Implement bot's turn logic
                # Example: Ask for a card from the player or from another bot
        
       # Check game end conditions
        if checkGameEnd(player_hand, bot_hands):
            break


        count += 1
      

            
# end of main     
main()        
    
    
    
    
    
    
    