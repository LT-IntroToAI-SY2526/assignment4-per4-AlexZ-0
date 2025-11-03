# NOTE: Until you fill in the TTTBoard class mypy is going to give you multiple errors
# talking about unimplemented class attributes, don't worry about this as you're working


class TTTBoard:
    """A tic tac toe board

    Attributes:
        board - a list of '*'s, 'X's & 'O's. 'X's represent moves by player 'X', 'O's
            represent moves by player 'O' and '*'s are spots no one has yet played on
    """

    def __init__(self):
        self.board = ["*"] * 9

    def __str__(self):
        """Return a printable version of the board"""
        rows = [self.board[i:i+3] for i in range(0, 9, 3)]
        return "\n".join(" ".join(row) for row in rows)

    def make_move(self, player: str, pos: int) -> bool:
        """Places the player's move if valid.

        Args:
            player - either 'X' or 'O'
            pos - integer from 0 to 8 (inclusive)
        Returns:
            True if move was successful, False otherwise
        """
        if pos < 0 or pos > 8:
            raise ValueError(f"Position {pos} out of range (0–8).")

        if self.board[pos] != "*":
            print("Spot already taken!")
            return False

        self.board[pos] = player
        return True

    def has_won(self, player: str) -> bool:
        """Check if the given player has won"""
        b = self.board
        win_positions = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # cols
            (0, 4, 8), (2, 4, 6),             # diagonals
        ]
        return any(b[a] == b[b_] == b[c] == player for a, b_, c in win_positions)

    def is_full(self) -> bool:
        """Return True if board is full"""
        return "*" not in self.board

    def game_over(self) -> bool:
        """Return True if someone won or board is full"""
        return self.has_won("X") or self.has_won("O") or self.is_full()

    def clear(self):
        """Reset the board to initial empty state"""
        self.board = ["*"] * 9



def play_tic_tac_toe() -> None:
    """Uses your class to play TicTacToe"""

    def is_int(maybe_int: str):
        """Returns True if val is int, False otherwise

        Args:
            maybe_int - string to check if it's an int

        Returns:
            True if maybe_int is an int, False otherwise
        """
        try:
            int(maybe_int)
            return True
        except ValueError:
            return False

    brd = TTTBoard()
    players = ["X", "O"]
    turn = 0

    while not brd.game_over():
        print(brd)
        move: str = input(f"Player {players[turn]} what is your move? ")

        if not is_int(move):
            raise ValueError(
                f"Given invalid position {move}, position must be integer between 0 and 8 inclusive"
            )

        if brd.make_move(players[turn], int(move)):
            turn = not turn

    print(f"\nGame over!\n\n{brd}")
    if brd.has_won(players[0]):
        print(f"{players[0]} wins!")
    elif brd.has_won(players[1]):
        print(f"{players[1]} wins!")
    else:
        print(f"Board full, cat's game!")


if __name__ == "__main__":
    # here are some tests. These are not at all exhaustive tests. You will DEFINITELY
    # need to write some more tests to make sure that your TTTBoard class is behaving
    # properly.
    brd = TTTBoard()
    brd.make_move("X", 8)
    brd.make_move("O", 7)

    assert brd.game_over() == False

    brd.make_move("X", 5)
    brd.make_move("O", 6)
    brd.make_move("X", 2)

    assert brd.has_won("X") == True
    assert brd.has_won("O") == False
    assert brd.game_over() == True

    brd.clear()

    assert brd.game_over() == False

    brd.make_move("O", 3)
    brd.make_move("O", 4)
    brd.make_move("O", 5)

    assert brd.has_won("X") == False
    assert brd.has_won("O") == True
    assert brd.game_over() == True

    print("All tests passed!")

    # uncomment to play!
    play_tic_tac_toe()
