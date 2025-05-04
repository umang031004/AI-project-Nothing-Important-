import random
from copy import deepcopy

MAX_DEPTH = 2


def group2(self, board):
    def minimax(board, depth, maximizingPlayer):
        if depth == 0 or self.endGameCheck(board):
            return self.evaluate(board), None, None

        possible_moves = self.getPossibleMoves(board)
        if maximizingPlayer:
            maxEval = float('-inf')
            best_move = None
            best_choice = None
            for move in possible_moves:
                for choice in move[2]:
                    new_board = deepcopy(board)
                    self.moveOnBoard(new_board, (move[0], move[1]), choice)
                    eval, _, _ = minimax(new_board, depth - 1, False)
                    if eval > maxEval:
                        maxEval = eval
                        best_move = move
                        best_choice = choice
            return maxEval, best_move, best_choice
        else:
            minEval = float('inf')
            best_move = None
            best_choice = None
            for move in possible_moves:
                for choice in move[2]:
                    new_board = deepcopy(board)
                    self.moveOnBoard(new_board, (move[0], move[1]), choice)
                    eval, _, _ = minimax(new_board, depth - 1, True)
                    if eval < minEval:
                        minEval = eval
                        best_move = move
                        best_choice = choice
            return minEval, best_move, best_choice

    _, best_move, best_choice = minimax(board, MAX_DEPTH, True)
    return best_move, best_choice
