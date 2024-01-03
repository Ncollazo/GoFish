

##**Introduction:**

The Go Fish card game is a classic game played with a standard deck of 52 cards. In this project, create a Python implementation of the game where one player competes against 4 computer-controlled opponents, referred to as "bots."

#**Abstract Data Types:**

#1. **Card ADT:**
   - Represents a single playing card in the deck.
   - Attributes include the card's suit and rank.
   - Operations:
     - Card(suit, rank): Creates a card object with the specified suit and rank.
     - getSuit(): Returns the suit of the card.
     - getNum(): Returns the number of the card 1-13 (J,Q,K).
     - isEqualsTo(otherCard): Determines if two cards are equivalent.
     - toString(): Returns a string representation of the card.

#2. **Deck ADT:**
   - Represents a standard deck of 52 playing cards.
   - Operations:
     - Deck(): Creates a new deck of 52 cards, initially unshuffled.
     - shuffle(): Shuffles the deck.
     - deal(): Returns and removes a card from the top of the deck.
     - len(): Returns the current number of cards in the deck.
     - isEmpty(): Checks if the deck is empty.
     - toString(): Returns a string representation of the deck.

##**Gameplay:**

Design and implement a driver program that enables the player to interact with the computer-controlled opponents. Here's a breakdown of the main function and potential helper functions:

#1. **Main Function:**
   - Initialize the player's hand and the hands of the bots.
   - Display the player's hand at the beginning of each round.
   - Allow the player to choose a card to ask for from a specific bot.
   - Check if the bot has the requested card; if yes, transfer the cards to the player; if no, the player draws from the remaining deck which is called the pond.
   - Bot's Turn: Randomly select a card for the bot to ask the player.
   - Repeat turns until a player runs out of cards or the deck becomes empty.
   - Determine the winner at the end of the game based on collected sets.

#2. **Initialize Hands Function:**
   - Create initial hands for the player and the bots.
   - Deal cards from the shuffled deck to each player, ensuring no matches in the initial hands.

#3. **Check for Matches Function:**
   - Check if a requested rank matches any cards in the bot's hand.
   - Transfer matching cards to the player if found; otherwise, the player draws from the deck.

##**Specifications:**

- File names: GoFishCard.py, GoFishDeck.py, GoFishGame.py.
---
