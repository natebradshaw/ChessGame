from ChessGame.pieceTypes.piece import Piece


class Rook(Piece):
    def __init__(self, piece_key, player):
        super(Rook, self).__init__(piece_key, player)

    def find_possible_moves(self):
        pass
