from cards import *

class BlackJack(object):
    
    def __init__(self):
        """
        None -> BlackJack
        Denotes a single BlackJack game
        """
        self.discard = [17,18,19,20]
        self.table = {'Row 1':[1,2,3,4,5], 'Row 2':[6,7,8,9,10], 'Row 3':[11,12,13], 'Row 4': [14,15,16]}

    def main():
        print 'Welcome to the game!'
        b = BlackJack()
        status = b.play()
        while status == False:
            b.play()

    def play(self): 
        # print
        table = self.getTable()
        print "Table: " + str(table)
        discard = self.getDiscard()
        print "Discard slots: " + str(discard)
##        self.initializeGame()
        print
        print 'You have been dealt:'
        deck = Deck()
        deck.shuffle()
        card = deck.deal()
        print card
        print
        move = self.askUserForMove()
        self.placeMove(card, move)
        return self.checkIfGameComplete()

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
            print self.invalidInputStatement(inputText)
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
        while not self.isValidInput(inp1):
            print self.invalidInputStatement(inp1)
            inp1 = raw_input(userPrompt)
        if inp1 == 'a':
            row = 'Row 1'
            slots = [1,2,3,4,5]
        elif inp1 == 'b':
            row = 'Row 2'
            slots = [6,7,8,9,10]
        elif inp1 == 'c':
            slots = [11,12,13]
            row = 'Row 3'
        elif inp1 == 'd':
            row = 'Row 4'
            slots = [14,15,16]
        elif inp1 == 'e':
            placement = ['discard']
            return placement
            
        print 'You may place this card in slots: ' + str(slots)
        slot = raw_input('''In which slot would you like to place this card?: ''')

        print 'Your card will be placed in ' + str(row) + ' slot ' + str(slot)
        placement = [row,int(slot)]
        return placement

        ##    def checkIfGameComplete(self):


        
        ##        self.checkIfGameComplete()
        #        '''(h) repeat steps 4 through 7 until the game is actually complete.
        #        (i) scoreGame
        #        (j) print some message saying the game is done'''

    # get methods

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
    def isValidInput(self, text):
        """
        Any type -> Boolean
        Takes an input and returns True only if the input is valid (a, b, c, d, or e)
        """
        text = text.strip()
        text = text.lower()
        valid_inputs = ['a', 'b', 'c', 'd', 'e']
        if not text in valid_inputs:
            return False
        return True

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
        print "'\nYour input, '" + inputText + "', was invalid. Please re-enter."


    
