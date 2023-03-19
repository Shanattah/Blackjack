import random

# The type of suit
suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
 
# The type of card
cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

# The values of each card
cards_values = {"A": 11, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}

def generateDeck():
    deck = []
    for suit in suits:
        for card in cards:
            deck.append((card, suit))
    random.shuffle(deck)
    return deck

def getCardValue(card):
    key = card[0]
    value = cards_values[key]
    return value

def turn(deck, current_score):
    card = deck.pop(0)
    print(">> ", card)
    cardValue = getCardValue(card)
    new_score = current_score + cardValue
    return new_score

def playGame():  
    
    # Setup
    deck = generateDeck()
    dealerScore = 0
    playerScore = 0
    
    print("-------------------------Dealers Hand-------------------------")
    dealerScore = turn(deck, dealerScore);
    dealerScore = turn(deck, dealerScore);
    print("Dealers score:", dealerScore)
    
    print("-------------------------Players Hand-------------------------")
    playerScore = turn(deck, playerScore);
    playerScore = turn(deck, playerScore);
    print("Your score:", playerScore)

    print("-------------------------Begin Game-------------------------")
    keepPlaying = True
    if playerScore == 21:
        print("Player blackjack! You win!")
        keepPlaying = False
    elif dealerScore == 21:
        print("Dealer blackjack! You lose!")
        keepPlaying = False
    while keepPlaying:      
        userChoice = input("HIT or STAND: ")
        if (userChoice == "HIT"):
            playerScore = turn(deck, playerScore)
            print("Your total:", playerScore)
            print("Dealer total:", dealerScore)
            if playerScore > 21:
                print("-------------------------You bust, dealer wins!-------------------------")
                keepPlaying = False
        elif (userChoice == "STAND"):
            print("-------------------------Dealers Hand-------------------------")
            dealerScore = turn(deck, dealerScore)
            print("Your total:", playerScore)
            print("Dealer total:", dealerScore)
            if dealerScore > 21:
                print("-------------------------Dealer busts, you win!-------------------------")
            elif dealerScore == playerScore:
                print("-------------------------Tie!-------------------------")
            elif dealerScore > playerScore:
                print("-------------------------You lose, dealer wins!-------------------------")
            else:
                print("-------------------------Dealer loses, you win!-------------------------")
            keepPlaying = False
        else:
            print("Please enter valid input: 'HIT' or 'STAND'")

            
playGame()
