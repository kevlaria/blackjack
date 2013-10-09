import random  # needed for shuffling a Deck

class Card(object):
    """Denote a single card.
    The card has a suit - 'S','C','H', 'D'
    The card has a rank A - K
    """
    
    def __init__(self, r, s):
        """
        None -> card
        Implementation of a card, where r is the rank, s is suit
        """
        self.rank = r
        self.suit = s

    def __str__(self):
        """
        None -> string
        """
        return 'Rank: ' + str(self.rank) + '; Suit: ' + str(self.suit)

    def get_rank(self):
        """
        None -> string
        Returns the rank of a card
        """
        return self.rank

    def get_suit(self):
        """
        None -> string
        Returns the suit of a card
        """
        return self.suit

class Deck(object):
    """Denote a deck to play cards with"""
     
    def __init__(self):
        """
        Initialize deck as a list of all 52 cards:
        13 cards in each of 4 suits
        """
        possSuit = ['S','C','H','D']
        possRank = ['A', '2','3','4','5','6','7','8','9', '10', 'J','Q','K']
        self.__deck = []
        for i in possSuit:
            for j in possRank:
                self.__deck.append(Card(j, i))

    def shuffle(self):
        """
        None -> Deck
        Shuffle the deck
        """
        return random.shuffle(self.__deck)

    def get_deck(self):
        """
        None -> Deck
        Returns a deck, or a list of card objects
        """
        return self.__deck

    def deal(self):
        """
        None -> Card
        Get the last card in the deck
        Simulates a pile of cards and getting the top one
        """
        if len(self.__deck) > 0:
            return self.__deck.pop()
        else:
            print "No more cards"
    
    def __str__(self):
        """
        None -> string
        Represent the whole deck as a string for printing -- very useful during code development
        """
        #the deck is a list of cards
        #this function just calls str(card) for each card in list
        # put a '\n' between them
        d = ''
        for card in self.__deck:
           d =  d + str(card) + '\n'
        return d
