import random

# This is a class named "Card" that represents a playing card. It has three attributes: "rank", "suit", and "value". The "rank" and "suit" attributes are set when the object is initialized, and the "value" attribute is set using a private method called "_get_card_value()", which returns the point value of the card based on its rank.
#The "str()" method is also defined in the class, which returns a string representation of the card object, in the format of "{rank} of {suit}".

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = self._get_card_value(rank)
        
    def __str__(self):
        return f"{self.rank} of {self.suit}"
        
    def _get_card_value(self, rank):
        return {
            "A": 11,
            "K": 10,
            "Q": 10,
            "J": 10,
            "10": 10,
            "9": 9,
            "8": 8,
            "7": 7,
            "6": 6,
            "5": 5,
            "4": 4,
            "3": 3,
            "2": 2
        }[rank]

class Deck:
    def __init__(self):
        # Initializes a new deck by generating and shuffling a list of cards
        self.cards = self._generate_deck()
        
    def __str__(self):
        # Returns a string representation of the deck
        return ', '.join(str(card) for card in self.cards)
    
    def _generate_deck(self):
        # Generates a standard deck of 52 cards with ranks A-K and suits Spades, Hearts, Clubs, and Diamonds
        deck = []
        for suit in ["Spades", "Hearts", "Clubs", "Diamonds"]:
            for rank in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]:
                card = Card(rank, suit)
                deck.append(card)
        # Shuffles the deck
        random.shuffle(deck)
        return deck
    
    def deal_card(self):
            # Deals the top card from the deck (removes it from the list of cards and returns it)
        return self.cards.pop(0)
    
class Hand:
    def __init__(self):
        # List to store cards in the hand
        self.cards = []
        # Total score of the cards in the hand
        self.score = 0
        
    def __str__(self):
        # String representation of the hand
        return ', '.join(str(card) for card in self.cards)
        
    def add_card(self, card):
        # Method to add a new card to the hand and update the score
        self.cards.append(card)
        self.score += card.value
        # If the hand has an Ace and score is over 21, change Ace value to 1
        if self.score > 21 and any(card.rank == "A" for card in self.cards):
            self._adjust_for_ace()
            
    def _adjust_for_ace(self):
        # Method to adjust the score when an Ace's value is changed to 1
        self.score -= 10
        # Change value of the first Ace found to 1
        for card in self.cards:
            if card.rank == "A":
                card.value = 1
                break

class BlackjackGame:
    def __init__(self):
        # Create a new deck and hands for the dealer and player
        self.deck = Deck()
        self.dealer_hand = Hand()
        self.player_hand = Hand()
        # Set the game_over flag to False
        self.game_over = False
        
    def _display_hands(self):
        # Print the dealer's first card face up and the player's cards
        print(f"Dealer's hand: {self.dealer_hand.cards[0]}, HIDDEN")
        print(f"Your hand: {self.player_hand}")
        
    def _check_blackjack(self):
        # Check if either the dealer or player has a blackjack
        if self.player_hand.score == 21:
            print("Player blackjack! You win!")
            # Set the game_over flag to True
            self.game_over = True
        elif self.dealer_hand.score == 21:
            print("Dealer blackjack! You lose!")
            # Set the game_over flag to True
            self.game_over = True
            
    def _dealer_turn(self):
        # Dealer draws cards until their hand value is at least 17
        while self.dealer_hand.score < 17:
            self.dealer_hand.add_card(self.deck.deal_card())
            print(f"Dealer draws: {self.dealer_hand.cards[-1]}")
            print(f"Dealer total: {self.dealer_hand.score}")
            if self.dealer_hand.score > 21:
                print("-------------------------Dealer busts, you win!-------------------------")
                # Set the game_over flag to True
                self.game_over = True
    
    def play(self):
        # Deal two cards to the dealer and player and display them
        print("-------------------------Dealers Hand-------------------------")
        self.dealer_hand.add_card(self.deck.deal_card())
        self.dealer_hand.add_card(self.deck.deal_card())
        print(f"Dealer's hand: {self.dealer_hand.cards[0]}, HIDDEN")
        print(f"Dealer's current score: {self.dealer_hand.score - self.dealer_hand.cards[1].value}")

        print("-------------------------Players Hand-------------------------")
        self.player_hand.add_card(self.deck.deal_card())
        self.player_hand.add_card(self.deck.deal_card())
        print(f"Your hand: {self.player_hand}")
        print(f"Your current score: {self.player_hand.score}")


        # Check for blackjack
        self._check_blackjack()

        # Continue playing until the game is over
        while not self.game_over:
            # Prompt the player to hit or stand
            action = input("Do you want to hit or stand? ").lower()
            if action not in ["hit", "stand"]:
                print("Invalid input. Please enter 'hit' or 'stand'.")
                continue
            if action == "hit":
                # Add a card to the player's hand and display it
                self.player_hand.add_card(self.deck.deal_card())
            print(f"You draw: {self.player_hand.cards[-1]}")
            print(f"Your total: {self.player_hand.score}")
            if self.player_hand.score > 21:
                print("-------------------------You bust, dealer wins!-------------------------")
                # Set the game_over flag to True
                self.game_over = True
            elif action == "stand":
                # Play out the dealer's turn
                self._dealer_turn()
                if not self.game_over:
                    # Determine the winner of the game
                    if self.player_hand.score > self.dealer_hand.score:
                        print("-------------------------You win!-------------------------")
                        self.game_over = True
                    elif self.player_hand.score == self.dealer_hand.score:
                        print("-------------------------Push! It's a tie.-------------------------")
                        self.game_over = True
                    else:
                        print("-------------------------Dealer wins!-------------------------")
                        self.game_over = True
            #Final result
            print("-------------------------Dealer's Hand-------------------------")
            print(f"Dealer's hand: {self.dealer_hand}")
            print(f"Dealer's total: {self.dealer_hand.score}")

            print("-------------------------Your Hand-------------------------")
            print(f"Your hand: {self.player_hand}")
            print(f"Your total: {self.player_hand.score}")

#Start the game
game = BlackjackGame()
game.play()

