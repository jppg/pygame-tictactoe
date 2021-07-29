from tictactoe import TicTacToe
import random
import csv
import os

gameNr = 1
gameLimit = 10000

lst_moves_1 = []
lst_moves_2 = []

while gameNr <= gameLimit:
    print("+++++++++++")
    print("Game#", gameNr)
    game = TicTacToe()

    tmp_moves_1 = []
    tmp_moves_2 = []
    while game.get_winner() == 0 and game.possible_moves() > 0:
        pos = game.get_positions().copy()
        while game.possible_moves() > 0:
            move = random.randint(0,9)
            if game.play(int(move)):
                if game.get_player() == 1:
                    tmp_moves_2.append([gameNr] + [game.get_turn() - 1] + pos + [move])
                else:
                    tmp_moves_1.append([gameNr] + [game.get_turn() - 1] + pos + [move])
                break

    print("Winner of game ", gameNr, "is", game.get_winner())

    if game.get_winner() == 1:
        lst_moves_1.append(tmp_moves_1)
        #lst_moves_1.append(tmp_moves_1[len(tmp_moves_1) - 1])
    else:
        #lst_moves_2.append(tmp_moves_2[len(tmp_moves_2) - 1])
        lst_moves_2.append(tmp_moves_2)

    #print("List X: ", lst_moves_1)
    #print("List O: ", lst_moves_2)
    game.print_board()

    gameNr = gameNr + 1

with open('moves_1.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    for row in lst_moves_1:
        writer.writerows(row)

with open('moves_2.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    for row in lst_moves_2:
        writer.writerows(row)