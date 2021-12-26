from ChessGame.pieceTypes.piece import Piece


class Rook(Piece):
    def __init__(self, piece_key, player):
        super(Rook, self).__init__(piece_key, player)


    def find_possible_moves(self, loc, previous_turn):
        possible_moves = {}
        possible_moves.update(self.find_bottom(loc))
        possible_moves.update(self.find_top(loc))
        possible_moves.update(self.find_left(loc))
        possible_moves.update(self.find_right(loc))
        return possible_moves

