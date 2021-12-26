from ChessGame.pieceTypes.piece import Piece


class Bishop(Piece):
    def __init__(self, piece_key, player):
        super(Bishop, self).__init__(piece_key, player)

    def find_possible_moves(self, loc, previous_turn):
        possible_moves = {}
        possible_moves.update(self.find_bottom_right(loc))
        possible_moves.update(self.find_top_right(loc))
        possible_moves.update(self.find_bottom_left(loc))
        possible_moves.update(self.find_top_left(loc))
        return possible_moves


