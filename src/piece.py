# PIECE DI SINI DIADAPTASI MENJADI PIECE YANG ADA DI SHOGI

# == PIECE VALUES ==
# pawn = 1
# lance, knight = 3
# silver, gold = 5
# bishop = 8
# rook = 9
# promoted bishop = 12
# promoted rook = 13

import os

class Piece:
    
    def __init__(self, name, color, value, texture = None, texture_rect = None):
        self.name = name
        self.color = color
        value_sign = 1 if color == "white" else -1
        self.value = value * value_sign
        self.moves = []
        self.moved = False
        self.texture = texture
        self.set_texture()
        self.texture_rect = texture_rect
    
    def set_texture(self, size = 80):
        self.texture = os.path.join(f'assets/images/imgs-{size}px/{self.color}_{self.name}.png')
        
    def add_moves(self, move):
        self.moves.append(move)

class Pawn(Piece):
    def __init__(self, color):
        if color == 'white': # PERSPEKTIF PLAYER 1 KALAU DI CATUR
            self.dir = -1
        else:
            self.dir = 1
            
        super().__init__("pawn", color, 1.0)
        
class Lance(Piece):
    def __init__(self, color):            
        super().__init__("lance", color, 4.30)
        
class Knight(Piece):
    def __init__(self, color):            
        super().__init__("knight", color, 4.50)
        
class Silver(Piece):
    def __init__(self, color):            
        super().__init__("silver", color, 6.40)
        
class Gold(Piece):
    def __init__(self, color):            
        super().__init__("gold", color, 6.90)
        
class Bishop(Piece):
    def __init__(self, color):            
        super().__init__("bishop", color, 8.90)
        
class Rook(Piece):
    def __init__(self, color):            
        super().__init__("rook", color, 10.40)
        
class King(Piece):
    def __init__(self, color):            
        super().__init__("king", color, 1000000.00)
        
