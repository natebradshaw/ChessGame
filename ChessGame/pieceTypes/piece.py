from ChessGame.config2 import players_pieces_location_map
import abc

class Piece(object):#object OR abc.ABC
    count = 0
    def __init__(self, key, player):
        Piece.count += 1
        self.key = key
        self.initial_location = None
        self.owner = player
        self.alive = True
        self.short_hand_name = f'{player.player_key}{self.key[0].upper()}{self.piece_origin()}'
        self.moved_status = False
        self.under_threat = False

    def set_location(self, loc):
        self.location = loc

    def set_initial_location(self, loc):
        self.initial_location = loc

    def piece_origin(self):
        if Piece.count <= 32:
            return self.key[-1].upper()
        else:
            pieces = self.owner.pieces
            player_piece_count = len(pieces)
            key = player_piece_count - 13
            return key

    def set_starting_position(self, board):
        column = players_pieces_location_map[self.key]
        if self.owner.player_key == 1:
            row = '8'
        else:
            row = '1'
        loc = board.structure[column][row]
        loc.add_piece(self)
        self.initial_location = loc
        return loc

    def set_dead(self):
        self.alive = False

    @abc.abstractmethod
    def find_possible_moves(self, loc, previous_turn):
        "Finds possible move"

    def king_standard_moves(self, loc, previous_turn, piece_att='current_piece'):
        possible_moves = {}
        possible_moves.update(self.king_find_bottom_right(loc, piece_att))
        possible_moves.update(self.king_find_bottom_center(loc, piece_att))
        possible_moves.update(self.king_find_bottom_left(loc, piece_att))
        possible_moves.update(self.king_find_mid_right(loc, piece_att))
        possible_moves.update(self.king_find_mid_left(loc, piece_att))
        possible_moves.update(self.king_find_top_right(loc, piece_att))
        possible_moves.update(self.king_find_top_center(loc, piece_att))
        possible_moves.update(self.king_find_top_left(loc, piece_att))
        return possible_moves

    def queen_possible_moves(self, loc, previous_turn, piece_att='current_piece'):
        possible_moves = {}
        possible_moves.update(self.find_bottom(loc, piece_att))
        possible_moves.update(self.find_top(loc, piece_att))
        possible_moves.update(self.find_left(loc, piece_att))
        possible_moves.update(self.find_right(loc, piece_att))
        possible_moves.update(self.find_bottom_right(loc, piece_att))
        possible_moves.update(self.find_top_right(loc, piece_att))
        possible_moves.update(self.find_bottom_left(loc, piece_att))
        possible_moves.update(self.find_top_left(loc, piece_att))
        return possible_moves

    def rook_possible_moves(self, loc, previous_turn, piece_att='current_piece'):
        possible_moves = {}
        possible_moves.update(self.find_bottom(loc, piece_att))
        possible_moves.update(self.find_top(loc, piece_att))
        possible_moves.update(self.find_left(loc, piece_att))
        possible_moves.update(self.find_right(loc, piece_att))
        return possible_moves

    def find_loc(self, board, piece_att='current_piece'):
        for column in range(1, 9):
            for row in range(1, 9):
                column_key = str(column)
                row_key = str(row)
                if board.structure[column_key][row_key].get_piece(piece_att) == self:
                    return board.structure[column_key][row_key]

    def find_bottom(self, loc, piece_att='current_piece'):
        bottom_moves = {}
        limit_found = False
        while limit_found is False:
            if loc.bot_cent_loc is None:  # no location
                limit_found = True
            elif loc.bot_cent_loc.get_piece(piece_att) is not None and loc.bot_cent_loc.get_piece(piece_att).owner == self.owner:  # own piece blocking path
                limit_found = True
            elif loc.bot_cent_loc.get_piece(piece_att) is not None and loc.bot_cent_loc.get_piece(piece_att).owner != self.owner:  # apponant piece blocking path
                bottom_moves[loc.bot_cent_loc] = 'Kill'
                limit_found = True
            elif loc.bot_cent_loc.get_piece(piece_att) is None:  # Empty location
                bottom_moves[loc.bot_cent_loc] = 'StandardMove'
                loc = loc.bot_cent_loc
        return bottom_moves

    def find_top(self, loc, piece_att='current_piece'):
        top_moves = {}
        limit_found = False
        while limit_found is False:
            if loc.top_cent_loc is None:  # no location
                limit_found = True
            elif loc.top_cent_loc.get_piece(piece_att) is not None and loc.top_cent_loc.get_piece(piece_att).owner == self.owner:  # own piece blocking path
                limit_found = True
            elif loc.top_cent_loc.get_piece(piece_att) is not None and loc.top_cent_loc.get_piece(piece_att).owner != self.owner:  # apponant piece blocking path
                top_moves[loc.top_cent_loc] = 'Kill'
                limit_found = True
            elif loc.top_cent_loc.get_piece(piece_att) is None:  # Empty location
                top_moves[loc.top_cent_loc] = 'StandardMove'
                loc = loc.top_cent_loc
        return top_moves

    def find_left(self, loc, piece_att='current_piece'):
        left_moves = {}
        limit_found = False
        while limit_found is False:
            if loc.mid_left_loc is None:  # no location
                limit_found = True
            elif loc.mid_left_loc.get_piece(piece_att) is not None and loc.mid_left_loc.get_piece(piece_att).owner == self.owner:  # own piece blocking path
                limit_found = True
            elif loc.mid_left_loc.get_piece(piece_att) is not None and loc.mid_left_loc.get_piece(piece_att).owner != self.owner:  # apponant piece blocking path
                left_moves[loc.mid_left_loc] = 'Kill'
                limit_found = True
            elif loc.mid_left_loc.get_piece(piece_att) is None:  # Empty location
                left_moves[loc.mid_left_loc] = 'StandardMove'
                loc = loc.mid_left_loc
        return left_moves

    def find_right(self, loc, piece_att='current_piece'):
        right_moves = {}
        limit_found = False
        while limit_found is False:
            if loc.mid_rght_loc is None:  # no location
                limit_found = True
            elif loc.mid_rght_loc.get_piece(piece_att) is not None and loc.mid_rght_loc.get_piece(piece_att).owner == self.owner:  # own piece blocking path
                limit_found = True
            elif loc.mid_rght_loc.get_piece(piece_att) is not None and loc.mid_rght_loc.get_piece(piece_att).owner != self.owner:  # apponant piece blocking path
                right_moves[loc.mid_rght_loc] = 'Kill'
                limit_found = True
            elif loc.mid_rght_loc.get_piece(piece_att) is None:  # Empty location
                right_moves[loc.mid_rght_loc] = 'StandardMove'
                loc = loc.mid_rght_loc
        return right_moves

    def find_bottom_right(self, loc, piece_att='current_piece'):
        bottom_right_moves = {}
        limit_found = False
        while limit_found is False:
            if loc.bot_rght_loc is None: #no location
                limit_found = True
            elif loc.bot_rght_loc.get_piece(piece_att) is not None and loc.bot_rght_loc.get_piece(piece_att).owner == self.owner: #own piece blocking path
                limit_found = True
            elif loc.bot_rght_loc.get_piece(piece_att) is not None and loc.bot_rght_loc.get_piece(piece_att).owner != self.owner: #apponant piece blocking path
                bottom_right_moves[loc.bot_rght_loc] = 'Kill'
                limit_found = True
            elif loc.bot_rght_loc.get_piece(piece_att) is None: #Empty location
                bottom_right_moves[loc.bot_rght_loc] = 'StandardMove'
                loc = loc.bot_rght_loc
        return bottom_right_moves

    def find_top_right(self, loc, piece_att='current_piece'):
        top_right_moves = {}
        limit_found = False
        while limit_found is False:
            if loc.top_rght_loc is None: #no location
                limit_found = True
            elif loc.top_rght_loc.get_piece(piece_att) is not None and loc.top_rght_loc.get_piece(piece_att).owner == self.owner: #own piece blocking path
                limit_found = True
            elif loc.top_rght_loc.get_piece(piece_att) is not None and loc.top_rght_loc.get_piece(piece_att).owner != self.owner: #apponant piece blocking path
                top_right_moves[loc.top_rght_loc] = 'Kill'
                limit_found = True
            elif loc.top_rght_loc.get_piece(piece_att) is None: #Empty location
                top_right_moves[loc.top_rght_loc] = 'StandardMove'
                loc = loc.top_rght_loc
        return top_right_moves

    def find_bottom_left(self, loc, piece_att='current_piece'):
        bottom_left_moves = {}
        limit_found = False
        while limit_found is False:
            if loc.bot_left_loc is None: #no location
                limit_found = True
            elif loc.bot_left_loc.get_piece(piece_att) is not None and loc.bot_left_loc.get_piece(piece_att).owner == self.owner: #own piece blocking path
                limit_found = True
            elif loc.bot_left_loc.get_piece(piece_att) is not None and loc.bot_left_loc.get_piece(piece_att).owner != self.owner: #apponant piece blocking path
                bottom_left_moves[loc.bot_left_loc] = 'Kill'
                limit_found = True
            elif loc.bot_left_loc.get_piece(piece_att) is None: #Empty location
                bottom_left_moves[loc.bot_left_loc] = 'StandardMove'
                loc = loc.bot_left_loc
        return bottom_left_moves

    def find_top_left(self, loc, piece_att='current_piece'):
        top_left_moves = {}
        limit_found = False
        while limit_found is False:
            if loc.top_left_loc is None: #no location
                limit_found = True
            elif loc.top_left_loc.get_piece(piece_att) is not None and loc.top_left_loc.get_piece(piece_att).owner == self.owner: #own piece blocking path
                limit_found = True
            elif loc.top_left_loc.get_piece(piece_att) is not None and loc.top_left_loc.get_piece(piece_att).owner != self.owner: #apponant piece blocking path
                top_left_moves[loc.top_left_loc] = 'Kill'
                limit_found = True
            elif loc.top_left_loc.get_piece(piece_att) is None: #Empty location
                top_left_moves[loc.top_left_loc] = 'StandardMove'
                loc = loc.top_left_loc
        return top_left_moves

    def knight_possible_moves(self, loc, previous_turn, piece_att='current_piece'):
        possible_moves = {}
        possible_moves.update(self.knight_bottom_locs(loc, piece_att))
        possible_moves.update(self.knight_top_locs(loc, piece_att))
        possible_moves.update(self.knight_right_locs(loc, piece_att))
        possible_moves.update(self.knight_left_locs(loc, piece_att))
        return possible_moves

    def pawn_possible_moves(self, loc, previous_turn, piece_att='current_piece'):
        possible_moves = {}
        if self.owner.player_key == 1:
            if loc.top_left_loc is not None:
                top_left = loc.top_left_loc
            else:
                top_left = None

            if loc.top_rght_loc is not None:
                top_rght = loc.top_rght_loc
            else:
                top_rght = None

            if loc.mid_left_loc is not None:
                mid_left = loc.mid_left_loc
            else:
                mid_left = None

            if loc.mid_rght_loc is not None:
                mid_rght = loc.mid_rght_loc
            else:
                mid_rght = None

            if loc.top_cent_loc is not None:
                cent = loc.top_cent_loc
            else:
                cent = None

            if cent is not None and cent.top_cent_loc is not None:
                two_up_cent = cent.top_cent_loc
            else:
                two_up_cent = None

        else:  # player 2
            if loc.bot_left_loc is not None:
                top_left = loc.bot_left_loc
            else:
                top_left = None

            if loc.bot_rght_loc is not None:
                top_rght = loc.bot_rght_loc
            else:
                top_rght = None

            if loc.mid_left_loc is not None:
                mid_left = loc.mid_left_loc
            else:
                mid_left = None

            if loc.mid_rght_loc is not None:
                mid_rght = loc.mid_rght_loc
            else:
                mid_rght = None

            if loc.bot_cent_loc is not None:
                cent = loc.bot_cent_loc
            else:
                cent = None

            if cent is not None and cent.bot_cent_loc is not None:
                two_up_cent = cent.bot_cent_loc
            else:
                two_up_cent = None

        if previous_turn['turn_type'] == 'TwoSpacePawn' and mid_left is not None \
                and mid_left.get_piece(piece_att) == previous_turn['moved_piece']:  # Enpassant left
            self.en_passant_kill = mid_left
            possible_moves[top_left] = 'EnPassant'
        if previous_turn['turn_type'] == 'TwoSpacePawn' and mid_rght is not None \
                and mid_rght.get_piece(piece_att) == previous_turn['moved_piece']:  # Enpassant right
            self.en_passant_kill = mid_rght
            possible_moves[top_rght] = 'EnPassant'
        if top_left is not None and top_left.get_piece(piece_att) is not None:  # diagonal left attack
            if top_left.get_piece(piece_att).owner != self.owner:
                possible_moves[top_left] = 'Kill'
        if top_rght is not None and top_rght.get_piece(piece_att) is not None:  # diagonal right attack
            if top_rght.get_piece(piece_att).owner != self.owner:
                possible_moves[top_rght] = 'Kill'
        if cent is not None and cent.get_piece(piece_att) is None:  # directly ahead
            possible_moves[cent] = 'StandardMove'
        if self.initial_location == loc and cent is not None and two_up_cent is not None \
                and cent.get_piece(piece_att) is None and two_up_cent.get_piece(piece_att) is None:  # initial move with two spaces
            possible_moves[two_up_cent] = 'TwoSpacePawn'
        possible_moves_checked = self.promoted_pawn_check(possible_moves)
        return possible_moves_checked

    def knight_bottom_locs(self, loc, piece_att='current_piece'):
        locs = {}
        locs_determinded = False
        while locs_determinded == False:
            if loc.bot_cent_loc is None:
                break
            else:
                loc = loc.bot_cent_loc

            if loc.bot_left_loc is None:
                pass
            elif loc.bot_left_loc.get_piece(piece_att) is None:
                locs[loc.bot_left_loc] = 'StandardMove'
            elif loc.bot_left_loc.get_piece(piece_att).owner != self.owner:
                locs[loc.bot_left_loc] = 'Kill'

            if loc.bot_rght_loc is None:
                pass
            elif loc.bot_rght_loc.get_piece(piece_att) is None:
                locs[loc.bot_rght_loc] = 'StandardMove'
            elif loc.bot_rght_loc.get_piece(piece_att).owner != self.owner:
                locs[loc.bot_rght_loc] = 'Kill'
            locs_determinded = True
        return locs

    def knight_top_locs(self, loc, piece_att='current_piece'):
        locs = {}
        locs_determinded = False
        while locs_determinded == False:
            if loc.top_cent_loc is None:
                break
            else:
                loc = loc.top_cent_loc

            if loc.top_left_loc is None:
                pass
            elif loc.top_left_loc.get_piece(piece_att) is None:
                locs[loc.top_left_loc] = 'StandardMove'
            elif loc.top_left_loc.get_piece(piece_att).owner != self.owner:
                locs[loc.top_left_loc] = 'Kill'

            if loc.top_rght_loc is None:
                pass
            elif loc.top_rght_loc.get_piece(piece_att) is None:
                locs[loc.top_rght_loc] = 'StandardMove'
            elif loc.top_rght_loc.get_piece(piece_att).owner != self.owner:
                locs[loc.top_rght_loc] = 'Kill'
            locs_determinded = True
        return locs

    def knight_right_locs(self, loc, piece_att='current_piece'):
        locs = {}
        locs_determinded = False
        while locs_determinded == False:
            if loc.mid_rght_loc is None:
                break
            else:
                loc = loc.mid_rght_loc

            if loc.bot_rght_loc is None:
                pass
            elif loc.bot_rght_loc.get_piece(piece_att) is None:
                locs[loc.bot_rght_loc] = 'StandardMove'
            elif loc.bot_rght_loc.get_piece(piece_att).owner != self.owner:
                locs[loc.bot_rght_loc] = 'Kill'

            if loc.top_rght_loc is None:
                pass
            elif loc.top_rght_loc.get_piece(piece_att) is None:
                locs[loc.top_rght_loc] = 'StandardMove'
            elif loc.top_rght_loc.get_piece(piece_att).owner != self.owner:
                locs[loc.top_rght_loc] = 'Kill'
            locs_determinded = True
        return locs

    def knight_left_locs(self, loc, piece_att='current_piece'):
        locs = {}
        locs_determinded = False
        while locs_determinded == False:
            if loc.mid_left_loc is None:
                break
            else:
                loc = loc.mid_left_loc

            if loc.bot_left_loc is None:
                pass
            elif loc.bot_left_loc.get_piece(piece_att) is None:
                locs[loc.bot_left_loc] = 'StandardMove'
            elif loc.bot_left_loc.get_piece(piece_att).owner != self.owner:
                locs[loc.bot_left_loc] = 'Kill'

            if loc.top_left_loc is None:
                pass
            elif loc.top_left_loc.get_piece(piece_att) is None:
                locs[loc.top_left_loc] = 'StandardMove'
            elif loc.top_left_loc.get_piece(piece_att).owner != self.owner:
                locs[loc.top_left_loc] = 'Kill'
            locs_determinded = True
        return locs



    def promoted_pawn_check(self, possible_moves):
        for move in possible_moves:
            if move.rowID_str == '1' or move.rowID_str == '8':
                possible_moves[move] = 'Promotion'
        return possible_moves

    def bishop_possible_moves(self, loc, previous_turn, piece_att='current_piece'):
        possible_moves = {}
        possible_moves.update(self.find_bottom_right(loc, piece_att))
        possible_moves.update(self.find_top_right(loc, piece_att))
        possible_moves.update(self.find_bottom_left(loc, piece_att))
        possible_moves.update(self.find_top_left(loc, piece_att))
        return possible_moves

    def get_king_loc(self):
        pass

    def king_find_bottom_right(self, loc, piece_att='current_piece'):
        bottom_right = {}
        if loc.bot_rght_loc is None:
            return bottom_right
        elif loc.bot_rght_loc.get_piece(piece_att) is None:
            bottom_right[loc.bot_rght_loc] = 'StandardMove'
            return bottom_right
        elif loc.bot_rght_loc.get_piece(piece_att).owner == self.owner:
            return bottom_right
        elif loc.bot_rght_loc.get_piece(piece_att).owner != self.owner:
            bottom_right[loc.bot_rght_loc] = 'Kill'
            return bottom_right

    def king_find_bottom_center(self, loc, piece_att='current_piece'):
        bottom_center = {}
        if loc.bot_cent_loc is None:
            return bottom_center
        elif loc.bot_cent_loc.get_piece(piece_att) is None:
            bottom_center[loc.bot_cent_loc] = 'StandardMove'
            return bottom_center
        elif loc.bot_cent_loc.get_piece(piece_att).owner == self.owner:
            return bottom_center
        elif loc.bot_cent_loc.get_piece(piece_att).owner != self.owner:
            bottom_center[loc.bot_cent_loc] = 'Kill'
            return bottom_center

    def king_find_bottom_left(self, loc, piece_att='current_piece'):
        bottom_left = {}
        if loc.bot_left_loc is None:
            return bottom_left
        elif loc.bot_left_loc.get_piece(piece_att) is None:
            bottom_left[loc.bot_left_loc] = 'StandardMove'
            return bottom_left
        elif loc.bot_left_loc.get_piece(piece_att).owner == self.owner:
            return bottom_left
        elif loc.bot_left_loc.get_piece(piece_att).owner != self.owner:
            bottom_left[loc.bot_left_loc] = 'Kill'
            return bottom_left

    def king_find_mid_right(self, loc, piece_att='current_piece'):
        mid_right = {}
        if loc.mid_rght_loc is None:
            return mid_right
        elif loc.mid_rght_loc.get_piece(piece_att) is None:
            mid_right[loc.mid_rght_loc] = 'StandardMove'
            return mid_right
        elif loc.mid_rght_loc.get_piece(piece_att).owner == self.owner:
            return mid_right
        elif loc.mid_rght_loc.get_piece(piece_att).owner != self.owner:
            mid_right[loc.mid_rght_loc] = 'Kill'
            return mid_right

    def king_find_mid_left(self, loc, piece_att='current_piece'):
        mid_left = {}
        if loc.mid_left_loc is None:
            return mid_left
        elif loc.mid_left_loc.get_piece(piece_att) is None:
            mid_left[loc.mid_left_loc] = 'StandardMove'
            return mid_left
        elif loc.mid_left_loc.get_piece(piece_att).owner == self.owner:
            return mid_left
        elif loc.mid_left_loc.get_piece(piece_att).owner != self.owner:
            mid_left[loc.mid_left_loc] = 'Kill'
            return mid_left

    def king_find_top_right(self, loc, piece_att='current_piece'):
        top_right = {}
        if loc.top_rght_loc is None:
            return top_right
        elif loc.top_rght_loc.get_piece(piece_att) is None:
            top_right[loc.top_rght_loc] = 'StandardMove'
            return top_right
        elif loc.top_rght_loc.get_piece(piece_att).owner == self.owner:
            return top_right
        elif loc.top_rght_loc.get_piece(piece_att).owner != self.owner:
            top_right[loc.top_rght_loc] = 'Kill'
            return top_right

    def king_find_top_center(self, loc, piece_att='current_piece'):
        top_center = {}
        if loc.top_cent_loc is None:
            return top_center
        elif loc.top_cent_loc.get_piece(piece_att) is None:
            top_center[loc.top_cent_loc] = 'StandardMove'
            return top_center
        elif loc.top_cent_loc.get_piece(piece_att).owner == self.owner:
            return top_center
        elif loc.top_cent_loc.get_piece(piece_att).owner != self.owner:
            top_center[loc.top_cent_loc] = 'Kill'
            return top_center

    def king_find_top_left(self, loc, piece_att='current_piece'):
        top_left = {}
        if loc.top_left_loc is None:
            return top_left
        elif loc.top_left_loc.get_piece(piece_att) is None:
            top_left[loc.top_left_loc] = 'StandardMove'
            return top_left
        elif loc.top_left_loc.get_piece(piece_att).owner == self.owner:
            return top_left
        elif loc.top_left_loc.get_piece(piece_att).owner != self.owner:
            top_left[loc.top_left_loc] = 'Kill'
            return top_left

    def check_if_under_threat(self, loc, previous_turn, piece_att='current_piece'):
        piece_type = 'knight'
        status = self.check_moves(moves=self.knight_possible_moves(loc, previous_turn, piece_att), piece_type=piece_type, piece_att=piece_att)
        if status == True:
            return True
        piece_type = 'bishop'
        status = self.check_moves(moves=self.bishop_possible_moves(loc, previous_turn,piece_att), piece_type=piece_type, piece_att=piece_att)
        if status == True:
            return True
        piece_type = 'king'
        status = self.check_moves(moves=self.king_standard_moves(loc, previous_turn,piece_att), piece_type=piece_type, piece_att=piece_att)
        if status == True:
            return True
        piece_type = 'queen'
        status = self.check_moves(moves=self.queen_possible_moves(loc, previous_turn, piece_att), piece_type=piece_type, piece_att=piece_att)
        if status == True:
            return True
        piece_type = 'rook'
        status = self.check_moves(moves=self.rook_possible_moves(loc, previous_turn,piece_att), piece_type=piece_type, piece_att=piece_att)
        if status == True:
            return True
        piece_type = 'pawn'
        status = self.threatening_pawn(loc, previous_turn, piece_att)
        if status == True:
            return True
        return False

    def set_under_threat(self, loc, previous_turn):
        self.under_threat = self.check_if_under_threat(loc, previous_turn)


    def threatening_pawn(self, loc, previous_turn, piece_att='current_piece'):
        if self.enpassant_threat(loc, previous_turn) == True:
            return True
        if (loc.get_piece(piece_att) is not None) and \
                (loc.get_piece(piece_att).initial_location.rowID == 1 or
                 loc.get_piece(piece_att).initial_location.rowID == 2):
            if loc.bot_left_loc is not None and loc.bot_left_loc.get_piece(piece_att) is not None \
                    and loc.bot_left_loc.get_piece(piece_att).key.__contains__('pawn')\
                    and loc.bot_left_loc.get_piece(piece_att).owner != loc.get_piece(piece_att).owner:
                return True
            if loc.bot_rght_loc is not None and loc.bot_rght_loc.get_piece(piece_att) is not None \
                    and loc.bot_rght_loc.get_piece(piece_att).key.__contains__('pawn')\
                    and loc.bot_rght_loc.get_piece(piece_att).owner != loc.get_piece(piece_att).owner:
                return True
        if (loc.get_piece(piece_att) is not None) and \
                (loc.get_piece(piece_att).initial_location.rowID == 7 or
                 loc.get_piece(piece_att).initial_location.rowID == 8):
            if loc.top_left_loc is not None and loc.top_left_loc.get_piece(piece_att) is not None \
                    and loc.top_left_loc.get_piece(piece_att).key.__contains__('pawn')\
                    and loc.top_left_loc.get_piece(piece_att).owner != loc.get_piece(piece_att).owner:
                return True
            if loc.top_rght_loc is not None and loc.top_rght_loc.get_piece(piece_att) is not None \
                    and loc.top_rght_loc.get_piece(piece_att).key.__contains__('pawn')\
                    and loc.top_rght_loc.get_piece(piece_att).owner != loc.get_piece(piece_att).owner:
                return True
        return False



    def enpassant_threat(self, loc, previous_turn, piece_att='current_piece'):
        last_moved_piece = False
        if self == previous_turn['moved_piece']:
            last_moved_piece = True
        pt = False
        if previous_turn['turn_type'] == 'TwoSpacePawn':
            pt = True
        ml_loc = loc.mid_left_loc
        mr_loc = loc.mid_rght_loc
        if last_moved_piece and pt and\
                (
                    (
                        ml_loc is not None
                        and ml_loc.get_piece(piece_att) is not None
                        and ml_loc.get_piece(piece_att).key.__contains__('pawn')
                    )
                or
                    (
                                mr_loc is not None
                     and mr_loc.get_piece(piece_att) is not None
                     and mr_loc.get_piece(piece_att).key.__contains__('pawn')
                    )
                ):
            return True
        return False

    def check_moves(self, moves, piece_type, piece_att='current_piece'):
        for move in moves:
            if move.get_piece(piece_att) is not None and move.get_piece(piece_att).key.__contains__(piece_type):
                return True
        return False

    def hypothetical_threat_move(self, loc, previous_turn, move, king_loc, board):
        def set_each_hypothetical_loc():
            for row in range(1,9):
                for column in board.structure:
                    location = board.structure[column][str(row)]
                    if location == loc:
                        location.set_hypothetical_piece(None)
                    elif location == move:
                        location.set_hypothetical_piece(loc.current_piece)
                        location.hypothetical_piece.initial_location = loc.current_piece.initial_location
                    else:
                        location.set_hypothetical_piece(location.current_piece)
                        if location.current_piece is not None:
                            location.hypothetical_piece.initial_location = location.current_piece.initial_location


        def set_each_hypothetical_loc_reset():
            for row in range(1,9):
                for column in board.structure:
                    location = board.structure[column][str(row)]
                    location.set_hypothetical_piece(None)

        set_each_hypothetical_loc()
        # board.present_board_hypothetical() # needed only for testing
        hypothetical_king_loc = self.find_hypothetical_king(loc, board)
        hypothetical_threat = self.check_if_under_threat(hypothetical_king_loc, previous_turn, 'hypothetical_piece')
        set_each_hypothetical_loc_reset()
        return hypothetical_threat

    def find_hypothetical_king(self, loc, board):
        player = loc.current_piece.owner
        for row in range(1, 9):
            for column in board.structure:
                location = board.structure[column][str(row)]
                if location.hypothetical_piece is not None \
                    and location.hypothetical_piece.owner == player \
                    and location.hypothetical_piece.key.__contains__('king'):
                        return location



