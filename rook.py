from chess_piece import Chess_Piece

class Rook(Chess_Piece):
    def  __init__(self, x : int, y : int, team : int) -> None:
        super().__init__(x, y, team)

    def can_move(self, board : list, x_destination : int, y_destination : int) -> bool:
        if board[x_destination][y_destination] != "":
            return False