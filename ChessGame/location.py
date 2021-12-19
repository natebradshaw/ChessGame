from time import time


class Location:
    def __init__(self, column_name, row, column_key, board):
        self.column_name = column_name
        self.rowID = row
        self.column_key = column_key
        self.name = f'{column_name.upper()}{row}'
        self.key = f'{column_key}{row}'
        self.current_piece = None
        self.board = board

    def get_top_left_loc(self):
        if self.column_key > 1 or self.rowID > 1:
            new_column = self.column_key - 1
            new_row = self.rowID - 1
            return self.board.structure[new_column][new_row]
        else:
            return None

    def get_top_center_loc(self):
        if self.rowID > 1:
            new_row = self.rowID - 1
            return self.board.structure[self.column_key][new_row]
        else:
            return None

    def get_top_right_loc(self):
        if self.column_key < 8 and self.rowID > 1:
            new_column = self.column_key + 1
            new_row = self.rowID - 1
            return self.board.structure[new_column][new_row]
        else:
            return None

    def get_mid_left_loc(self):
        if self.column_key > 1:
            new_column = self.column_key - 1
            return self.board.structure[new_column][self.rowID]
        else:
            return None

    def get_mid_right_loc(self):
        if self.column_key < 8:
            new_column = self.column_key + 1
            return self.board.structure[new_column][self.rowID]
        else:
            return None

    def get_bottom_left_loc(self):
        if self.column_key > 1 and self.rowID < 8:
            new_column = self.column_key - 1
            new_row = self.rowID + 1
            return self.board.structure[new_column][new_row]
        else:
            return None

    def get_bottom_center_loc(self):
        if self.rowID < 8:
            new_row = self.rowID + 1
            return self.board.structure[self.column_key][new_row]
        else:
            return None

    def get_bottom_right_loc(self):
        if self.column_key < 8 and self.rowID < 8:
            new_column = self.column_key + 1
            new_row = self.rowID + 1
            return self.board.structure[new_column][new_row]
        else:
            return None

    def add_piece(self, piece):
        self.current_piece = piece
        piece.set_location(self)

    def remove_piece(self):
        pass

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

    def set_piece(self, piece):
        self.current_piece = piece
