from ChessGame.config2 import players_pieces_location_map
from ChessGame.pieceTypes.piece import Piece


class Pawn(Piece):
    def __init__(self, piece_key, player):
        super(Pawn, self).__init__(piece_key, player)
        self.en_passant_kill = None

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

    def set_en_passant_kill(self, new_status):
        self.en_passant_kill = new_status

    def find_possible_moves(self, loc, previous_turn):
        possible_moves = self.pawn_possible_moves(loc, previous_turn)
        return possible_moves



    def get_list(self, possible_moves):
        return dict.keys(possible_moves)



