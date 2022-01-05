import json
from ChessGame.pieceTypes.queen import Queen
from ChessGame.pieceTypes.rook import Rook
from ChessGame.pieceTypes.bishop import Bishop
from ChessGame.pieceTypes.knight import Knight
from ChessGame.playerTypes.player import Player
from ChessGame.playerTypes.rand_bot import RandBot
from ChessGame.playerTypes.kill_bot import KillBot
from ChessGame.pieceTypes.piece import Piece
from ChessGame.board import Board
from ChessGame.config import possible_piece_types
from ChessGame.config2 import players_pieces_map, turn_types


class Game:
    def __init__(self, bot_game=False, player_1_bot_type=False, player_2_bot_type=False):
        self.board = self.setBoard()
        self.players = {'1': None, '2': None}
        self.game_status = 'Introduction'
        self.previous_turn = {'old_loc': None, 'new_loc': None, 'moved_piece': None, 'turn_type': None, 'check_status': False}
        self.winner = None
        self.loser = None
        self.turn_count = 0
        self.draw = False
        self.stalemate = False
        self.game_details = []
        self.bot_game = bot_game
        self.player_1_bot_type = player_1_bot_type
        self.player_2_bot_type = player_2_bot_type

    def set_all_location_attributes(self):
        for column in range(1, 9):
            for row in range(1, 9):
                column_key = str(column)
                row_key = str(row)
                self.board.structure[column_key][row_key].set_neighboring_loc()

    def set_all_current_threat_status(self):
        for row in range(1, 9):
            row_str = str(row)
            for column in self.board.structure:
                loc = self.board.structure[column][row_str]
                if loc.current_piece is not None:
                    loc.current_piece.set_under_threat(loc, self.previous_turn)

    def set_players_pieces(self, player):
        for piece_key in players_pieces_map:
            piece_type = players_pieces_map[piece_key]
            for item in possible_piece_types:
                if item['name'] == piece_type:
                    class_sub_type = item['cls']
                    piece = class_sub_type(piece_key, player)
                    piece.set_starting_position(self.board)
                    player.add_piece(piece)
                    # self.set_initial_piece_location(piece)

    def setPlayer(self, player_count):
        if self.bot_game == True:
            if player_count == 1:
                player_type = self.player_1_bot_type
            else:
                player_type = self.player_2_bot_type
            player_name = str(player_count)
            if player_type == 'RANDBOT':
                player = RandBot(player_count, player_name)
            elif player_type == 'KILLBOT':
                player = KillBot(player_count, player_name)
            self.set_players_pieces(player)
            return player
        else:
            valid_entree = False
            while valid_entree == False:
                player_type = input(f'PLayer {player_count}, are you a Randbot, Killbot, or person?').upper()
                if player_type == 'RANDBOT' or player_type == 'PERSON' or player_type == 'KILLBOT':
                    valid_entree = True
            player_name = input(f'Player {player_count}, what is your name?')
            if player_type == 'RANDBOT':
                player = RandBot(player_count, player_name)
            elif player_type == 'KILLBOT':
                player = KillBot(player_count, player_name)
            else:
                player = Player(player_count, player_name)
            self.set_players_pieces(player)
            return player

    def setBoard(self):
        board = Board()
        return board

    def validate_draw(self):
        piece_count = 0
        for player in self.players:
            for piece in self.players[player].pieces:
                if piece.alive:
                    piece_count += 1
        if piece_count <= 2:
            self.draw = True


    def run(self):
        self.introduction()
        while self.winner is None and self.draw == False:
            self.turn_count += 1
            self.turn()
        self.conclusion()

    def introduction(self):
        print("Welcome to Chess")
        Piece.count = 0
        self.set_all_location_attributes()
        for player_count in self.players:
            player = self.setPlayer(int(player_count))
            self.players[player_count] = player
        self.game_status = '1'

    def turn(self):
        #self.board.present_board() #Present the user the board
        active_player = self.players[self.game_status] #Player makes a move
        self.move(active_player)
        if self.winner is None:
            self.next_player()

    def next_player(self):
        if self.game_status == '1':#player 1
            self.game_status = '2' #player 2
        else:
            self.game_status = '1' #player 1

    def move(self, active_player):
        finished_move = False
        while finished_move == False:
            if self.previous_turn['check_status'] == True:
                print(f'{active_player.name}, your king is in check.')
            selected_piece = active_player.select_piece(self.previous_turn, turn_count=self.turn_count)
            old_loc = selected_piece.find_loc(self.board)
            possible_locations = selected_piece.find_possible_moves(old_loc, self.previous_turn)
            if len(possible_locations.keys()) == 0 and (type(active_player) == Player):
                print('The piece selected has no possible moves. Select another piece.')
                continue
            elif len(possible_locations.keys()) == 0 and type(active_player) != Player:
                continue
            #print(f'Possible Locations:{self.display_possible_locations(possible_locations)}')
            possible_locations = self.validate_moves(old_loc, selected_piece, possible_locations)
            if len(possible_locations.keys()) == 0 and type(active_player) == Player:
                print('The piece selected has no possible moves. Select another piece.')
                continue
            elif len(possible_locations.keys()) == 0 and type(active_player) != Player:
                continue
            #print(f'Validated Locations:{self.display_possible_locations(possible_locations)}')
            new_loc, turn_type = self.select_piece_new_location(selected_piece, possible_locations)
            self.finalize_move(old_loc, new_loc, selected_piece, turn_type)
            finished_move = True

    def validate_moves(self, old_loc, selected_piece, possible_locations):
        validated_possible_moves = {}
        for move in possible_locations:
            hypothetical_threat = selected_piece.hypothetical_threat_move(old_loc, self.previous_turn, move, self.find_own_king(), self.board)
            if not hypothetical_threat:
                validated_possible_moves[move] = possible_locations[move]
        return validated_possible_moves

    def select_piece_new_location(self, selected_piece, possible_locations):
        location, turn_type = self.players[self.game_status].select_piece_new_location(
            selected_piece, possible_locations, turn_count=self.turn_count)
        return location, turn_type

    def finalize_move(self, old_loc, new_loc, piece, turn_type):
        if turn_type == 'EnPassant': #Checking for rare types of turns
            en_passant_kill = piece.en_passant_kill#status, not kill
            en_passant_kill.current_piece.set_dead()
            en_passant_kill.set_piece(None)
            piece.set_en_passant_kill(None)
        elif turn_type == 'Promotion': #Checking for rare types of turns
            piece.set_dead()
            piece = self.promotion(piece.owner)
        elif turn_type == 'Castling':
            if piece.castling_3_king_loc == new_loc:
                rook_old_loc = piece.paired_3_rook_old_loc
                rook_new_loc = piece.paired_3_rook_new_loc
                rook = rook_old_loc.current_piece
                rook_old_loc.set_piece(None)
                rook_new_loc.set_piece(rook)
                rook.moved_status = True
                piece.moved_status = True

            else:
                rook_old_loc = piece.paired_4_rook_old_loc
                rook_new_loc = piece.paired_4_rook_new_loc
                rook = rook_old_loc.current_piece
                rook_old_loc.set_piece(None)
                rook_new_loc.set_piece(rook)
                rook.moved_status = True
                piece.moved_status = True

        if new_loc.current_piece is not None:
            new_loc.current_piece.set_dead()

        old_loc.set_piece(None)
        new_loc.set_piece(piece)
        piece.moved_status = True

        self.set_all_current_threat_status()
        king_loc = self.find_apponent_king()
        self.previous_turn['old_loc'] = old_loc
        self.previous_turn['new_loc'] = new_loc
        self.previous_turn['moved_piece'] = piece
        self.previous_turn['turn_type'] = turn_type
        self.previous_turn['check_status'] = king_loc.current_piece.under_threat
        #self.display_turn_details()
        self.validate_draw()
        self.save_turn_details()
        if self.previous_turn['check_status'] == True:
            check_mate = king_loc.current_piece.validate_check_mate(king_loc, self.previous_turn, self.board)
            if check_mate:
                self.finish_game()
        else:
            opponent = king_loc.current_piece.owner
            stalemate = self.stalemate_validate(opponent)
            drawn_out = self.drawn_out()
            if stalemate:
                self.stalemate = True
            if stalemate or drawn_out:
                self.draw = True
                self.conclusion()
        # self.board.present_board_statuses() # needed only for testing

    def drawn_out(self):
        if self.turn_count > 250:
            return True
        return False

    def stalemate_validate(self, player):
        for piece in player.pieces:
            if piece.alive:
                loc = piece.find_loc(self.board)
                possible_locs = piece.find_possible_moves(piece.find_loc(self.board), self.previous_turn)
                validated_locs = self.validate_moves(loc, piece, possible_locs)
                if len(validated_locs) > 0:
                    return False
        return True

    def present_turn(self):
        print(f'{self.previous_turn}')

    def promotion(self, owner):
        if owner.pieces[0].initial_location.rowID <= 2:
            initial_row_id = 1
        else:
            initial_row_id = 8
        valid_piece_type = False
        while valid_piece_type == False:
            piece_type = owner.promotion_selection()
            if piece_type == 'QUEEN':
                piece = Queen(piece_key='queen', player=owner)
                piece.set_initial_location(self.search_loc_from_name(f'D{initial_row_id}'))
            elif piece_type == 'ROOK':
                piece = Rook(piece_key='rook', player=owner)
                piece.set_initial_location(self.search_loc_from_name(f'A{initial_row_id}'))
            elif piece_type == 'BISHOP':
                piece = Bishop(piece_key='bishop', player=owner)
                piece.set_initial_location(self.search_loc_from_name(f'C{initial_row_id}'))
            elif piece_type == 'KNIGHT':
                piece = Knight(piece_key='knight', player=owner)
                piece.set_initial_location(self.search_loc_from_name(f'B{initial_row_id}'))
            else:
                print('Invalid piece type')
                continue
            owner.add_piece(piece)
            valid_piece_type = True
            return piece

    def under_threat(self, selected_piece, loc, previous_turn):
        threats = selected_piece.under_threat(loc=loc, previous_turn=previous_turn)

    def find_apponent_king(self):
        if self.game_status == '1':
            for piece in self.players['2'].pieces:
                if piece.key.__contains__('king'):
                    return piece.find_loc(self.board)
        else:
            for piece in self.players['1'].pieces:
                if piece.key.__contains__('king'):
                    return piece.find_loc(self.board)

    def find_own_king(self):
        for piece in self.players[self.game_status].pieces:
            if piece.key.__contains__('king'):
                return piece.find_loc(self.board)

    def finish_game(self):
        self.winner = self.players[self.game_status]
        if self.winner.player_key == 1:
            self.loser = self.players['2']
        else:
            self.loser = self.players['1']

    def search_loc_from_name(self, search_loc):
        for row in range(1,9):
            for column in self.board.structure:
                loc = self.board.structure[column][str(row)]
                if loc.name.upper() == search_loc.upper():
                    return loc

    def conclusion(self):
        if self.winner:
            self.save_game_data()
        #self.board.present_board()
        if self.draw == True:
            print('The game concludes in a draw.')
        else:
            print(f'{self.loser.name} (Player {self.loser.player_key}) is in check mate.')
            print(f'Congragulations {self.winner.name} (Player {self.winner.player_key}), you win!')

    def save_turn_details(self):
        turn_record = {}
        for player in self.players:
            for piece in self.players[player].pieces:
                row_key = f'{self.players[player].player_key}{piece.key}_row'
                col_key = f'{self.players[player].player_key}{piece.key}_col'
                piece_threat = f'{self.players[player].player_key}{piece.key}_threat'
                if piece.alive:
                    loc = piece.find_loc(self.board)
                    col_name = loc.column_key
                    row_name = loc.rowID
                    turn_record[col_key] = col_name
                    turn_record[row_key] = row_name
                    turn_record[piece_threat] = int(piece.under_threat) + 1
                else:
                    turn_record[col_key] = 0
                    turn_record[row_key] = 0
                    turn_record[row_key] = 0
        turn_record['turn_type'] = turn_types[self.previous_turn['turn_type']]
        turn_record['check_status'] = 1 if self.previous_turn['check_status'] else 0
        turn_record['player_turn'] = int(self.previous_turn['moved_piece'].owner.player_key)
        turn_record['old_loc_col'] = self.previous_turn['old_loc'].column_key
        turn_record['old_loc_row'] = self.previous_turn['old_loc'].rowID
        turn_record['new_loc_col'] = self.previous_turn['old_loc'].column_key
        turn_record['new_loc_row'] = self.previous_turn['old_loc'].rowID
        turn_record['turn_number'] = self.turn_count
        counter = 0
        for piece_type in possible_piece_types:
            counter += 1
            if type(self.previous_turn['moved_piece']) == piece_type['cls']:
                turn_record['moved_piece_type'] = counter
        self.game_details.append(turn_record)

    def save_game_data(self):
        player_1_status = 1 if self.winner and self.winner.player_key == 1 else 0
        player_2_status = 1 if self.winner and self.winner.player_key == 2 else 0
        for turn in self.game_details:
            if turn['player_turn'] == 1:
                turn['won'] = player_1_status
            else:
                turn['won'] = player_2_status
        filename = 'GameData.json'
        try:
        # 1. Read file contents
            with open(filename, "r") as file:
                data = json.load(file)
        # 2. Update json object
            for turn in self.game_details:
                data.append(turn)
        # 3. Write json file
            with open(filename, "w") as file:
                json.dump(data, file)
        except Exception as e:
            lst = [{'alice': 24, 'bob': 27}]
            # Write the initial json object (list of dicts)
            with open(filename, mode='w') as f:
                json.dump(self.game_details, f)
            # Append the new dict to the list and overwrite whole file


    # For Testing:
    def display_init_locations(self, player_key):
        for piece in self.players[player_key].pieces:
            print(f'{piece.short_hand_name}, {piece.initial_location.name}')

    # For Testing:
    def display_turn_details(self):
        print(f"Summary - Old Loc:{self.previous_turn['old_loc'].name}, New Loc:{self.previous_turn['new_loc'].name}, Moved Piece:{self.previous_turn['moved_piece'].short_hand_name}, turn_type:{self.previous_turn['turn_type']}")
        print(f'Check Status: {self.previous_turn["check_status"]}')
        print(f'turns{self.turn_count}')
        for player in self.players:
            player_pieces = f'{self.players[player].player_key}:'
            for piece in self.players[player].pieces:
                player_pieces += f' {piece.short_hand_name}, {piece.alive};'
            print(player_pieces)

    # For Testing:
    def display_possible_locations(self, possible_locations):
        locations_str = f'Locs:'
        for loc in possible_locations:
            locations_str += f' {loc.name}, cur:{loc.current_piece.short_hand_name if loc.current_piece else None}, hypo:{loc.hypothetical_piece};'
        return locations_str

