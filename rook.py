from chess_piece import Chess_Piece

class Rook(Chess_Piece):
    def  __init__(self, x : int, y : int, team : int) -> None:
        super().__init__(x, y, team)

    def can_move(self, board : list, x_destination : int, y_destination : int) -> bool:
        if board[x_destination][y_destination] != "":
            return False
        
        if abs(self.x - x_destination) >= 1 and abs(self.y - y_destination) >= 1 :
            return False
        
        return True
    
    def can_take(self, board : list, x_destination : int, y_destination : int) -> bool:
        if abs(self.x - x_destination) >= 1 and abs(self.y - y_destination) >= 1:
            return False
        
        if board[y_destination][x_destination].get_team() != self.team:
            return True
        
        return False