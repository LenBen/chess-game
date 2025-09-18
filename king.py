from chess_piece import Chess_Piece

class King(Chess_Piece):
    def __init__(self, x : int, y : int, team : int) -> None:
        super().__init__(x, y, team)
        
    def can_move(self, board : list, x_destination : int, y_destination : int) -> bool:
        if board[x_destination][y_destination] != "":
            if self.can_take(x_destination, y_destination):
                return True
            return False
        
        if abs(self.x - x_destination) > 1:
            return False
        
        if abs(self.y - y_destination) > 1:
            return False
        
        return False

    def can_take(self, board : list, x_destination : int, y_destination : int) -> bool:
        if abs(self.x - x_destination) == 1 and abs(self.y - y_destination) == 1 and \
              self.team != board[x_destination][y_destination].get_team():
            return True
        else:
            return False

