from ChessGame.pieceTypes.queen import Queen
from ChessGame.pieceTypes.rook import Rook
from ChessGame.pieceTypes.bishop import Bishop
from ChessGame.pieceTypes.knight import Knight
from ChessGame.player import Player
from ChessGame.pieceTypes.piece import Piece
from ChessGame.board import Board
from ChessGame.config import possible_piece_types
from ChessGame.config2 import players_pieces_map


class Game:
    def __init__(self):
        self.board = self.setBoard()
        self.players = {'1': None, '2': None}
        self.game_status = 'Introduction'
        self.previous_turn = {'old_loc': None, 'new_loc': None, 'moved_piece': None, 'turn_type': None, 'check_status': None}
        self.winner = None
        self.loser = None

    def run(self):
        self.introduction()
        while self.winner is None:
            self.turn()
        self.conclusion()

    def introduction(self):
        print("Welcome to Chess")
        self.set_all_location_attributes()
        for player_count in self.players:
            player = self.setPlayer(int(player_count))
            self.players[player_count] = player
        self.game_status = '1'

    def set_all_location_attributes(self):
        for column in range(1, 9):
            for row in range(1, 9):
                column_key = str(column)
                row_key = str(row)
                self.board.structure[column_key][row_key].set_neighboring_loc()

    def turn(self):
        self.board.present_board() #Present the user the board
        active_player = self.players[self.game_status] #Player makes a move
        self.move(active_player)
        self.next_player()

    def move(self, active_player):
        finished_move = False
        while finished_move == False:
            if self.previous_turn['check_status'] == 'check':
                old_loc, new_loc, selected_piece, unique_turn_type = self.check_move()
            else:
                selected_piece = active_player.select_piece(self.previous_turn)
                old_loc = selected_piece.find_loc(self.board)
                possible_locations = selected_piece.find_possible_moves(old_loc, self.previous_turn)
                if len(possible_locations.keys()) == 0:
                    print('The piece selected has no possible moves. Select another piece.')
                    continue
                new_loc, turn_type = self.select_piece_new_location(selected_piece, possible_locations)
                self.finalize_move(old_loc, new_loc, selected_piece, turn_type)
                finished_move = True


    def check_move(self):
        pass
        #return old_loc, new_loc, selected_piece, unique_turn_type

    def get_check_status(self):
        return None

    def select_piece_new_location(self, selected_piece, possible_locations):
        valid_location = False
        while valid_location == False:
            selected_location = input(f'You selected {selected_piece.short_hand_name}, which of these locations will you move it to? {self.list_out_possible_locations(possible_locations)}')
            selected_location = selected_location.upper()
            for location in possible_locations:
                if location.name == selected_location:
                    valid_location = True
                    turn_type = possible_locations[location]
                    return location, turn_type
            print(f'invalid location, enter location again. possible locations: {self.list_out_possible_locations(possible_locations)}')

    def list_out_possible_locations(self, possible_locations):
        locs = ''
        for location in possible_locations:
            name_formatted = f'|{location.name}|'
            locs += name_formatted
        return locs

    def finish_game(self):
        winner = self.players[self.game_status]
        if winner.player_key == 1:
            loser = self.players['2']
        else:
            loser = self.players['1']
        self.winner = winner
        self.loser = loser
        self.board.present_board()
        print(f'{loser.name} (Player {loser.player_key}) is in check mate.')
        print(f'Congragulations {winner.name} (Player {winner.player_key}), you win!')

    def promotion(self, owner):
        valid_piece_type = False
        while valid_piece_type == False:
            piece_type = input(f'The pawn is promted! What type would you like it promoted to? '
                           f'Queen, Rook, Bishop, Knight?')
            piece_type_cleaned = piece_type.upper()
            if piece_type_cleaned == 'QUEEN':
                piece = Queen(piece_key='queen', player=owner)

            elif piece_type_cleaned == 'ROOK':
                piece = Rook(piece_key='rook', player=owner)

            elif piece_type_cleaned == 'BISHOP':
                piece = Bishop(piece_key='bishop', player=owner)

            elif piece_type_cleaned == 'KNIGHT':
                piece = Knight(piece_key='knight', player=owner)
            else:
                print('invalid piece type')
                continue
            owner.add_piece(piece)
            valid_piece_type = True
            return piece



        queen = Queen()#maybe change Queen to take in type of initation.
        return queen

    def finalize_move(self, old_loc, new_loc, piece, turn_type):
        if turn_type == 'EnPassant': #Checking for rare types of turns
            en_passant_kill = piece.en_passant_kill#status, not kill
            en_passant_kill.current_piece.set_dead()
            en_passant_kill.set_piece(None)
            piece.set_en_passant_kill(None)
        elif turn_type == 'Promotion': #Checking for rare types of turns
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

        self.previous_turn['old_loc'] = old_loc
        self.previous_turn['new_loc'] = new_loc
        self.previous_turn['moved_piece'] = piece
        self.previous_turn['turn_type'] = turn_type
        self.previous_turn['check_status'] = self.get_check_status()
        if self.previous_turn['check_status'] == 'check_mate':
            self.finish_game()



    def set_players_pieces(self, player):
        for piece_key in players_pieces_map:
            piece_type = players_pieces_map[piece_key]
            for item in possible_piece_types:
                if item['name'] == piece_type:
                    class_sub_type = item['cls']
                    piece = class_sub_type(piece_key, player)
                    piece.set_starting_position(self.board)
                    player.add_piece(piece)
                    #self.set_initial_piece_location(piece)

    # def set_piece_type(self, piece_type):
    #     for item in possible_piece_types:
    #         if item['name'] == piece_type:
    #             piece = item['cls']
    #             return piece

    def next_player(self):
        if self.game_status == '1':#player 1
            self.game_status = '2' #player 2
        else:
            self.game_status = '1' #player 1

    def setPlayer(self, player_count):
        player_name = input(f'Player {player_count}, what is your name?')
        player = Player(player_count, player_name)
        self.set_players_pieces(player)
        return player

    def setBoard(self):
        board = Board()
        return board

    def set_initial_piece_location(self, piece):
        pass
    #run some loop on the location piece map and write the answers only in the location

    def conclusion(self):
        pass




