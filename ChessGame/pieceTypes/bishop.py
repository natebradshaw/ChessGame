from ChessGame.pieceTypes.piece import Piece


class Bishop(Piece):
    def __init__(self, piece_key, player):
        super(Bishop, self).__init__(piece_key, player)

    def find_possible_moves(self, loc, previous_turn):
        possible_moves = self.bishop_possible_moves(loc, previous_turn)
        return possible_moves




