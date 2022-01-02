from ChessGame.pieceTypes.bishop import Bishop
from ChessGame.pieceTypes.king import King
from ChessGame.pieceTypes.knight import Knight
from ChessGame.pieceTypes.pawn import Pawn
from ChessGame.pieceTypes.queen import Queen
from ChessGame.pieceTypes.rook import Rook

possible_piece_types = (
    {'name': 'pawn', 'cls': Pawn},
    {'name': 'rook', 'cls': Rook},
    {'name': 'knight', 'cls': Knight},
    {'name': 'bishop', 'cls': Bishop},
    {'name': 'king', 'cls': King},
    {'name': 'queen', 'cls': Queen},
)
