from time import time


class Location:
    def __init__(self, column_name, row, column_key, board):
        self.column_name = column_name
        self.rowID = row
        self.rowID_str = str(row)
        self.column_key = column_key
        self.column_key_str = str(column_key)
        self.name = f'{column_name.upper()}{row}'
        self.key = f'{column_key}{row}'
        self.current_piece = None
        self.hypothetical_piece = None
        self.board = board
        self.top_left_loc = None
        self.top_cent_loc = None
        self.top_rght_loc = None
        self.mid_left_loc = None
        self.mid_rght_loc = None
        self.bot_left_loc = None
        self.bot_cent_loc = None
        self.bot_rght_loc = None

    def get_top_left_loc(self):
        if self.column_key > 1 and self.rowID < 8:
            new_column = str(self.column_key - 1)
            new_row = str(self.rowID + 1)
            return self.board.structure[new_column][new_row]
        else:
            return None

    def get_top_center_loc(self):
        if self.rowID < 8:
            new_row = str(self.rowID + 1)
            return self.board.structure[self.column_key_str][new_row]
        else:
            return None

    def get_top_right_loc(self):
        if self.column_key < 8 and self.rowID < 8:
            new_column = str(self.column_key + 1)
            new_row = str(self.rowID + 1)
            return self.board.structure[new_column][new_row]
        else:
            return None

    def get_mid_left_loc(self):
        if self.column_key > 1:
            new_column = str(self.column_key - 1)
            return self.board.structure[new_column][self.rowID_str]
        else:
            return None

    def get_mid_right_loc(self):
        if self.column_key < 8:
            new_column = str(self.column_key + 1)
            return self.board.structure[new_column][self.rowID_str]
        else:
            return None

    def get_bottom_left_loc(self):
        if self.column_key > 1 and self.rowID > 1:
            new_column = str(self.column_key - 1)
            new_row = str(self.rowID - 1)
            return self.board.structure[new_column][new_row]
        else:
            return None

    def get_bottom_center_loc(self):
        if self.rowID > 1:
            new_row = str(self.rowID - 1)
            return self.board.structure[self.column_key_str][new_row]
        else:
            return None

    def get_bottom_right_loc(self):
        if self.column_key < 8 and self.rowID > 1:
            new_column = str(self.column_key + 1)
            new_row = str(self.rowID - 1)
            return self.board.structure[new_column][new_row]
        else:
            return None

    def add_piece(self, piece, test='current_piece'):
        new_test = self.set_piece(test)
        self.current_piece = piece
        piece.set_location(self)

    def get_piece(self, att):
        return getattr(self, att)

    def remove_piece(self):
        pass

    def set_hypothetical_piece(self, piece):
        self.hypothetical_piece = piece

    def test_location(self):
        start = time()
        print(self.get_top_left_loc())
        print(self.get_top_center_loc())
        print(self.get_top_right_loc())
        print(self.get_mid_left_loc())
        print(self.get_mid_right_loc())
        print(self.get_bottom_left_loc())
        print(self.get_bottom_center_loc())
        print(self.get_bottom_right_loc())
        end = time()
        print(end - start)

    def present_location(self):
        if self.current_piece is None:
            return f'[___]'
        else:
            return f'[{self.current_piece.short_hand_name}]'

    def present_location_hypothetical(self):
        if self.hypothetical_piece is None:
            return f'[___]'
        else:
            return f'[{self.hypothetical_piece.short_hand_name}]'

    def present_location_under_threat(self):
        if self.current_piece is None:
            return f'[_____]'
        else:
            if self.current_piece.under_threat:
                return f'[True_]'
            else:
                return f'[False]'

    def set_piece(self, piece):
        self.current_piece = piece

    def set_neighboring_loc(self):
        self.top_left_loc = self.get_top_left_loc()
        self.top_cent_loc = self.get_top_center_loc()
        self.top_rght_loc = self.get_top_right_loc()
        self.mid_left_loc = self.get_mid_left_loc()
        self.mid_rght_loc = self.get_mid_right_loc()
        self.bot_left_loc = self.get_bottom_left_loc()
        self.bot_cent_loc = self.get_bottom_center_loc()
        self.bot_rght_loc = self.get_bottom_right_loc()
