from ChessGame.pieceTypes.piece import Piece


class Knight(Piece):
    def __init__(self, piece_key, player):
        super(Knight, self).__init__(piece_key, player)

    def find_possible_moves(self, loc, previous_turn):
        possible_moves = self.knight_possible_moves(loc, previous_turn)
        return possible_moves


