computer = 'X'
user = 'O'
empty = 'e'

infinity = 1000

class AI(object):
    def __init__(self, board):
        self.board = board[:]
        self.at_score = []
        self.is_finish()
        self.get_coords()
        self.cnt = 0

    def is_full(self, board):
        for y in range(3):
            for x in range(3):
                if board[y][x] == empty:
                    return False
        return True
    
    def is_win(self, player, board):
        #가로, 세로
        for y in range(3):
            row, col = 0, 0
            for x in range(3):
                if board[y][x] == player:
                    row += 1
                if board[x][y] == player:
                    col += 1
            if row == 3 or col == 3:
                return True
            
        for y in range(3):
            x, right, left = 2, 0, 0
            if board[y][y] == player:
                right += 1
            if board[y][x] == player:
                left += 1
            x -= 1
        if right == 3 or left == 3:
            return True
        return False
    
    def is_finish(self):
        return (self.is_full(self.board)) or (self.is_win(computer, self.board)) or (self.is_win(user, self.board))

    #
    def get_coords(self):
        coords = []
        for y in range(3):
            for x in range(3):
                if self.board[y][x] == empty:
                    coords.append((x, y))
        return coords

    