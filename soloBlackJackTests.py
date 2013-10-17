# Vincent Inverso, Kevin Lee

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
        self.assertEqual('AH', str(card))

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
        self.assertEqual('AS\n2S\n3S\n4S\n5S\n6S\n7S\n8S\n9S\n10S\nJS\nQS\nKS\nAC\n2C\n3C\n4C\n5C\n6C\n7C\n8C\n9C\n10C\nJC\nQC\nKC\nAH\n2H\n3H\n4H\n5H\n6H\n7H\n8H\n9H\n10H\nJH\nQH\nKH\nAD\n2D\n3D\n4D\n5D\n6D\n7D\n8D\n9D\n10D\nJD\nQD\nKD\n', str(deck))

    ## soloBlackJack class tests
    # game (ie non-scoring) tests

    def testmain(self):
        pass
        # Can't test method that returns nothing

    def testinitializeGame(self):
        pass
        # Can't test method that returns nothing

    def testplay(self):
        pass
        # Can't test method that returns nothing

    # update methods tests

    def testplaceMove(self):
        b = BlackJack()
        card = Card('A', 'H')
        move = ['Row 1', 1]
        b.placeMove(card, move)
        table = b.getTable()
        self.assertEqual(card, table['Row 1'][0])

    def testplaceMove2(self):
        b = BlackJack()
        card = Card('A', 'H')
        move = ['discard']
        b.placeMove(card, move)
        discard = b.getDiscard()
        self.assertEqual(card, discard[0])

    def testupdateSlot(self):
        b = BlackJack()
        card = Card('A', 'H')
        move = ['Row 1', 1]
        b.updateSlot(card, move)
        self.assertEqual([card, 2, 3, 4, 5], b.table['Row 1'])

    def testupdateSlot2(self):
        b = BlackJack()
        card = Card('A', 'S')
        move = ['Row 3', 12]
        b.updateSlot(card, move)
        self.assertEqual([11, card, 13], b.table['Row 3'])

    def testupdateSlot3(self):
        b = BlackJack()
        card = Card('A', 'S')
        move = ['Row 3', 12]
        card1 = Card('K', 'D')
        move = ['Row 3', 12]
        b.updateSlot(card, move)
        self.assertEqual([11, card, 13], b.table['Row 3'])

    def testupdateSlot4(self):
        b = BlackJack()
        card2 = Card('A', 'S')
        move1 = ['Row 3', 12]
        card3 = Card('K', 'D')
        move2 = ['Row 3', 13]
        b.updateSlot(card2, move1)
        b.updateSlot(card3, move2)
        self.assertEqual([11, card2, card3], b.table['Row 3'])


    def testupdateDiscard1(self):
        b = BlackJack()
        card = Card('A', 'S')
        self.assertEqual([card, 18, 19, 20], b.updateDiscard(card))

    def testupdateDiscard2(self):
        b = BlackJack()
        card1 = Card('A', 'S')
        card2 = Card('K', 'S')
        card3 = Card('Q', 'S')
        card4 = Card('J', 'S')
        card5 = Card('10', 'S')
        b.updateDiscard(card1)
        b.updateDiscard(card2)
        b.updateDiscard(card3)
        self.assertEqual([card1, card2, card3, card4], b.updateDiscard(card4))
        self.assertEqual(None, b.updateDiscard(card5))

    def testavailableDiscard(self):
        b = BlackJack()
        self.assertEqual([17, 18, 19, 20], b.availableDiscard())
        
    def testavailableDiscard2(self):
        b = BlackJack()
        card = Card('A', 'S')
        b.updateDiscard(card)
        self.assertEqual([18, 19, 20], b.availableDiscard())

    def testavailableDiscard3(self):
        b = BlackJack()
        card1 = Card('A', 'S')
        card2 = Card('K', 'S')
        card3 = Card('Q', 'S')
        card4 = Card('J', 'S')
        card5 = Card('10', 'S')
        b.updateDiscard(card1)
        b.updateDiscard(card2)
        b.updateDiscard(card3)
        b.updateDiscard(card4)
        self.assertEqual('rowIsFull', b.availableDiscard())

    def testslotChecker(self):
        b = BlackJack() 
        card1 = Card('A', 'S')
        slotsInRow = [1, 2, 3, card1]
        self.assertEqual([1, 2, 3], b.slotChecker(slotsInRow))

    def testslotChecker2(self):
        b = BlackJack() 
        card1 = Card('A', 'S')
        card2 = Card('K', 'S')
        slotsInRow = [card1, card2]
        self.assertEqual('rowIsFull', b.slotChecker(slotsInRow))


    def testparseRowInput(self):
        b = BlackJack()
        self.assertEqual(('Row 1', [1, 2, 3, 4, 5]), b.parseRowInput('a'))
        self.assertEqual(('Row 1', [1, 2, 3, 4, 5]), b.parseRowInput('A'))
        self.assertEqual(('discard', []), b.parseRowInput('e'))

    def testparseRowInput2(self):
        b = BlackJack()
        card1 = Card('A', 'S')
        card2 = Card('K', 'S')
        card3 = Card('Q', 'S')
        card4 = Card('J', 'S')
        card5 = Card('10', 'S')
        b.updateDiscard(card1)
        b.updateDiscard(card2)
        b.updateDiscard(card3)
        b.updateDiscard(card4)
        b.updateDiscard(card5)
        self.assertEqual(('InvalidMove', []), b.parseRowInput('e'))

    def testparseRowInput3(self):
        b = BlackJack()
        card1 = Card('A', 'S')
        card2 = Card('K', 'S')
        card3 = Card('Q', 'S')
        b.placeMove(card1, ['Row 3', 11])
        b.placeMove(card2, ['Row 3', 12])
        b.placeMove(card3, ['Row 3', 13])
        self.assertEqual(('InvalidMove', []), b.parseRowInput('c'))

    def testaskUserForMove(self):
        pass
        # Can't test method with user input

    def testavailableSlots(self):
        table = self.playGame()
        self.assertEqual('rowIsFull', table.availableSlots('Row 1'))

    def testavailableSlots2(self):
        b = BlackJack()
        self.assertEqual([1, 2, 3, 4, 5], b.availableSlots('Row 1'))

    def testavailableSlots3(self):
        b = BlackJack()
        card = Card('A', 'S')
        move = ['Row 1', 1]
        b.updateSlot(card, move)
        self.assertEqual([2, 3, 4, 5], b.availableSlots('Row 1'))

    def testcheckIfGameComplete(self):
        game = self.playGame()
        self.assertTrue(game.checkIfGameComplete())

    def testcheckIfGameComplete2(self):
        b = BlackJack()
        card = Card('A', 'H')
        move = ['Row 1', 1]
        b.updateSlot(card, move)
        self.assertFalse(b.checkIfGameComplete())

    # Scoring methods tests

    def testgetColumnsForScoring(self):
        game = self.playGame()
        columns = game.getColumnsForScoring()
        self.assertEqual('A', columns[0][0].get_rank())
        self.assertEqual('10', columns[1][1].get_rank())
        self.assertEqual('2', columns[3][3].get_rank())

    def testgetRanksInList(self):
        game = self.playGame()
        table = game.getTable()
        cards = table['Row 1']
        cards2 = table['Row 3']
        self.assertEqual([1, 2, 3, 4, 5], game.getRanksInList(cards))
        self.assertEqual([10, 10, 10], game.getRanksInList(cards2))

    def testisAceInList(self):
        b = BlackJack()
        self.assertTrue(b.isAceInList([3, 4, 1]))
        self.assertFalse(b.isAceInList([4, 5, 6]))

    def testsumList(self):
        b = BlackJack()
        self.assertEqual(30, b.sumList([10, 10, 10]))
        self.assertEqual(11, b.sumList([10, 1]))
        self.assertEqual(30, b.sumList([5, 10, 15]))

    def testlistScore(self):
        b = BlackJack()
        self.assertEqual(7, b.listScore(21, False, 3))
        self.assertEqual(5, b.listScore(20, False, 3))
        self.assertEqual(4, b.listScore(19, False, 4))
        self.assertEqual(3, b.listScore(18, False, 5))
        self.assertEqual(2, b.listScore(17, False, 3))
        self.assertEqual(1, b.listScore(16, False, 3))
        self.assertEqual(1, b.listScore(3, False, 2))
        self.assertEqual(0, b.listScore(22, False, 4))
        #Scenarios with Aces
        self.assertEqual(7, b.listScore(11, True, 3))
        self.assertEqual(2, b.listScore(7, True, 2))
        self.assertEqual(1, b.listScore(5, True, 4))
        self.assertEqual(1, b.listScore(12, True, 2))
        self.assertEqual(0, b.listScore(22, True, 4))
        #BlackJack scenario
        self.assertEqual(10, b.listScore(11, True, 2))

    def testscoreSingleList(self):
        b = BlackJack()
        card1 = Card('7', 'S')
        card2 = Card('2', 'S')
        card3 = Card('3', 'S')
        card4 = Card('8', 'S')
        card5 = Card('A', 'C')
        self.assertEqual(7, b.scoreSingleList([card1, card2, card3, card4, card5]))

    def testscoreSingleList2(self):
        b = BlackJack()
        card1 = Card('A', 'S')
        card2 = Card('K', 'S')
        self.assertEqual(10, b.scoreSingleList([card1, card2]))


    def testscoreRows(self):
        game = self.playGame()
        self.assertEqual(2, game.scoreRows())

    def testscoreRows(self):
        game = self.playGame2()
        self.assertEqual(22, game.scoreRows())

    def testscoreRows3(self):
        game = self.playGame3()
        self.assertEqual(9, game.scoreRows())

    def testscoreColumns(self):
        game = self.playGame()
        columns = game.getColumnsForScoring()
        self.assertEqual(8, game.scoreColumns(columns))

    def testscoreColumns2(self):
        game = self.playGame2()
        columns = game.getColumnsForScoring()
        self.assertEqual(18, game.scoreColumns(columns))

    def testscoreColumns3(self):
        game = self.playGame3()
        columns = game.getColumnsForScoring()
        self.assertEqual(31, game.scoreColumns(columns))


    def testscoreGame(self):
        game = self.playGame()
        self.assertEqual(8 + 2, game.scoreGame())

    def testscoreGame2(self):
        game = self.playGame2()
        self.assertEqual(18 + 22, game.scoreGame())

    def testscoreGame3(self):
        game = self.playGame3()
        self.assertEqual(31 + 9, game.scoreGame())


    # Validation methods tests

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

    def testprintDiscard(self):
        pass
        #Can't test print statement

    def testdisplayTable(self):
        pass
        #Can't test print statement

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


    # Get and Set method tests

    def testgetTable(self):
        b = BlackJack()
        table = b.getTable()
        self.assertEqual([1, 2, 3, 4, 5], table['Row 1'])

    def testgetDiscard(self):
        b = BlackJack()
        discard = b.getDiscard()
        self.assertEqual([17, 18, 19, 20], b.getDiscard())

    def testsetTable(self):
        b = BlackJack()
        table = b.getTable()
        card = Card('A', 'S')
        row = 'Row 3'
        slot = 12
        b.setTable(table, card, row, slot)
        self.assertEqual('S', table['Row 3'][1].get_suit())


    def testsetDiscard(self):
        b = BlackJack()
        discard = b.getDiscard()
        card = Card('A', 'S')
        slotIndex = 0
        self.assertEqual([card, 18, 19, 20], b.setDiscard(discard, card, slotIndex))


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
        return b

    def playGame2(self):
        """
        Plays an entire game, and creates the following table:
        Row 1: ['7S', '2S', '3S', '8S', 'AC']
        Row 2: ['2H', '2C', '3H', '4H', '10S']
        Row 3: ['AS', '5H', '5D']
        Row 4: ['AD', '2D', '3D']
        """
        b = BlackJack()
        card1 = Card('7', 'S')
        move1 = ['Row 1', 1]
        b.updateSlot(card1, move1)
        card2 = Card('2', 'S')
        move2 = ['Row 1', 2]
        b.updateSlot(card2, move2)
        card3 = Card('3', 'S')
        move3 = ['Row 1', 3]
        b.updateSlot(card3, move3)
        card4 = Card('8', 'S')
        move4 = ['Row 1', 4]
        b.updateSlot(card4, move4)
        card5 = Card('A', 'C')
        move5 = ['Row 1', 5]
        b.updateSlot(card5, move5)
        card6 = Card('2', 'H')
        move6 = ['Row 2', 6]
        b.updateSlot(card6, move6)
        card7 = Card('2', 'C')
        move7 = ['Row 2', 7]
        b.updateSlot(card7, move7)
        card8 = Card('3', 'H')
        move8 = ['Row 2', 8]
        b.updateSlot(card8, move8)
        card9 = Card('4', 'H')
        move9 = ['Row 2', 9]
        b.updateSlot(card9, move9)
        card10 = Card('10', 'S')
        move10 = ['Row 2', 10]
        b.updateSlot(card10, move10)
        card11 = Card('A', 'S')
        move11 = ['Row 3', 11]
        b.updateSlot(card11, move11)
        card12 = Card('5', 'H')
        move12 = ['Row 3', 12]
        b.updateSlot(card12, move12)
        card13 = Card('5', 'D')
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
        return b

    def playGame3(self):
        """
        Plays an entire game, and creates the following table:
        Row 1: ['AH', '2S', '3S', '8S', 'AC']
        Row 2: ['KH', '10C', 'QH', '4H', '10S']
        Row 3: ['AS', '5H', '5D']
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
        card4 = Card('8', 'S')
        move4 = ['Row 1', 4]
        b.updateSlot(card4, move4)
        card5 = Card('A', 'C')
        move5 = ['Row 1', 5]
        b.updateSlot(card5, move5)
        card6 = Card('K', 'H')
        move6 = ['Row 2', 6]
        b.updateSlot(card6, move6)
        card7 = Card('10', 'C')
        move7 = ['Row 2', 7]
        b.updateSlot(card7, move7)
        card8 = Card('Q', 'H')
        move8 = ['Row 2', 8]
        b.updateSlot(card8, move8)
        card9 = Card('4', 'H')
        move9 = ['Row 2', 9]
        b.updateSlot(card9, move9)
        card10 = Card('10', 'S')
        move10 = ['Row 2', 10]
        b.updateSlot(card10, move10)
        card11 = Card('A', 'S')
        move11 = ['Row 3', 11]
        b.updateSlot(card11, move11)
        card12 = Card('5', 'H')
        move12 = ['Row 3', 12]
        b.updateSlot(card12, move12)
        card13 = Card('5', 'D')
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
        return b


unittest.main()
