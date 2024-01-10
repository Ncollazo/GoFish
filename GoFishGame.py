#N, Collazo
#
# the game of go fish everyone start with 7 cards out of 52 with  4 players max. 
# exta once the cards go into pond deck to be pulled out when the player 
# player will ask bot for a numder of a card igoring suit. 4 of same numder is need. 
# if they do not have that num card then they will pick from the pond.If they do bot will give the card.
# move to next player bot they get to ask other players(bot or main player) a numder at random. 
# untill the person with the empty their hand first wins. 


#import statemt
import random
from GoFishDeck import GoFishDeck
from GoFishCard import GoFishCard
from random import randint

# Initialize hands, bots, and number of bots
# Deal the deck and remove 4 matched cards (book)
# @param hand1 is the human player
# @param bot_hand1  bot 1 hand cards
# @param bot_hand2  bot 2 hand cards
# @param bot_hand2  bot 3 hand cards
# @return the leftover cards (pond) after initialization of the deck
def initializeHands(player_hand, bot_hand1, bot_hand2, bot_hand3):
    pond = []
    
    deck = GoFishDeck()
    deck.shuffle()

    count = 0

    while not deck.isEmpty():
        card = deck.deal()

        # Distribute 7 cards to each player
        if count < 7:
            player_hand.append(card)
        elif count < 14:
            bot_hand1.append(card)
        elif count < 21:
            bot_hand2.append(card)
        elif count < 28:
            bot_hand3.append(card)
       # Collect the remaining cards into the pond
        else:
            pond.append(card) 

        count += 1

   
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


def choose_number(hands):
    # Logic to choose the number from the combined hands (player and bots)
    # If there's a number that appears multiple times, prioritize it
    # Otherwise, choose randomly

    num_counts = {}

    # Combine all hands into a single list
    all_cards = [card for hand in hands for card in hand]

    for card in all_cards:
        num = card.getNum()
        if num in num_counts:
            num_counts[num] += 1
        else:
            num_counts[num] = 1

    # Find numbers that appear more than once
    multiple_options = [num for num, count in num_counts.items() if count >= 2]

    if multiple_options:
        return random.choice(multiple_options)  # Choose from numbers that appear multiple times
    else:
        available_numbers = list(num_counts.keys())
        
        return random.choice(available_numbers)  # Choose randomly if no number appears more than once

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
    bot_hands = [bot_hand1,bot_hand2,bot_hand3]

    pond = initializeHands(player_hand, bot_hand1, bot_hand2, bot_hand3)
    
    #title of game 
    print("(='.'=)--Go Fish Game--(='.'=)")
    
    # count for loop
    count = 0  

    # a while loop that print out the cards hand 1 and bot hands card as "[]"   
    bot_names = ["Tank Sinatra", "Elfish Presley", "Norman Baits"]

    while len(player_hand) > 0 and any(len(hand) > 0 for hand in bot_hands):
    # Check for matches and remove books
        match(player_hand)
        for bot_hand in bot_hands:
            match(bot_hand) 


    # Player's turn
        if count % 2 == 0:
            print("Your Hand: ", player_hand)
            for i, bot_name in enumerate(bot_names, start=1):
                print(f"Player {i}: {bot_name}")
                print("[]" * len(bot_hands[i - 1]), "")

        ask_a_bot = int(input("Choose a player to ask from 1 to 3: "))  # Input to select a bot
        bot_index = ask_a_bot - 1 
        num_to_ask = int(input("Choose a number to ask from 1 to 13: "))
        found = False
        selected_bot_hand = bot_hands[bot_index]
        
        i = 0
        while i < len(selected_bot_hand):
            card = selected_bot_hand[i]
            print(f"Checking card {card} in hand...")
            print(f"Card Number: {card.getNum()}, Num to Ask: {num_to_ask}")
            if card.getNum() == num_to_ask:
                player_hand.append(card)
                selected_bot_hand.remove(card)
                found = True
                print(f"{bot_names[bot_index]} gave you {card}.")
                break
            else:
                i += 1

        if not found:
            print("Card not found in bot's hand.")
            if len(pond) > 0:
                card_from_pond = pond.pop()
                player_hand.append(card_from_pond)
                print(f"You picked {card_from_pond} from the pond.")
            elif len(pond) == 0:
                print(f"There is no more in the pond.")
                print(f"Once you ask a player and they don't have the card, you gain nothing.")

        # Bot turns
        #I need to choose a random bot including the player from a list. 
        #And once that bot is chosen they'll ask a number between one and 13 and choose it 
        #how they choose the number will be if they have more than two cards of the same
        # number they will be more likely to choose that number if they do not they choose a random number that is in their deck if they asked a player a number
        # they will not ask the player the same number until all four players have played again.
        num_bots = len(bot_hands)
        all_players = [player_hand] + bot_hands  # Combine player and bot hands
        all_names = ["You"] + bot_names  # Combine player and bot names

        for i, hand in enumerate(all_players):
            print(f"Player {i + 1} Hand: {hand}")
    
        for i, hand in enumerate(all_players):
            chosen_player_hand = all_players[i]
            num_to_ask = choose_number(chosen_player_hand)  # Choose the number to ask
        
        # Ask the player for the chosen number
        found = False
        for card in all_players[i]:
            if card.getNum() == num_to_ask:
                chosen_player_hand.append(card)
                all_players[i].remove(card)
                found = True
                print(f"{all_names[i]} took {card} from {all_names[i]}.")
                break
        
        if not found:
            print(f"{all_names[i]} doesn't have {num_to_ask}.")
            # Handle picking from the pond or alternative strategy

        # Check game end conditions
        if checkGameEnd(player_hand, bot_hands):
            break

        count += 1
                
# end of main     
main()        
    
    
    
    
    
    
    