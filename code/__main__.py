from tictactoe import TicTacToe
from machine import Machine
from sys import exit
import pygame
import pygame_menu

TITLE = 1
print(TITLE)
TITLE = "Tic Tac Toe"
print(TITLE)

POS_SIZE = 200

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 700

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0, 255, 0) 
BLUE = (0, 0, 128)
GRAY = (120,120,120)

pygame.init()
machine = Machine()
#clock = pygame.time.Clock()

screen = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
screen.fill(GRAY)
pygame.display.set_caption(TITLE)

menu = pygame_menu.Menu(TITLE, WINDOW_WIDTH , WINDOW_HEIGHT,
                       theme=pygame_menu.themes.THEME_BLUE)


cpu_model = ""
def set_model(self, mode):
    global cpu_model
    cpu_model = mode

def print_grid():
    pygame.draw.line(screen, BLACK, (POS_SIZE, 0), (POS_SIZE, WINDOW_WIDTH))
    pygame.draw.line(screen, BLACK, (POS_SIZE*2, 0), (POS_SIZE*2, WINDOW_WIDTH))
    pygame.draw.line(screen, BLACK, (0, POS_SIZE), (WINDOW_WIDTH, POS_SIZE))
    pygame.draw.line(screen, BLACK, (0, POS_SIZE*2), (WINDOW_WIDTH, POS_SIZE*2))

def start_the_game():
    global cpu_model

    menu.close()
    game = TicTacToe()

    machine = Machine(cpu_model)
    machine.fit()

    tiles = []
    pos_0 = pygame.draw.rect(screen, WHITE, (0, 0, POS_SIZE, POS_SIZE))
    tiles.append(pos_0)
    pos_1 = pygame.draw.rect(screen, WHITE, (POS_SIZE, 0, POS_SIZE, POS_SIZE))
    tiles.append(pos_1)
    pos_2 = pygame.draw.rect(screen, WHITE, (POS_SIZE*2, 0, POS_SIZE, POS_SIZE))
    tiles.append(pos_2)
    pos_3 = pygame.draw.rect(screen, WHITE, (0, POS_SIZE, POS_SIZE, POS_SIZE))
    tiles.append(pos_3)
    pos_4 = pygame.draw.rect(screen, WHITE, (POS_SIZE, POS_SIZE, POS_SIZE, POS_SIZE))
    tiles.append(pos_4)
    pos_5 = pygame.draw.rect(screen, WHITE, (POS_SIZE*2, POS_SIZE, POS_SIZE, POS_SIZE))
    tiles.append(pos_5)
    pos_6 = pygame.draw.rect(screen, WHITE, (0, POS_SIZE*2, POS_SIZE, POS_SIZE))
    tiles.append(pos_6)
    pos_7 = pygame.draw.rect(screen, WHITE, (POS_SIZE, POS_SIZE*2, POS_SIZE, POS_SIZE))
    tiles.append(pos_7)
    pos_8 = pygame.draw.rect(screen, WHITE, (POS_SIZE*2, POS_SIZE*2, POS_SIZE, POS_SIZE))
    tiles.append(pos_8)

    print_grid()

    pygame.display.flip()

    pygame.display.update()
    
    # Main Loop
    while game.get_winner() == 0 and game.possible_moves() > 0:
        pygame.event.pump()
        pygame.display.update()

        pos = -1
        if game.get_player() == 1:
            # Mouse position and button clicking.
            mouse_pos = pygame.mouse.get_pos()
            leftClick, middleClick, rightClick = pygame.mouse.get_pressed()

            # Check if the rect collided with the mouse pos
            # and if the left mouse button was pressed.
            if leftClick:
                if pos_0.collidepoint(mouse_pos):
                    pos = 0
                elif pos_1.collidepoint(mouse_pos):
                    pos = 1
                elif pos_2.collidepoint(mouse_pos):
                    pos = 2
                elif pos_3.collidepoint(mouse_pos):
                    pos = 3
                elif pos_4.collidepoint(mouse_pos):
                    pos = 4
                elif pos_5.collidepoint(mouse_pos):
                    pos = 5
                elif pos_6.collidepoint(mouse_pos):
                    pos = 6
                elif pos_7.collidepoint(mouse_pos):
                    pos = 7
                elif pos_8.collidepoint(mouse_pos):
                    pos = 8
        else:
            currentConditions = game.get_positions().copy()
            currentConditions.insert(0, game.get_turn())
            pred = machine.predict(currentConditions)
            if len(pred) > 0:
                pos = int(pred[0])

        if game.play(int(pos)):
            i = 0
            while i < len(game.positions):
                color = WHITE
                if game.positions[i] == 1:
                    color = RED
                elif game.positions[i] == 2:
                    color = BLUE
                tiles[i] = pygame.draw.rect(screen, color, (tiles[i].x,tiles[i].y, tiles[i].w, tiles[i].h))
                i = i + 1
            print_grid()
        
        # Quit pygame.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit(1)

    result = 'The game ended with a draw'
    color = BLACK
    if game.get_winner() > 0:
        result = 'Player ' + str(game.get_winner()) + ' won!'
    font = pygame.font.Font(pygame.font.get_default_font(), 36)
    text_result = font.render(result, True, color)
    screen.blit(text_result, dest=(0, WINDOW_WIDTH+10))
    pygame.display.update()
    pygame.time.delay(3000)

menu.add.text_input('Name: ', default='Joao')
menu.add.selector('Model: ', [
    ("Support Vector Machine", "support_vector_machine"),
    ("Decision Tree Classifier", "decision_tree_classifier"),
    ("Gaussian NB", "gaussian_nb"),
    ("Random Forest Classifier", "random_forest_classifier"),
    ("GradientBoostingClassifier", "radient_boosting_classifier"),
    ("AdaBoostClassifier", "ada_boost_classifier"),
    ("Bernoulli NB", "bernoulli_nb"),
    ("Logistic Regression", "logistic_regression")
    ], onchange=set_model)
menu.add.button('Play', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)

menu.mainloop(screen)