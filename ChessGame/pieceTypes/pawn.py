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

        else: #player 2
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
                and mid_left.current_piece == previous_turn['moved_piece']: #Enpassant left
            self.en_passant_kill = mid_left
            possible_moves[top_left] = 'EnPassant'
        if previous_turn['turn_type'] == 'TwoSpacePawn' and mid_rght is not None \
                and mid_rght.current_piece == previous_turn['moved_piece']: #Enpassant right
            self.en_passant_kill = mid_rght
            possible_moves[top_rght] = 'EnPassant'
        if top_left is not None and top_left.current_piece is not None: #diagonal left attack
            if top_left.current_piece.owner != self.owner:
                possible_moves[top_left] = 'Kill'
        if top_rght is not None and top_rght.current_piece is not None: #diagonal right attack
            if top_rght.current_piece.owner != self.owner:
                possible_moves[top_rght] = 'Kill'
        if cent is not None and cent.current_piece is None: #directly ahead
            possible_moves[cent] = 'StandardMove'
        if self.initial_location == loc and cent is not None and two_up_cent is not None \
                and cent.current_piece is None and two_up_cent.current_piece is None:#initial move with two spaces
            possible_moves[two_up_cent] = 'TwoSpacePawn'
        return possible_moves





