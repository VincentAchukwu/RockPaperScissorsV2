# Rock, Paper, Scissors game

import random, time

class RPS(object):
    """docstring for RPS"""
    def __init__(self):
        
        # listing the combinations of wins, draws, and losses with corresponding messages
        self.userWin = {
            "rs": "Rock beats Scissors!",
            "pr": "Paper beats Rock!",
            "sp": "Scissors beats Paper!",
        }
        self.draw = {
            "rr": "Rock equals Rock!",
            "pp": "Paper equals Paper!",
            "ss": "Scissors equals Scissors!",
        }
        self.userLose = {
            "rp": "Rock loses to Paper!",
            "ps": "Paper loses to Scissors!",
            "sr": "Scissors loses to Rock!"
        }

    def getScoreLimit(self):

        userIn = input("First to how many wins?: ")   # user chooses how many games to play / score limit

        # this loop runs only while the user inputs a non numeric character(s)
        # PROBLEM: WHAT IF USER INPUTS ALPHANUMERIC CHARACTERS
        while userIn.isalpha():
            userIn = input("Invalid character. Please enter a score limit: ")
        return int(userIn)

    def play(self, scoreLimit):

        # decided to use these for end of game messages
        winMsgs = ["Well played!", "Great!", "Ez pez!", "Most impressive.", "You win!"]
        drawMsgs = ["Draw!", "Tie!", "Stalemate!", "Tie, try again."]
        loseMsgs = ["Maybe next time!", "Hard luck!", "You lost!", "Unlucky!"]

        options = ["r", "p", "s"]

        done = False    # keeps loop going while it's "not done"
        userScore = 0   # storing user and computer score
        compScore = 0
        gamesPlayed = 0
        # while the game isn't done and neither player reached score limit
        while (not done) and (userScore < scoreLimit) and (compScore < scoreLimit):
            userchoice = input().lower()
            compChoice = random.choice(options)     # computer chooses random option
            result = userchoice + compChoice        # concatenating the options

            # if user decides to quit
            if userchoice == "q":
                done = True

            # if user types invalid input
            elif userchoice not in options:
                print("Invalid option, try again..")

            # MAYBE refactor to avoid repetition of "random.choice()..."
            # if user wins
            elif result in self.userWin:
                userScore += 1
                gamesPlayed += 1
                print("{} Score: {}:{}".format(self.userWin[result], userScore, compScore))

            # if its a draw
            elif result in self.draw:
                # gamesPlayed += 1 # probably best not to increment number of games played when it's a draw
                print("{} Score: {}:{}".format(self.draw[result], userScore, compScore))

            # if user loses
            else:
                compScore += 1
                gamesPlayed += 1
                print("{} Score: {}:{}".format(self.userLose[result], userScore, compScore))

        # adding newline for spacing
        # if the number of games played is less than score limit, quit (DRAW NOT COUNTED AS GAME PLAYED)
        if gamesPlayed < scoreLimit:
            return "\nYou quit.."

        # if you lose
        elif userScore < compScore:
            return "\n{} Final score: {}:{}".format(random.choice(loseMsgs), userScore, compScore)

        # if draw
        elif userScore == compScore:
            return "\n{} Final score: {}:{}".format(random.choice(drawMsgs), userScore, compScore)

        # if you win
        return "\n{} Final score: {}:{}".format(random.choice(winMsgs), userScore, compScore)

def main():
    # Basically, if you want to play "best of NUM_GAMES" then I'd have to use "totalGames"
    # Else if you want to use "first to SCORE_VALUE" then I'd have to use "scoreLimit"

    rps = RPS()
    goodbyeMsgs = ["Thanks for playing!", "Ciao!", "Goodbye!", "See you around!"]
    playAgainMsgs = ["Would you dare to play again? (Y/N): ", "Play again? (Y/N): ", "Care for another game? (Y/N): ", "Try again? (Y/N): "]

    # intro messages
    print("Welcome to the greatest game of Rock, Paper, Scissors!")
    time.sleep(1.5)
    print("Simply press 'R' or 'P' or 'S'. To quit, press 'Q'.\nGood luck!")

    scoreLimit = rps.getScoreLimit()    # then we convert it to an integer and pass it to the play() function
    print(rps.play(scoreLimit))

    # loop runs while user wants to play again
    while input(random.choice(playAgainMsgs)).upper() == "Y":
        print()     # just to space things out a bit
        print(rps.play(rps.getScoreLimit()))
    print(random.choice(goodbyeMsgs))

if __name__ == '__main__':
    main()
