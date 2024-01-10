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

def choose_number(bot_hands):
    all_cards = [card for hand in bot_hands for card in hand]

    # Calculate the number counts within the bot's hands
    num_counts = {}
    for card in all_cards:
        num = card.getNum()
        if num in num_counts:
            num_counts[num] += 1
        else:
            num_counts[num] = 1

    # Find numbers that appear multiple times (more than two cards)
    multiple_options = [num for num, count in num_counts.items() if count >= 3]

    if multiple_options:
        return random.choice(multiple_options)  # Choose from numbers that appear three or more times
    else:
        # If there are no numbers with three or more cards, choose randomly from available numbers
        available_numbers = list(num_counts.keys())
        return random.choice(available_numbers)

def organize_hand(hand):
    organized_hand = {}
    
    for card in hand:
        num = card.getNum()
        if num in organized_hand:
            organized_hand[num].append(card)
        else:
            organized_hand[num] = [card]
    
    organized = []
    for key in sorted(organized_hand.keys()):
        organized.extend(organized_hand[key])
    
    return organized   

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
    all_players = [player_hand,bot_hand1,bot_hand2,bot_hand3]
    bot_names = ["Tank Sinatra", "Elfish Presley", "Norman Baits"]
    all_names = ["You","Tank Sinatra", "Elfish Presley", "Norman Baits"]

    pond = initializeHands(player_hand, bot_hand1, bot_hand2, bot_hand3)
    
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


    # Player's turn
        if count % 2 == 0:
            player_hand = organize_hand(player_hand)
            print("Your Hand: ", player_hand)
            print("[]" * len(player_hand), "")
            for i, bot_name in enumerate(bot_names, start=1):
                print(f"Player {i}: {bot_name}")
                print("[]" * len(bot_hands[i - 1]), "")
                print(f"{bot_name}'s hand {organize_hand(bot_hands[i - 1])}")


        while True:
            try:
                ask_a_bot = int(input("Choose a player to ask from 1 to 3: "))  # Input to select a bot
                bot_index = ask_a_bot - 1
                if ask_a_bot in [1, 2, 3]:
                    break
                else:
                    print("Please enter a number from 1 to 3.")
            except ValueError:
                print("Please enter a valid number.")

        num_to_ask = int(input("Choose a number to ask from 1 to 13: "))
        found = False
        selected_bot_hand = bot_hands[bot_index]
        
        i = 0
        while i < len(selected_bot_hand):
            card = selected_bot_hand[i]
            if card.getNum() == num_to_ask:
                player_hand.append(card)
                selected_bot_hand.remove(card)
                found = True
                print(f"{bot_names[bot_index]} gave you {card}.")
                break
            else:
                i += 1

        if not found:
            print(f"{card} not found in {bot_names[bot_index]}'s hand.")
            if len(pond) > 0:
                card_from_pond = pond.pop()
                player_hand.append(card_from_pond)
                print(f"You picked {card_from_pond} from the pond.")
            elif len(pond) == 0:
                print(f"There is no more in the pond.")

        # Bot turns
        for i in range(len(bot_hands)):
            bot_hand = bot_hands[i]
            bot_name = bot_names[i]
            print("this is turn", bot_name )

            # Get the number to ask using the choose_number function
            num_to_ask = choose_number(bot_hands)       

            # Randomly choose a player to remove cards, excluding the current bot
            available_players = [player for player in all_players if player != bot_hand]
            chosen_player = random.choice(available_players)
            chosen_player_name = chosen_player

            # Ask the player for the chosen number
            found = False
            for card in chosen_player:
                if card.getNum() == num_to_ask:
                    bot_hand.append(card)
                    chosen_player.remove(card)
                    found = True
                    chosen_player_name = [name for name in all_names if chosen_player in all_players][0]
                    print(f"{bot_name} took {card} from {chosen_player_name}.")
                    break
        
            if not found:
                chosen_player_name = [name for name in all_names if chosen_player in all_players][0]
                print(f"{chosen_player_name} doesn't have {num_to_ask}.")
                # Handle picking from the pond or alternative strategy
                if len(pond) > 0:
                    card_from_pond = pond.pop()
                    player_hand.append(card_from_pond)
                elif len(pond) == 0:
                    print(f"There is no more in the pond.")
                    print(f"Once you ask a player and they don't have the card, you gain nothing.")

        # Check game end conditions
        if checkGameEnd(player_hand, bot_hands):
            break

        count += 1
                
# end of main     
main()        
    
    
    
    
    
    
    