from soloBlackJack import *
from cards import *
import unittest

class TestCards(unittest.TestCase):

    ## Card class tests

    def testInitialisationCard(self):
        card = Card('A', 'H')
        self.assertEqual('A', card.get_rank())
        self.assertEqual('H', card.get_suit())

    def testStringCard(self):
        card = Card('A', 'H')
        self.assertEqual('Rank: A; Suit: H', str(card))

    ## Deck class tests

    def testInitialisationDeck(self):
        deck = Deck()
        card = deck.get_deck()[0]
        self.assertEqual('A', card.get_rank())

    def testInitialisationDeck2(self):
        deck = Deck()
        card = deck.get_deck()[0]
        self.assertEqual('S', card.get_suit())

    def testInitialisationDeck3(self):
        deck = Deck()
        cards = deck.get_deck()
        self.assertEqual(52, len(cards))

    def testshuffle(self):
        deck = Deck()
        random.seed(52)
        shuffledDeck = deck.shuffle()
        card = deck.get_deck()[51]
        self.assertEqual('D', card.get_suit())

    def testshuffle2(self):
        deck = Deck()
        random.seed(52)
        shuffledDeck = deck.shuffle()
        card = deck.get_deck()[51]
        self.assertNotEqual('K', card.get_rank())


    def testshuffle1(self):
        deck = Deck()
        shuffledDeck = deck.shuffle()
        cards = deck.get_deck()
        self.assertEqual(52, len(cards))

    def testdeal(self):
        deck = Deck()
        card = deck.deal()
        self.assertEqual('K', card.get_rank())

    def testdeal(self):
        deck = Deck()
        card = deck.deal()
        self.assertEqual('D', card.get_suit())
        
    def testStringDeck(self):
        deck = Deck()
        card = deck.get_deck()[0]
        self.assertEqual('Rank: A; Suit S', str(deck))

    ## soloBlackJack class tests
    # game (ie non-scoring) tests
    # getters and validation methods tests

    def testgetTable(self):
        b = BlackJack()
        table = b.getTable()
        self.assertEqual([1, 2, 3, 4, 5], table['Row 1'])

    def testgetDiscard(self):
        b = BlackJack()
        discard = b.getDiscard()
        self.assertEqual([17, 18, 19, 20], b.getDiscard())

    def testisValidRow(self):
        b = BlackJack()
        self.assertTrue(b.isValidRow('a'))

    def testisValidInput1(self):
        b = BlackJack()
        self.assertTrue(b.isValidRow('E'))

    def testisValidRow2(self):
        b = BlackJack()
        self.assertFalse(b.isValidRow('f'))

    def testinvalidInputStatement(self):
        pass
        # Can't test print statement

    def testprintTable(self):
        pass
        # Can't test print statement

    def testisValidSlot(self):
        b = BlackJack()
        self.assertTrue(b.isValidSlot('3', [1, 2, 3, 4, 5]))

    def testisValidSlot2(self):
        b = BlackJack()
        self.assertFalse(b.isValidSlot('3', [1, 2, 'QH', 4, 5]))

    def testisValidSlot3(self):
        b = BlackJack()
        self.assertFalse(b.isValidSlot('3', [6, 7, 8, 9, 10]))

    def testisInteger(self):
        b = BlackJack()
        self.assertTrue(b.isInteger('3'))

    def testisInteger(self):
        b = BlackJack()
        self.assertFalse(b.isInteger('a'))

    def testisInteger(self):
        b = BlackJack()
        self.assertFalse(b.isInteger('3.0'))

    def testStringBlackJack(self):
        b = BlackJack()
        self.assertEquals("{'Row 1': [1, 2, 3, 4, 5], 'Row 3': [11, 12, 13], 'Row 2': [6, 7, 8, 9, 10], 'Row 4': [14, 15, 16]}\n[17, 18, 19, 20]", str(b))

    def testStringBlackJack1(self):
        b = BlackJack()
        card = Card('A', 'S')
        move = ['Row 3', 12]
        b.updateSlot(card, move)
        self.assertEquals("{'Row 1': [1, 2, 3, 4, 5], 'Row 3': [11, 'AS', 13], 'Row 2': [6, 7, 8, 9, 10], 'Row 4': [14, 15, 16]}\n[17, 18, 19, 20]", str(b))


    # update methods tests

    def testupdateSlot(self):
        b = BlackJack()
        card = Card('A', 'H')
        move = ['Row 1', 1]
        updatedTable = b.updateSlot(card, move)
        self.assertEqual(['AH', 2, 3, 4, 5], b.table['Row 1'])

    def testupdateSlot2(self):
        b = BlackJack()
        card = Card('A', 'S')
        move = ['Row 3', 12]
        updatedTable = b.updateSlot(card, move)
        self.assertEqual([11, 'AS', 13], b.table['Row 3'])

    def testupdateSlot3(self):
        b = BlackJack()
        card = Card('A', 'S')
        move = ['Row 3', 12]
        card1 = Card('K', 'D')
        move = ['Row 3', 12]
        b.updateSlot(card, move)
        self.assertEqual([11, 'AS', 13], b.table['Row 3'])

    def testupdateSlot4(self):
        b = BlackJack()
        card2 = Card('A', 'S')
        move1 = ['Row 3', 12]
        card3 = Card('K', 'D')
        move2 = ['Row 3', 13]
        b.updateSlot(card2, move1)
        b.updateSlot(card3, move2)
        self.assertEqual([11, 'AS', 'KD'], b.table['Row 3'])



    def testupdateDiscard1(self):
        b = BlackJack()
        card = Card('A', 'S')
        move = ['Discard']
        self.assertEqual(['AS', 18, 19, 20], b.updateDiscard(card, move))

    def testupdateDiscard2(self):
        b = BlackJack()
        card1 = Card('A', 'S')
        card2 = Card('K', 'S')
        card3 = Card('Q', 'S')
        card4 = Card('J', 'S')
        card5 = Card('10', 'S')
        move = ['Discard']
        b.updateDiscard(card1, move)
        b.updateDiscard(card2, move)
        b.updateDiscard(card3, move)
        b.updateDiscard(card4, move)
        self.assertEqual(['AS', 'KS', 'QS', 'JS'], b.updateDiscard(card5, move))

    def testaskUserForMove(self):
        pass
        # Can't test method with user input

    # Scoring function tests

    def testColumnsForScoring(self):
        self.playGame()

    # Helper functions

    def playGame(self):
        """
        Plays an entire game, and creates the following table:
        Row 1: ['AS', '2S', '3S', '4S', '5S']
        Row 2: ['6S', '7S', '8S', '9S', '10S']
        Row 3: ['JS', 'QS', 'KS']
        Row 4: ['AD', '2D', '3D']
        """
        b = BlackJack()
        card1 = Card('A', 'S')
        move1 = ['Row 1', 1]
        b.updateSlot(card1, move1)
        card2 = Card('2', 'S')
        move2 = ['Row 1', 2]
        b.updateSlot(card2, move2)
        card3 = Card('3', 'S')
        move3 = ['Row 1', 3]
        b.updateSlot(card3, move3)
        card4 = Card('4', 'S')
        move4 = ['Row 1', 4]
        b.updateSlot(card4, move4)
        card5 = Card('5', 'S')
        move5 = ['Row 1', 5]
        b.updateSlot(card5, move5)
        card6 = Card('6', 'S')
        move6 = ['Row 2', 6]
        b.updateSlot(card6, move6)
        card7 = Card('7', 'S')
        move7 = ['Row 2', 7]
        b.updateSlot(card7, move7)
        card8 = Card('8', 'S')
        move8 = ['Row 2', 8]
        b.updateSlot(card8, move8)
        card9 = Card('9', 'S')
        move9 = ['Row 2', 9]
        b.updateSlot(card9, move9)
        card10 = Card('10', 'S')
        move10 = ['Row 2', 10]
        b.updateSlot(card10, move10)
        card11 = Card('J', 'S')
        move11 = ['Row 3', 11]
        b.updateSlot(card11, move11)
        card12 = Card('Q', 'S')
        move12 = ['Row 3', 12]
        b.updateSlot(card12, move12)
        card13 = Card('K', 'S')
        move13 = ['Row 3', 13]
        b.updateSlot(card13, move13)
        card14 = Card('A', 'D')
        move14 = ['Row 4', 14]
        b.updateSlot(card14, move14)
        card15 = Card('2', 'D')
        move15 = ['Row 4', 15]
        b.updateSlot(card15, move15)
        card16 = Card('3', 'D')
        move16 = ['Row 4', 16]
        b.updateSlot(card16, move16)
        b.printTable()

#33333333

#aoweifjoa;weejfiewaf

unittest.main()
