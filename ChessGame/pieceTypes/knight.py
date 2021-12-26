from ChessGame.pieceTypes.piece import Piece


class Knight(Piece):
    def __init__(self, piece_key, player):
        super(Knight, self).__init__(piece_key, player)

    def find_possible_moves(self, loc, previous_turn):
        possible_moves = {}
        possible_moves.update(self.bottom_locs(loc))
        possible_moves.update(self.top_locs(loc))
        possible_moves.update(self.right_locs(loc))
        possible_moves.update(self.left_locs(loc))
        return possible_moves

    def bottom_locs(self, loc):
        locs = {}
        locs_determinded = False
        while locs_determinded == False:
            if loc.bot_cent_loc is None:
                break
            else:
                loc = loc.bot_cent_loc

            if loc.bot_left_loc is None:
                pass
            elif loc.bot_left_loc.current_piece is None:
                locs[loc.bot_left_loc] = 'StandardMove'
            elif loc.bot_left_loc.current_piece.owner != self.owner:
                locs[loc.bot_left_loc] = 'Kill'

            if loc.bot_rght_loc is None:
                pass
            elif loc.bot_rght_loc.current_piece is None:
                locs[loc.bot_rght_loc] = 'StandardMove'
            elif loc.bot_rght_loc.current_piece.owner != self.owner:
                locs[loc.bot_rght_loc] = 'Kill'
            locs_determinded = True
        return locs

    def top_locs(self, loc):
        locs = {}
        locs_determinded = False
        while locs_determinded == False:
            if loc.top_cent_loc is None:
                break
            else:
                loc = loc.top_cent_loc

            if loc.top_left_loc is None:
                pass
            elif loc.top_left_loc.current_piece is None:
                locs[loc.top_left_loc] = 'StandardMove'
            elif loc.top_left_loc.current_piece.owner != self.owner:
                locs[loc.top_left_loc] = 'Kill'

            if loc.top_rght_loc is None:
                pass
            elif loc.top_rght_loc.current_piece is None:
                locs[loc.top_rght_loc] = 'StandardMove'
            elif loc.top_rght_loc.current_piece.owner != self.owner:
                locs[loc.top_rght_loc] = 'Kill'
            locs_determinded = True
        return locs

    def right_locs(self, loc):
        locs = {}
        locs_determinded = False
        while locs_determinded == False:
            if loc.mid_rght_loc is None:
                break
            else:
                loc = loc.mid_rght_loc

            if loc.bot_rght_loc is None:
                pass
            elif loc.bot_rght_loc.current_piece is None:
                locs[loc.bot_rght_loc] = 'StandardMove'
            elif loc.bot_rght_loc.current_piece.owner != self.owner:
                locs[loc.bot_rght_loc] = 'Kill'

            if loc.top_rght_loc is None:
                pass
            elif loc.top_rght_loc.current_piece is None:
                locs[loc.top_rght_loc] = 'StandardMove'
            elif loc.top_rght_loc.current_piece.owner != self.owner:
                locs[loc.top_rght_loc] = 'Kill'
            locs_determinded = True
        return locs

    def left_locs(self, loc):
        locs = {}
        locs_determinded = False
        while locs_determinded == False:
            if loc.mid_left_loc is None:
                break
            else:
                loc = loc.mid_left_loc

            if loc.bot_left_loc is None:
                pass
            elif loc.bot_left_loc.current_piece is None:
                locs[loc.bot_left_loc] = 'StandardMove'
            elif loc.bot_left_loc.current_piece.owner != self.owner:
                locs[loc.bot_left_loc] = 'Kill'

            if loc.top_left_loc is None:
                pass
            elif loc.top_left_loc.current_piece is None:
                locs[loc.top_left_loc] = 'StandardMove'
            elif loc.top_left_loc.current_piece.owner != self.owner:
                locs[loc.top_left_loc] = 'Kill'
            locs_determinded = True
        return locs
