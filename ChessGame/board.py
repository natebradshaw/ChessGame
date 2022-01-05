from ChessGame.location import Location
from string import ascii_lowercase


class Board:

    def __init__(self):#attributes need to go in structure then locations_dict
        self.structure = self.create_structure()
        #self.locations_dict = self.create_locations_dict()

    def create_structure(self):
        structure = {}
        for i in range(0, 8):
            column_name = ascii_lowercase[i]
            column_key = i + 1
            column_key_str = str(column_key)
            row = self.create_row(column_name, column_key)
            structure[column_key_str] = row
        return structure

    def create_row(self, column_name, column_key):
        row = {}
        for loc in range(1, 9):
            location = Location(column_name=column_name, row=loc, column_key=column_key, board=self)
            loc_str = str(loc)
            row[loc_str] = location
        return row

    def create_locations_dict(self):
        location_dict = {}
        for column in self.structure:
            for row in self.structure[column]:
                loc = self.structure[column][row]
                location_dict[loc] = None
        return location_dict

    def present_board(self):
        header = '  '
        for column in self.structure:
            column_name = self.structure[column]['1'].column_name
            column_formatted = f'|={column_name.upper()}=|'
            header+=column_formatted
        print(header)
        for row in range(8,0,-1):
            row_str = str(row)
            line = f' {row_str}'
            for column in self.structure:
                loc = self.structure[column][row_str]
                line += loc.present_location()
            print(line)

    # needed only for testing
    def present_board_hypothetical(self):
        header = '  '
        for column in self.structure:
            column_name = self.structure[column]['1'].column_name
            column_formatted = f'|={column_name.upper()}=|'
            header+=column_formatted
        print(header)
        for row in range(1,9):
            row_str = str(row)
            line = f' {row_str}'
            for column in self.structure:
                loc = self.structure[column][row_str]
                line += loc.present_location_hypothetical()
            print(line)

    # needed only for testing
    def present_board_statuses(self):
        header = '  '
        for column in self.structure:
            column_name = self.structure[column]['1'].column_name
            column_formatted = f'|__{column_name.upper()}__|'
            header += column_formatted
        print(header)
        for row in range(1, 9):
            row_str = str(row)
            line = f' {row_str}'
            for column in self.structure:
                loc = self.structure[column][row_str]
                line += loc.present_location_under_threat()
            print(line)





