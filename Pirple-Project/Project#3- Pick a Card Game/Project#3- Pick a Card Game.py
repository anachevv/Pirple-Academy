"""
Pick a Card Game:UNO!
"""
import random

Deck = []
colours = ["Red", "Green", "Yellow", "Blue"]
faceValues = ["0","1","2","3","4","5","6","7","8","9", "Draw Two", "Skip", "Reverse"]
wilds = ["wilds", "Wild Draw Four"]
def createDeck():
    for colour in colours:
        cardVal = "  ", format(str(colour, faceValues))
        Deck.append(cardVal)
        if cardVal != 0:
            Deck.append(cardVal)
    for i in range(4):
        Deck.append(wilds[0])
        Deck.append(wilds[1])
    return Deck


def shuffleDeck(Deck):
    for cardPos in range(len(Deck)):
        randPos = random.randint(0,107)
        Deck[cardPos], Deck[randPos] = Deck[randPos], Deck[cardPos]
        return Deck

def drawCards(numCards):
    cardsDrawn = []
    for x in range(numCards):
        cardsDrawn.append(unoDeck.pop(0))
    return cardsDrawn


def showHand(player, playerHand):
    print("Player {}'s turn",format(player+1))
    print("Your hand")
    y = 1
    for card in playerHand:
        print(card)
        print("{}) {}".format(y,card))
    y += 1
def canPlay(discardCard,playerHand):
    for card in playerHand:
        splitCard = discardCard.split(" ",1)
        if "Wild" in card:
            return True
        elif colours in card or cardVal in card:
            return True
    return False
unoDeck = createDeck()
unoDeck = shuffleDeck(unoDeck)
discards = []
print(unoDeck)

players = []
colours = ["Red", "Green", "Yellow", "Blue"]
numPlayers = int(input("How many players?"))
while numPlayers<2 or numPlayers>4:
    numPlayers = int(input("Invalid. Please enter a number between 2-4. How many players?"))
for player in range(numPlayers):
    players.append(drawCards(5))

print(players)
playerTurn = 0
playDirection = 1
splitCard = 0
playing = True
discards.append(unoDeck.pop(0))
currentColour = splitCard[0]
if currentColour != "Wild":
    cardVal = splitCard[1]
else:
    cardVal = "Any"

splitCard = discards[0].split(" ",1)
while playing:
    showHand(playerTurn,players[playerTurn])
    print("Card on top of discard pile: {}",format(discards[-1]))
if canPlay(currentColour, cardVal, players[playerTurn]):
    cardChosen = input("Which card do you want to play?: ")
    while not canPlay(currentColour, cardVal,[player[playerTurn[cardChosen-1]]]):
        cardChosen = int(input("Not a valid card. Which card do you want to play? "))
        print("You played {}".format(players[playerTurn[cardChosen-1]]))
        discards.append(players[playerTurn].pop(cardChosen-1))
    if len(players[playerTurn]) == 0:
        playing = False
        winner = "Player {}".format(playerTurn +1)
    print("You can't play. You have to draw a card.")
    players[playerTurn].extend(drawCards(1))

splitCard = discards[-1].split(" ",1)
currentColour = splitCard[0]
if len(splitCard) == 1:
    cardVal = "Any"
else:
    cardVal = splitCard[1]
if currentColour == "Wild":
    for x in range(len(colours)):
        print("{}) {}".format(x+1, colours[x]))
    newColour = int(input("What colour would you like to choose? "))
    while newColour < 1 or newColour > 4:
        newColour = int(input("Invalid option. What colour would you like to choose? "))
        currentColour = colours[newColour-1]
if cardVal == "Reverse":
    playDirection = playDirection * -1
elif cardVal == "Skip":
    playerTurn += playDirection
elif cardVal == "Draw Two":
    playerDraw = playerTurn + playDirection
    if playerTurn == numPlayers:
        playerDraw == 0
    elif playerDraw < 0:
        playerDraw = numPlayers - 1

    players[playerDraw].extend(drawCards(2))
elif cardVal == "Draw Four":
    players[playerTurn].extend(drawCards(4))
playerTurn += playDirection
if playerTurn >= numPlayers:
    playerTurn = 0
elif playerTurn < 0:
    playerTurn = numPlayers - 1

print("Game Over")
print("{} is the winner!")