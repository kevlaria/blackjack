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
unittest.main()
