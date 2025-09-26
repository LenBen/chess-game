from chess_piece import Chess_Piece

class Bishop(Chess_Piece):
    def __init__(self, x : int, y : int, team : int):
        super().__init__(x, y, team)

    def can_move(self, board : list, x_destination : int, y_destination : int) -> bool:
        if board[y_destination][x_destination] != "":
            return False
        
        if abs(self.x - x_destination) != abs(self.y - y_destination):
            return False
        
        return True
    
    def can_take(self, board : list, x_destination : int, y_destination : int) -> bool:
        if abs(self.x - x_destination) != abs(self.y - y_destination):
            return False
        
        if board[y_destination][x_destination].get_team() != self.team:
            return True
        
        return False