from ChessGame.pieceTypes.piece import Piece


class Rook(Piece):
    def __init__(self, piece_key, player):
        super(Rook, self).__init__(piece_key, player)


    def find_possible_moves(self, loc, previous_turn):
        possible_moves = self.rook_possible_moves(loc, previous_turn)
        return possible_moves

