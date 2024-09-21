from tictactoe import TicTacToe
from player import AIPlayer

MOVE_TIMEOUT = 2

def get_move(board, size, team_role):
    game_state = TicTacToe(size, 5, board)
    player_mask = 1 if team_role == 'x' else -1
    ai_player = AIPlayer(player_mask)
    return ai_player.get_move(game_state, MOVE_TIMEOUT)