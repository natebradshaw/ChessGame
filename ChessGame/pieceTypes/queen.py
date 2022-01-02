from ChessGame.pieceTypes.piece import Piece


class Queen(Piece):
    def __init__(self, piece_key, player):
        super(Queen, self).__init__(piece_key, player)

    def find_possible_moves(self, loc, previous_turn):
        possible_moves = self.queen_possible_moves(loc, previous_turn)
        return possible_moves

