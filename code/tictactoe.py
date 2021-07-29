import random

class TicTacToe:
    positions = []
    winner = 0
    size = 3
    cond_winner_1 = ''
    cond_winner_2 = ''
    player = 1
    turn = 0
    def __init__(self, size=3):
        self.positions = []
        self.winner = 0
        self.turn = 0
        self.size = size
        for i in range(size * size):
            self.positions.append(0)
        for i in range(size):
            self.cond_winner_1 = self.cond_winner_1 + '1'
            self.cond_winner_2 = self.cond_winner_2 + '2'
        
        self.player = random.randrange(1,3)

    def get_player(self):
        return self.player

    def get_positions(self):
        return self.positions

    def get_turn(self):
        return self.turn

    def get_winner(self):
        return self.winner

    def play(self, pos):
        res = False
        error_msg = ''
        if pos < 0 or pos >= len(self.positions):
            error_msg = 'invalid position'
        elif self.positions[pos] != 0:
            if self.player == 2:
                error_msg = 'the position is already taken (' + str(pos) + ')'
                #print(error_msg)
        else:
            self.positions[pos] = self.player
            if self.player == 1:
                self.player = 2
            else:
                self.player = 1
            self.turn = self.turn + 1
            self.check_winner()
            res = True
        
        return res

    def possible_moves(self):
        return self.positions.count(self.positions == 0)
            

    def check_winner(self):
        horizontal_line = ''
        vertical_line = ''
        diagonal_line_1 = ''
        i = 0
        while i < len(self.positions) and self.winner == 0:
            if i % self.size == 0:
                horizontal_line = ''
            vertical_line = ''
            diagonal_line_1 = ''
            diagonal_line_2 = ''

            horizontal_line = horizontal_line + str(self.positions[i])
            for j in range(self.size):
                v = self.size * j + i
                if v < len(self.positions):
                    vertical_line = vertical_line + str(self.positions[v])

                d1 = j * (self.size + 1)
                if d1 < len(self.positions):
                    diagonal_line_1 = diagonal_line_1 + str(self.positions[d1])

                d2 = (j + 1)*(self.size - 1)
                if d2 < len(self.positions):
                    diagonal_line_2 = diagonal_line_2 + str(self.positions[d2])

            if horizontal_line == self.cond_winner_1 or vertical_line == self.cond_winner_1 or diagonal_line_1 == self.cond_winner_1 or diagonal_line_2 == self.cond_winner_1:
                self.winner = 1
            elif horizontal_line == self.cond_winner_2 or vertical_line == self.cond_winner_2 or diagonal_line_1 == self.cond_winner_2 or diagonal_line_2 == self.cond_winner_2:
                self.winner = 2

            i = i + 1

    def print_board(self):
        #print(self.positions)
        row = ''
        n = 1
        for pos in self.positions:
            if len(row) > 0:
                row = row + ' | '
            if pos == 0:
                row = row + str(n-1)
            elif pos == 1:
                row = row + 'X'
            elif pos == 2:
                row = row + 'O'
            if n % self.size == 0:
                print(row)
                print('---------')
                row = ''
            n = n + 1
        print(row)