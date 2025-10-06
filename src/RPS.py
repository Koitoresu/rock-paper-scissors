from random import choice
from sys import exit

class RockPaperScissors(): 
    def __init__(self): 
        self.playerHp = 3
        self.opponentHp = 3
        self.playerOptions = ['Rock', 'Paper', 'Scissors'] 

    def opponentsChoice(self):
        return choice(self.playerOptions)
    
    def evaluate_winner(self, choice1, choice2): 
        if (choice1 == 'Rock' and choice2 == 'Scissors') or \
            (choice1 == 'Paper' and choice2 == 'Rock') or \
                (choice1 == 'Scissors' and choice2 == 'Paper'):
            print(f'{choice1} beats {choice2}. You win this round!')
            self.opponentHp -= 1
        else:
            print(f'{choice2} beats {choice1}. You lose this round!')
            self.playerHp -= 1

    def playGame(self): 
        while self.playerHp > 0 and self.opponentHp > 0: 
            print(f'\tHP: {self.playerHp} | OpponentHp: {self.opponentHp}\n')
            playerInput = str(input('What stance will you go with:\n'))
            
            if len(playerInput) == 0:
                print('You must choose a stance\n')
                continue
                
            stance = playerInput.capitalize()

            if stance not in self.playerOptions: 
                print('\nYour choice was invalid, please choose another stance!\n')
                continue

            opponentsChoice = self.opponentsChoice()

            if stance == opponentsChoice: 
                print(f'Both chose {stance}. It\'s a tie!')
            else: 
                self.evaluate_winner(stance, opponentsChoice)
            
        if self.opponentHp == 0:
            print('\nWINNER WINNER CHICKEN DINNER')
        else: 
            # self.playerHp == 0:
            print('\nYOU LOSE!')

        # exit()

if __name__ == '__main__':
    initializeGame = RockPaperScissors()
    initializeGame.playGame()