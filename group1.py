import random

def group1(self, board):
    # Get all possible moves
    possible_moves = self.getPossibleMoves(board)

    # If no moves are possible, end the turn
    if not possible_moves:
        self.game.end_turn()
        return

    best_move = None
    best_choice = None
    best_score = -float('inf')  # Start with the worst possible score

    for move in possible_moves:
        current_pos = move[0], move[1]
        for choice in move[2]:
            # Using 'getSquare' if that is the correct method
            piece = board.getSquare(current_pos[0], current_pos[1]).squarePiece

            # Simulate the move on the board
            board.move_piece(current_pos[0], current_pos[1], choice[0], choice[1])

            # Initialize captured_piece to None
            captured_piece = None

            # Simulate capture if choice is a valid move (not an adjacent square)
            if choice not in board.getAdjacentSquares(current_pos[0], current_pos[1]):
                captured_x = current_pos[0] + (choice[0] - current_pos[0]) // 2
                captured_y = current_pos[1] + (choice[1] - current_pos[1]) // 2
                captured_piece = board.getSquare(captured_x, captured_y).squarePiece
                board.remove_piece(captured_x, captured_y)

            # Evaluate the board state after making the move
            score = self.evaluate(board)  # Storing the score after the move
            
            # Give bonus if a piece was captured
            if captured_piece:
                score += 100
            
            # If the new score is better, update the best move and choice
            if score > best_score:
                best_score = score
                best_move = move
                best_choice = choice

            # Undo the move after evaluation to reset the board
            board.move_piece(choice[0], choice[1], current_pos[0], current_pos[1])
            if captured_piece:
                board.getSquare(captured_x, captured_y).squarePiece = captured_piece

    # If no best move was found, choose randomly
    if best_move is None or best_choice is None:
        best_move = random.choice(possible_moves)
        best_choice = random.choice(best_move[2])

    return best_move, best_choice
