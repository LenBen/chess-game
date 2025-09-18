class Chess_Piece:
    def __init__(self, x : int, y : int, team : int) -> None:
        self.x = x
        self.y = y
        self.can_change = False
        self.times_moved = 0
        self.team = team
    
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def set_x(self, x):
        if x >= 0 and x <= 7:
            self.x = x
    
    def set_y(self, y):
        if y >= 0 and y <= 7:
            self.y = y
    
    def get_times_moved(self):
        return self.times_moved