from cards import *

## Methods listing
# Game Playing methods
# Scoring Methods
# Get and set methods
# Validation Methods
# Print Methods

class BlackJack(object):
 
    def __init__(self):
        """
        None -> BlackJack
        Denotes a single BlackJack game
        """
        self.discard = [17,18,19,20]
        self.table = {'Row 1':[1,2,3,4,5], 'Row 2':[6,7,8,9,10], 'Row 3':[11,12,13], 'Row 4': [14,15,16]}


    # Game Playing methods


    def play(self): 
        """
        None -> None
        Runs the game from beginning to end (by displaying final score)
        """
        print '\n*************************************'
        self.printTable()
        print '\n'
        self.printDiscardSlots()
        print '\n'
        deck = Deck()
        complete = False
        while not complete:
            #TODO Priority Low - should we shuffle the cards every time we loop?
            deck.shuffle()
            card = deck.deal()
            print '\n*************************************'
            print '\nYou have been dealt: ' + str(card) + '\n'
            move = self.askUserForMove()
            self.placeMove(card, move)
            print '\n*************************************'
            self.printTable()
            print '\n'
            self.printDiscardSlots()
            print '\n'
            complete = self.checkIfGameComplete()
        finalScore = self.scoreGame()
        print 'Your final score is: ', finalScore


    def askUserForMove(self):
        """
        None -> List[string] or List[string, int]
        Prompts user for input, and returns the row name and the slot. Returns 'discard' if user selects 'Discard'.
        """

        placement = []
        userPrompt = """Which row would you like to place this card in, (enter a, b, c, d, or e)?:\n\ta) Row 1\n\tb) Row 2\n\tc) Row 3\n\td) Row 4\n\te) Discard\nYour entry: """

        inp1 = raw_input(userPrompt)
        while not self.isValidRow(inp1):
            self.invalidInputStatement(inp1)
            inp1 = raw_input(userPrompt)
        rowSlots = self.parseRowInput(inp1)
        row = rowSlots[0]
        slots = rowSlots[1]
        if row == 'InvalidMove':
            return self.askUserForMove()
        if row == 'discard':
            placement = ['discard']
            return placement

        print '\nYou may place this card in slots: ' + str(self.availableSlots(row))
        slot = raw_input('''In which slot would you like to place this card?: ''')
        
        while not self.isValidSlot(slot, slots):
            self.invalidInputStatement(slot)
            return self.askUserForMove()
            
        print '\nYour card will be placed in ' + str(row) + ', Slot ' + str(slot)
        placement = [row,int(slot)]
        return placement


    def parseRowInput(self, inp1):
        """
        String -> Tuple(String, List[Int,...])
        Given an input, check for validity, and return the Row.
        """
        table = self.getTable()
        inp1 = inp1.lower()
        if inp1 == 'a':
            row = 'Row 1'
            slots = table[row]
        elif inp1 == 'b':
            row = 'Row 2'
            slots = table[row]
        elif inp1 == 'c':
            row = 'Row 3'
            slots = table[row]
        elif inp1 == 'd':
            row = 'Row 4'
            slots = table[row]
        elif inp1 == 'e':
            if self.availableDiscard() == 'rowIsFull':
                print 'Sorry, but you have no more discard slots.\n'
                return ('InvalidMove', [])
            else:
                return ('discard', [])
        if self.availableSlots(row) == 'rowIsFull':
            print 'Sorry, but this row is full.\n'
            return ('InvalidMove', [])
        return (row, slots)


    def placeMove(self, card, move):
        if move == ['discard']:
            updatedDiscard = self.updateDiscard(card)
            return updatedDiscard
        else:
            updatedTable = self.updateSlot(card, move)
            return updatedTable


    def updateDiscard(self, card):
        """
        Card -> Discard 
        Takes a card and puts it in the next available slot (ie unoccupied) in the discard pile
        """
        discard = self.getDiscard()
        for slotIndex in range(len(discard)):
            if type(discard[slotIndex]) == int:
                discard = self.setDiscard(discard, card, slotIndex)
                print '\nYour card has been discarded.'
                return discard

    
    def updateSlot(self, card, move):
        """
        Card, List[string, int] -> Table
        Takes a Card and a Move[row, slot] and updates the table
        """
        table = self.getTable()
        inputRow = move[0]
        inputSlot = move[1]
        tableRow = table[inputRow]
        if inputSlot in tableRow:
            table = self.setTable(table, card, inputRow, inputSlot)
            return table
        else:
            inputText = str(inputRow) + ", Slot " + str(inputSlot)
            self.invalidInputStatement(inputText)
        return table


    def availableSlots(self, row):
        """
        String -> String / List
        Takes in a row name, and either returns a list of the slots that are available, or a string indicating that the row is full
        """
        table = self.getTable()
        slotsInRow = table[row]
        slotsAvailable = self.slotChecker(slotsInRow)
        return slotsAvailable


    def availableDiscard(self):
        """
        None -> Boolean
        Checks if discard row is full or not. If full, returns False, otherwise returns True
        """
        discard = self.getDiscard()
        discardAvaialble = []
        slotsAvailable = self.slotChecker(discard)
        return slotsAvailable


    def slotChecker(self, slotsInRow):
        """
        List[Int,...] -> String / List
        Given a list of slots, checks if there are free slots in a row. If not full, returns a list of the slots that are avialable, or a string indicating that the row is full
        """
        slotsAvailable = []
        for slot in slotsInRow:
            if type(slot) == int:
                slotsAvailable.append(slot)
        if slotsAvailable == []:
            return 'rowIsFull'
        return slotsAvailable


    def checkIfGameComplete(self):
        """
        None -> Boolean
        Loops through the table to see if there are any empty slots available (represented by integers on the table). Returns True if there are no more integers on the table.
        """
        table = self.getTable()
        for rows in table.values():
            for slot in rows:
                if type(slot) == int:
                    return False
        return True


    #scoring methods
        
    def scoreGame(self):
        '''
        None -> Int
        Uses the scoring functions which score both the row and column hands,
        and returns a total score.
        '''
        table = self.getTable()
        rowsScore = self.scoreRows(table)
        columns = self.getColumnsForScoring(table)
        columnsScore = self.scoreColumns(columns)
        totalScore = columnsScore + rowsScore
        return totalScore


    def scoreRows(self, table):
        '''
        Table -> Integer
        Returns the score from all the rows of the game.
        '''
        #here we tally each row and eventually return a total row score
        totalRowScore = 0
        for row in table.values():
            handScore = self.scoreSingleList(row)
            totalRowScore += handScore
        return totalRowScore


    def scoreSingleList(self, rowOfCards):
        """
        List[Cards,...] -> Row
        Given a row of cards, give the score of a single row
        """
        cardsInRow = len(rowOfCards)
        rankList = self.getRanksInList(rowOfCards)
        handSum = self.sumList(rankList)
        aceExistsInRow = self.isAceInList(rankList)
        handScore = self.listScore(handSum, aceExistsInRow, cardsInRow)
        return handScore


    def getRanksInList(self, cards):
        """
        Cards -> List[Int,...]
        For a list of cards, extract their ranks and return the ranks in a list of integers. J, Q and K are converted into '10', 'A' is converted into '1'
        """
        ranks = []
        for card in cards:
            rank = card.get_rank()
            if rank == 'A':
                rank = '1'
            if rank == 'J' or rank == 'Q' or rank == 'K':
                rank = '10'
            rankInt = int(rank)
            ranks.append(rankInt)
        return ranks


    def sumList(self, rankList):
        """
        List[Int,...], Int
        Takes a list of ranks, and returns the sum of the ranks
        """
        return sum(rankList)


    def isAceInList(self, ranks):
        """
        List[int,...] --> Boolean
        Given a list of ranks, returns True if an Ace (represented as '1') is in the list. Else returns false
        """
        if 1 in ranks:
            return True
        return False

            
    def listScore(self, handSum, aceExistsInRow, cardsInRow):
        """
        Int -> Int
        Takes in a sum of a list of cards, and returns the score
        """
        handScore = 0
        #here we check to see that if there was an ace present in the row, should we make it an 11 rather than 1
        #if so, we add 10, as 1 was already added
        if handSum < 12 and aceExistsInRow:
                handSum += 10
        #Here we score each individual hand
        if handSum > 21:
            handScore = 0
        elif handSum < 17:
            handScore = 1
        elif handSum == 17:
            handScore = 2
        elif handSum == 18:
            handScore = 3
        elif handSum == 19:
            handScore = 4
        elif handSum == 20:
            handScore = 5
        elif handSum == 21:
            if cardsInRow == 2:
                handScore = 10
            else:
                handScore = 7
        return handScore


    def getColumnsForScoring(self, table):
        '''
        None -> List[List[Card]]
        Takes the table and returns a list of lists of Card objects that
        represent the columns of the game
        '''
        columns = []
        c1 = [] #Leftmost column
        c1.append(table['Row 1'][0])
        c1.append(table['Row 2'][0])
        columns += [c1]
        c2 = [] #Rightmost column
        c2.append(table['Row 1'][-1])
        c2.append(table['Row 2'][-1])
        columns += [c2]
        c3 = [] #2nd leftmost column
        c3.append(table['Row 1'][1])
        c3.append(table['Row 2'][1])
        c3.append(table['Row 3'][0])
        c3.append(table['Row 4'][0])
        columns += [c3]
        c4 = [] #Middle column
        c4.append(table['Row 1'][2])
        c4.append(table['Row 2'][2])
        c4.append(table['Row 3'][1])
        c4.append(table['Row 4'][1])
        columns += [c4]
        c5 = [] #2nd rightmost column
        c5.append(table['Row 1'][3])
        c5.append(table['Row 2'][3])
        c5.append(table['Row 3'][2])
        c5.append(table['Row 4'][2])
        columns += [c5]
        return columns


    def scoreColumns(self, columns):
        """
        List[Cards,..] -> Int
        Takes in a list of cards (from the columns of the table) and returns the total score for all columns
        """
        totalColumnScore = 0
        for column in columns:
            handScore = self.scoreSingleList(column)
            totalColumnScore += handScore
        return totalColumnScore

    # Get and set methods

    def getTable(self):
        """
        None -> Table
        Returns the current table
        """
        return self.table


    def getDiscard(self):
        """
        None -> Discard
        Returns the current discard list
        """
        return self.discard


    def setTable(self, table, card, row, slot):
        """
        Table, Card, string, int -> Table
        Updates the table given a card, a row and a slot
        """
        tableRow = table[row]
        rowIndex = tableRow.index(slot)
        tableRow[rowIndex] = card
        return table


    def setDiscard(self, discard, card, slotIndex):
        """
        Updates the discard list, given a card and a slotIndex
        """
        discard[slotIndex] = card
        return discard
    

    # Data validation methods


    def isValidRow(self, text):
        """
        String -> Boolean
        Returns true only if text is a, b, c, d or e
        """
        text = text.strip()
        text = text.lower()
        valid_inputs = ['a', 'b', 'c', 'd', 'e']
        if not text in valid_inputs:
            return False
        return True


    def isValidSlot(self, text, slots):
        """
        String, List[String,...]
        Takes an input and returns True only if the input is valid (is an integer and is a valid slot)
        """
        if not self.isInteger(text):
            return False
        number = int(text)
        if not number in slots:
            return False
        return True


    def isInteger(self,text):
        """
        Any type -> Bool
        Takes an input and returns True only if the input is a valid integer
        """
        text = text.strip()
        dot = text.find('.')
        if dot > -1:
            return False
        try:
            int(text)
            return True
        except:
            return False


    # Printing methods


    def invalidInputStatement(self, inputText):
        """
        None -> None
        Prints invalid input text
        """
        print "\nYour input, '" + inputText + "', was invalid. Please re-enter.\n"


    def printTable(self):
       """
       None -> None
       Prints table
       """
       table = self.getTable()
       print '\nTable: '
       rows = ['Row 1', 'Row 2', 'Row 3', 'Row 4']
       for row in rows:
           print
           print '[' + str(row) + ']',
           if row == 'Row 3' or row == 'Row 4':
               print '     ',
           for slot in table[row]:
               if len(str(slot)) == 2:
                   print str(slot) + '   ',
               elif len(str(slot)) == 3:
                   print str(slot) + '  ',
               else:
                   print str(slot) + '    ',


    def printDiscardSlots(self):
        discardList = self.getDiscard()
        print "Discard Slots: \n\n\t",
        for card in discardList:
            print str(card) + '\t',


    def __str__(self):
        """
        None -> Str
        """
        return str(self.table) + '\n' + str(self.discard)


def main():
    print 'Welcome to the game!'
    b = BlackJack()
    status = b.play()
    while status == False:
        b.play()

 
