# Cards we have
A = ["1C", "1P", "1O", "1E", "2C", "2P", "2O", "2E", "3C", "3P", "3O", "3E", "4C", "4P", "4O", "4E", "5C", "5P", "5O",
     "5E", "6C", "6P", "6O", "6E", "7C", "7P", "7O", "7E", "8C", "8P", "8O", "8E", "9C", "9P", "9O", "9E", "10C", "10P", "10O", "10E", "DC", "DP",
     "DO", "DE", "VC", "VP", "VO", "VE", "RC", "RP", "RO", "RE", "1C", "1P", "1O", "1E", "2C", "2P", "2O", "2E", "3C", "3P", "3O", "3E", "4C", "4P",
     "4O", "4E", "5C", "5P", "5O", "5E", "6C", "6P", "6O", "6E", "7C", "7P", "7O", "7E", "8C", "8P", "8O", "8E", "9C", "9P", "9O", "9E", "10C", "10P", "10O", "10E", "DC", "DP",
     "DO", "DE", "VC", "VP", "VO", "VE", "RC", "RP", "RO", "RE", "1C", "1P", "1O", "1E", "2C", "2P", "2O", "2E", "3C", "3P", "3O", "3E", "4C", "4P",
     "4O", "4E", "5C", "5P", "5O", "5E", "6C", "6P", "6O", "6E",  "7C", "7P", "7O", "7E", "8C", "8P", "8O", "8E", "9C", "9P", "9O", "9E", "10C", "10P", "10O", "10E", "DC", "DP",
     "DO", "DE", "VC", "VP", "VO", "VE", "RC", "RP", "RO", "RE"]

# To know how a full deck looks like
fullDeck = ["1C", "1P", "1O", "1E", "2C", "2P", "2O", "2E", "3C", "3P", "3O", "3E", "4C", "4P", "4O", "4E", "5C", "5P",
          "5O", "5E", "6C", "6P", "6O", "6E", "7C", "7P", "7O", "7E", "8C", "8P", "8O", "8E", "9C", "9P", "9O", "9E",
          "10C", "10P", "10O", "10E", "DC", "DP", "DO", "DE", "VC", "VP", "VO", "VE", "RC", "RP", "RO", "RE"]

# Function to count the number of full decks
def count():

    # Number of full decks
    numFullDeck = 0

    # Empty deck to store the cards
    deck = []


    # Goes through the list and puts the cards in the other list
    for i in A:
        deck.append(i)

        # If the deck matches the fullDeck then it adds 1 and clears the current deck
        if deck == fullDeck:
            numFullDeck += 1
            print(deck)
            deck = []

    # The cases of how many full can we have
    if numFullDeck == 0:
        print("There are no full decks.")
    elif numFullDeck == 1:
        print(" There is ", + numFullDeck + " full deck.")
    else:
        print(" There are ", + numFullDeck + " full decks.")

count()