import pygame

class Piece:
    def __init__(self, x, y, color, board):
        self.x = x
        self.y = y
        self.pos = (x, y)
        self.board = board
        self.color = color


    def _move(self, tile):
        for i in self.board.tile_list:
            i.highlight = False
        #Moves
        if tile in self.valid_moves() and not self.board.is_jump:
            prev_tile = self.board.get_tile_from_pos(self.pos)
            self.pos, self.x, self.y, = tile.pos, tile.x, tile.y
            prev_tile.current_piece = None
            tile.current_piece = self
            self.board.chosen_piece = None
            self.has_moved = True

            if self.notation == 'p':
                if self.y == 0 or self.y == 7:
                    from Double import Double
                    tile.current_piece = Double(
                        self.x, self.y, self.color, self.board
                    )
            return True
        #Jumps
        elif self.board.is_jump:
            for move in self.valid_jumps():
                if tile in move:
                    prev_tile = self.board.get_tile_from_pos(self.pos)
                    jumped_piece = move[-1]
                    self.pos, self.x, self.y = tile.pos, tile.x, tile.y
                    prev_tile.current_piece = None
                    jumped_piece.chosen_piece = None
                    tile.current_piece = self
                    self.board.chosen_piece = None
                    self.has_moved = True
                    #Promotion
                    if self.notation == 'p':
                        if self.y == 0 or self.y == 7:
                            from Double import Double
                            tile.current_piece = Double(
                                self.x, self.y, self.color, self.board
                            )
                    return True
        else:
            self.board.chosen_piece = None
            return False
