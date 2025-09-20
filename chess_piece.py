class Chess_Piece:
    def __init__(self, x : int, y : int, team : int) -> None:
        self.x = x
        self.y = y
        self.can_change = False
        self.times_moved = 0
        self.team = team
    

    def get_x(self) -> int:
        return self.x
    
    def get_y(self) -> int:
        return self.y
    
    def set_x(self, x) -> bool:
        if x >= 0 and x <= 7:
            self.x = x
        else:
            return False
    
    def set_y(self, y) -> bool:
        if y >= 0 and y <= 7:
            self.y = y
        else:
            return False
    
    def get_times_moved(self) -> int:
        return self.times_moved
    
    def get_team(self) -> int:
        return self.team