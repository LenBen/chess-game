from chess_piece import Chess_Piece

class Pawn(Chess_Piece):
    def __init__(self, x : int, y : int) -> None:
        super.__init__(x, y)
        self.can_change = True
        self.times_moved = 0
    
    def can_move(self, board : list, x_destination : int, y_destination : int) -> bool:
        if board[x_destination][y_destination] != "":
            if self.can_take(x_destination, y_destination):
                return True
            return False
        
        if self.y != y_destination:
            return False

        if abs(self.x - x_destination) > 2:
            return False  

        if abs(self.x - x_destination) == 2 and self.times_moved != 0:
            return False
        
        return True

    def can_take(self, x_destination : int, y_destination : int) -> bool:
        if abs(self.x - x_destination) == 1 and abs(self.y - y_destination) == 1:
            return True
        else:
            return False
    