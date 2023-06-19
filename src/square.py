
class Square:
    
    def __init__(self, horizontal, vertical, piece = None):
        self.horizontal = horizontal
        self.vertical = vertical
        self.piece = piece
        
    def has_piece(self):
        return self.piece != None
    
    def isempty(self):
        return not self.has_piece()
    
    def has_team_piece(self, color):
        return self.has_piece() and self.piece.color == color

    def has_rival_piece(self, color):
        return self.has_piece() and self.piece.color != color
    
    def isempty_or_rival(self, color):
        return self.isempty() or self.has_rival_piece(color) 
    
    
    @staticmethod
    def in_range(*args):
        for arg in args:
            if arg < -0 or arg > 8:
                return False
        return True

