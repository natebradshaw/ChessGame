from ChessGame.config2 import players_pieces_location_map
from ChessGame.pieceTypes.piece import Piece


class Pawn(Piece):
    def __init__(self, piece_key, player):
        super(Pawn, self).__init__(piece_key, player)

    def set_starting_position(self, board):
        column = players_pieces_location_map[self.key]
        if self.owner.player_key == 1:
            row = '7'
        else:
            row = '2'
        loc = board.structure[column][row]
        loc.add_piece(self)
        self.initial_location = loc
        return loc

    def find_possible_moves(self):
        pass

        #possible_moves = []
        if self.owner.player_key == 1:
            pass
        #else:
            direction = 1
        #    if self.location.get_top_left_loc()
        #if self.initial_location == self.location:




