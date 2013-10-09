from cards import *

class BlackJack(object):
    
    def __init__(self):
        """
        None -> BlackJack
        Denotes a single BlackJack game
        """
        self.discard = [17,18,19,20]
        self.table = {'Row 1':[1,2,3,4,5], 'Row 2':[6,7,8,9,10], 'Row 3':[11,12,13], 'Row 4': [14,15,16]}

    # Game Scoring methods

    def scoreGame(self, table):
        '''Uses the scoring functions which score both the row and column hands,
        and returns a total score.''' 
        columns = self.getColumnsForScoring(table)
        columnsScore = self.scoreColumns(columns)
        rowScore = self.scoreRows(table)
        return (columnsScore + rowScore)

    def scoreRows(self, table):
        '''Returns the score from the rows of the game.'''
        #here we reformat the dictionary to represent only the card's rank
        for key in table:
            cardIndex = 0
            for card in table[key]:
                table[key][cardIndex] = card[:-1]
                cardIndex += 1
        #here we tally each hand and eventually return a total row score
        totalRowScore = 0
        intList = ['3','4','5','6','7','8','9', '10']
        for row in table.values():
            aceExistsInRow = False
            handSum = 0
            for card in row:
                if card in intList:
                    handSum += int(card)
                elif card == 'J' or card == 'Q' or card == 'K':
                    handSum += 10
                else:
                    handSum += 1
                    aceExistsInRow = True
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
                handScore = 7
            totalRowScore += handScore
        return totalRowScore

    def scoreColumns(self, columns):
        '''Takes in the columns list of lists and scores the columns.'''
        totalColumnScore = 0
        intList = ['3','4','5','6','7','8','9', '10']
        for column in columns:
            #we keep track of the number of cards in the hand that we're scoring in case there is a blackjack scenario
            numOfCardsInColumn = 0
            aceExistsInRow = False
            handSum = 0
            for card in column:
                if card in intList:
                    handSum += int(card)
                elif card == 'J' or card == 'Q' or card == 'K':
                    handSum += 10
                else:
                    handSum += 1
                    aceExistsInRow = True
                numOfCardsInColumn += 1
            #here we check to see that if there was an ace present in the column, should we make it an 11 rather than 1
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
                #checks for blackjack here
                if numOfCardsInColumn == 2:
                    handScore = 10
                else:
                    handScore = 7
            totalColumnScore += handScore
        return totalColumnScore
                
    def getColumnsForScoring(self, table):
        '''Takes the table and returns a list of lists that
        represent the columns of the game (rank only - for scoring purposes).'''
        columns = []
        c1 = []
        c1.append(table['Row 1'][0][:-1])
        c1.append(table['Row 2'][0][:-1])
        columns += [c1]
        c2 = []
        c2.append(table['Row 1'][-1][:-1])
        c2.append(table['Row 2'][-1][:-1])
        columns += [c2]
        c3 = []
        c3.append(table['Row 1'][1][:-1])
        c3.append(table['Row 2'][1][:-1])
        c3.append(table['Row 3'][0][:-1])
        c3.append(table['Row 4'][0][:-1])
        columns += [c3]
        c4 = []
        c4.append(table['Row 1'][2][:-1])
        c4.append(table['Row 2'][2][:-1])
        c4.append(table['Row 3'][1][:-1])
        c4.append(table['Row 4'][1][:-1])
        columns += [c4]
        c5 = []
        c5.append(table['Row 1'][3][:-1])
        c5.append(table['Row 2'][3][:-1])
        c5.append(table['Row 3'][2][:-1])
        c5.append(table['Row 4'][2][:-1])
        columns += [c5]
        return columns

    # Game Playing methods

    def play(self): 
        table = self.getTable()
        print "Table: " + str(table)
        discard = self.getDiscard()
        print "Discard slots: " + str(discard)
