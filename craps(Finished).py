"""
File: craps.py

This module studies and plays the game of craps.
"""

from die import Die

class Player(object):

    def __init__(self):
        """Has a pair of dice and an empty rolls list."""
        self.die1 = Die()
        self.die2 = Die()
        self.atStartUp = True
        self.winner = False
        self.loser = False
        self.rolls = []

    def __str__(self):
        """Returns a string representation of the list of rolls."""
        result = ""
        for (v1, v2) in self.rolls:
            result = result + str((v1, v2)) + " total = " +\
                     str(v1 + v2) + "\n"
        return result

    def lastRoll(self):
        (v1, v2) = self.rolls[-1]
        return str(str((v1, v2)) + " total = " +\
                     str(v1 + v2))
    
    def rollDice(self):
        v1 = 0
        v2 = 0
        self.die1.roll()
        self.die2.roll()
        (v1, v2) = (self.die1.getValue(),
                    self.die2.getValue())
        self.rolls.append((v1, v2))
        if self.atStartUp == True:
            initialSum = v1 + v2
            if initialSum in (2, 3, 12):
                self.loser = True
            elif initialSum in (7, 11):
                self.winner = True
        elif self.atStartUp == False:
            laterSum = v1 + v2
            if laterSum == 7:
                self.loser = True
            elif laterSum == initialSum:
                self.winner = True
        return (v1, v2)
    
    def getNumberOfRolls(self):
        """Returns the number of the rolls."""
        return len(self.rolls)

    def isWinner(self):
        return self.winner

    def isLoser(self):
        return self.loser
    
    def play(self, display = False):
        """Plays a game, saves the rolls for that game, 
        and returns True for a win and False for a loss."""
        while self.isWinner() == False and self.isLoser() == False:
            (v1, v2) = self.rollDice()
            if display == True:
                input(self.lastRoll())
        return


def playOneGame():
    """Plays a single game and prints the results."""
    player = Player()
    youWin = player.play(display = True)
    #print(player)
    if youWin:
        print("You win!")
    else:
        print("You lose!")

def playManyGames(number):
    """Plays a number of games and prints statistics."""
    if number == 1:
        playOneGame()
    else:
        wins = 0
        losses = 0
        winRolls = 0
        lossRolls = 0
        winAverage = 0
        lossAverage = 0
        for count in range(number):
            player = Player()
            hasWon = player.play()
            rolls = player.getNumberOfRolls()
            if hasWon:
                wins += 1
                winRolls += rolls
            else:
                losses += 1
                lossRolls += rolls
                winAverage = winRolls / wins if wins != 0 else 0
                lossAverage = lossRolls / losses if losses != 0 else 0
        print("The total number of wins is", wins)
        print("The total number of losses is", losses)
        print("The average number of rolls per win is %0.2f" % \
            (winAverage))
        print("The average number of rolls per loss is %0.2f" % \
            (lossAverage))
        print("The winning percentage is %0.3f" % ((wins / number) * 100))

def main():
    """Plays a number of games and prints statistics."""
    number = int(input("Enter the number of games: "))
    playManyGames(number)

if __name__ == "__main__":
    main()