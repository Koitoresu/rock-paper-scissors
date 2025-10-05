from random import random

class RockPaperScissors(): 
    def __init__(self): 
        self.playerHp = 3
        self.opponentHp = 3
        self.playerOptions = ['Rock', 'Paper', 'Scissors'] 

    def playGame(self): 
        playerInput = str(input('What stance will you go with:\n'))
        stance = playerInput.lower()

        while self.playerHp > 0: 
            if len(playerInput) <= 0:
                if stance not in self.playerOptions: 
                    print('Your choice was invalid, please choose another stance!')

            if self.opponentHp == 0:
                print('WIINNER WINNER CHICKEN DINNER')
                break

    def opponentsChoice(self):
        choice = random.random % 3

        return self.playerOptions[choice]


