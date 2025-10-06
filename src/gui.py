import pygame
from RPS import RockPaperScissors

pygame.init()

base_width, base_height = 1280, 720
screen = pygame.display.set_mode((base_width, base_height))
pygame.display.set_caption('Rock, Paper, Scissors')
clock = pygame.time.Clock()
running = True
game = RockPaperScissors()
game_state = 'menu'

_paperMove = pygame.image.load('./assets/paper_transparent.png').convert_alpha()
_rockMove = pygame.image.load('./assets/rock_transparent.png').convert_alpha()
_scissorMove = pygame.image.load('./assets/scissors_transparent.png').convert_alpha()
_startButton = pygame.image.load('./assets/start_button.png').convert_alpha()
_exitButton = pygame.image.load('./assets/exit_button.png').convert_alpha()
_resetButton = pygame.image.load('./assets/reset.png').convert_alpha()

font = pygame.font.SysFont('Segoe Script', 30)
welcome_text = font.render('Welcome to the Rock, Paper, Scissors Game!', True, 'Black')
welcomeTextPos = (300, 150)
message = 'test'

class Button():
    def __init__(self, x, y, img, scale):
        width = img.get_width()
        height = img.get_height()
        self.img = pygame.transform.scale(img, (int(width * scale), int(height * scale)))
        self.rect = self.img.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):
        # get mouse pos
        pos = pygame.mouse.get_pos()
        action = False
        # print(pos)

        #check mouse over and click condition
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

            if pygame.mouse.get_pressed()[0] == 0: 
                self.clicked = False

        # draw button on sceen 
        screen.blit(self.img, (self.rect.x, self.rect.y))  # look into blit 

        return action

startButton = Button(450, 250, _startButton, 0.7)
resetButton = Button(450, 250, _resetButton, 0.7)
exitButton = Button(450, 400, _exitButton, 0.7)
rockButton = Button(100, 200, _rockMove, 0.5)
paperButton = Button(300, 200, _paperMove, 0.5)
scissorButton = Button(500, 200, _scissorMove, 0.5)

while running: 
    screen.fill((255, 255, 255))

    if game_state == 'menu': 
        screen.blit(welcome_text, welcomeTextPos)

        if startButton.draw():
            game_state = 'playing'
            pygame.event.clear()

        if exitButton.draw(): 
            running = False

    elif game_state == 'playing':
        hpText = font.render(f'Player HP: {game.playerHp} | Opponent HP: {game.opponentHp}', True, 'Black')
        screen.blit(hpText, (base_width // 2.5, 0))

        if rockButton.draw():
            stance = 'Rock'
            opponentsChoice = game.opponentsChoice()
            result = game.evaluate_winner(stance, opponentsChoice)
            # print(stance)

        if paperButton.draw():
            stance = 'Paper'
            opponentsChoice = game.opponentsChoice()
            result = game.evaluate_winner(stance, opponentsChoice)
            # print(stance)

        if scissorButton.draw():
            stance = 'Scissor'
            opponentsChoice = game.opponentsChoice()
            result = game.evaluate_winner(stance, opponentsChoice)
            # print(stance)

        if game.playerHp <= 0: 
            message = 'YOU LOSE'
            game_state = 'game_over'
        elif game.opponentHp <= 0:
            message = 'WINNER WINNER CHICKEN DINNER'
            game_state = 'game_over'
    elif game_state == 'game_over':
        msgText = font.render(message, True, 'Black')
        screen.blit(msgText, (300, 150))

        if resetButton.draw():
            game.playerHp = 3
            game.opponentHp = 3
            message = ''
            game_state = 'playing'
    
    pygame.display.update()

    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        #     mouse_pos = event.pos

pygame.quit