##        self.initializeGame()
        print
        print 'You have been dealt:'
        deck = Deck()
        complete = False
        while not complete:
            #TODO Priority Low - should we shuffle the cards every time we loop?
            deck.shuffle()
            card = deck.deal()
            print card
            print
            move = self.askUserForMove()
            self.placeMove(card, move)
            print
            print "Table: " + str(table)
            print "Discard slots: " + str(discard)
            complete = self.checkIfGameComplete()
        finalScore = self.scoreGame(table)
        print 'Your final score is: ', finalScore

    def __str__(self):
        """
        None -> Str
        """
        return str(self.table) + '\n' + str(self.discard)

    def placeMove(self, card, move):
        if move == ['discard']:
            updatedDiscard = self.updateDiscard(card, move)
            return updatedDiscard
        else:
            updatedTable = self.updateSlot(card, move)
            return updatedTable

    
    def updateSlot(self, card, move):
        """
        Card, List[string, int] -> Table
        Takes a Card and a Move[row, slot] and updates the table
        """
        inputRow = move[0]
        inputSlot = move[1]
        tableRow = self.table[inputRow]
        if inputSlot in tableRow:
            rowIndex = tableRow.index(inputSlot)
            tableRow[rowIndex] = card.rank + card.suit
            self.table[inputRow] = tableRow
        else:
            inputText = str(inputRow) + ", Slot " + str(inputSlot)
            self.invalidInputStatement(inputText)
        return self.table

    def updateDiscard(self, card, move):
        """
        Card, List[string, int] -> 
        Takes a card and puts it in the discard pile
        """
        i = -1
        discard = self.getDiscard()
        for slotIndex in range(len(discard) + 1):
            i = i+1
            if i >= len(discard):
                print 'No more discard slots available!'
                return self.discard
            elif type(discard[slotIndex]) == int:
                discard[slotIndex] = card.rank + card.suit
                print 'Your card has been discarded.'
                self.discard = discard
                return self.discard
            

##    def initializeGame(self):

    def checkIfGameComplete(self):
        for lst in self.table.values():
            for slot in lst:
                if type(slot) == int:
                    print
                    print 'Not done!'
                    return False
        print
        print 'Done!'
        return True




    def askUserForMove(self):
        placement = []
        userPrompt = '''Which row would you like to place this card in, (enter a, b, c, d, or e)?:
        a) Row 1
        b) Row 2
        c) Row 3
        d) Row 4
        e) Discard
        '''
        inp1 = raw_input(userPrompt)
        while not self.isValidRow(inp1):
            self.invalidInputStatement(inp1)
            inp1 = raw_input(userPrompt)
        if inp1 == 'a':
            row = 'Row 1'
            slots = self.table[row]
        elif inp1 == 'b':
            row = 'Row 2'
            slots = self.table[row]
        elif inp1 == 'c':
            slots = self.table[row]
            row = 'Row 3'
        elif inp1 == 'd':
            row = 'Row 4'
            slots = self.table[row]
        elif inp1 == 'e':
            placement = ['discard']
            return placement
            
        print 'You may place this card in slots: ' + str(slots)
        slot = raw_input('''In which slot would you like to place this card?: ''')
        while not self.isValidSlot(slot, slots):
            self.invalidInputStatement(slot)
            print '\nYou may place this card in slots: ' + str(slots)
            slot = raw_input('''In which slot would you like to place this card?: ''')
        print 'Your card will be placed in ' + str(row) + ' slot ' + str(slot)
        placement = [row,int(slot)]
        return placement


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

    def isString(self, text):
        """
        Any type -> boolean
        Takes an input and returns True if the input is a string
        """
        text = text.strip()
        if text == '':
            return False
        else:
            return True

    def invalidInputStatement(self, inputText):
        """
        None -> None
        Prints invalid input text
        """
        print "\nYour input, '" + inputText + "', was invalid. Please re-enter."

def main():
    print 'Welcome to the game!'
    b = BlackJack()
    status = b.play()
    while status == False:
        b.play()

    
